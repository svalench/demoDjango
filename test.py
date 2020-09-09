import json
import struct

import snap7

client = snap7.client.Client()  # формирование обращения к соединению
client.connect('192.168.1.80', 0,  2)
data = client.db_read(50,716,)

print(data)