import json
import struct

import snap7
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import CreateView



class PlcRemoteUse():

	def __init__(self,address,rack,slot):
		self.client = snap7.client.Client()  # формирование обращения к соединению
		self.client.connect(address, rack,  slot)  # подключение к контроллеру. Adress - IP адресс. Rack, slot - выставляються/смотрятся в TIA portal
		self.ves = 0
		self.dataRead= 0
		self.db_read = 3
		self.db_write = 6000
	
	def getOut(self,byte,bit):
		out = self.client.ab_read(int(byte),1)
		value = int.from_bytes(out[0:1], byteorder='little',signed=True)
		bits=bin(value)
		bits= bits.replace("0b","")
		if(len(bits)<8):
			for i in range(8 - len(bits)):
				bits="0"+bits
		bits=bits[::-1]
		try:
			status = bits[bit]
		except:
			status=0
		return status

	def tearDown(self):
		self.client.disconnect()
		self.client.destroy()

	def getSatusAllBitInByte(self,byte):
		byte=int(byte)
		retVal = self.client.db_read(self.db_read, byte, 1)
		value = int.from_bytes(retVal[0:1], byteorder='little',signed=True)
		bits=bin(value)
		bits= bits.replace("0b","")
		if(len(bits)<8):
			for i in range(8 - len(bits)):
				bits="0"+bits
		bits=bits[::-1]
		return bits

	def getBit(self,byte,bit):
		bits = self.getSatusAllBitInByte(byte)
		try:
			status = bits[bit]
		except:
			status=0
		return status

	def changeBit(self,byte,bit):
		byte=int(byte)
		bit=int(bit)
		bitsSet = [1,2,4,8,16,32,64,128]
		bitsReset = [254, 253, 251, 247, 239, 223, 191, 127]
		retVal = self.client.db_read(self.db_write, byte, 1)
		value = int.from_bytes(retVal[0:1], byteorder='little')
		bits=bin(value)
		bits= bits.replace("0b","")
		if(len(bits)<8):
			for i in range(8 - len(bits)):
				bits="0"+bits
		bits=bits[::-1]
		try:
			status = bits[bit]
		except:
			status=0
		if(status!="0"):
			ret = value & bitsReset[bit]
		else:
			ret = value | bitsSet[bit]
		a = (ret).to_bytes(2, byteorder='little')
		self.client.db_write(self.db_write, byte, a)
		return ret

	def setBit(self,byte,bit):
		bitsSet = [1,2,4,8,16,32,64,128]
		retVal = self.client.db_read(self.db_write, byte, 1)
		value = int.from_bytes(retVal[0:1], byteorder='big')
		ret = value | bitsSet[bit]
		a = (ret).to_bytes(2, byteorder='little')
		self.client.db_write(self.db_write, byte, a)

	def resetBit(self, byte, bit):
		bitsReset = [254, 253, 251, 247, 239, 223, 191, 127]
		retVal = self.client.db_read(self.db_write, byte, 1)
		value = int.from_bytes(retVal[0:1], byteorder='big')
		ret = value & bitsReset[bit]
		a = (ret).to_bytes(2, byteorder='little')
		self.client.db_write(self.db_write, byte, a)

	def getdata(self,startDB,endDB):
		try:
			self.dataRead = self.client.db_read(self.db_read, startDB, endDB)
			return True
		except:
			return False

	def disassembleFloat(self,start,end):
		val = struct.unpack('>f', self.dataRead[start:end])
		return val[0]
	def disassembleDouble(self,start,end):
		val = struct.unpack('>d', self.dataRead[start:end])
		return val[0]
	def disassembleInt(self,start,end):
		return int.from_bytes(self.dataRead[start:end], "big")   




