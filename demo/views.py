from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.shortcuts import render,redirect
from demo.models import *
from django.core import serializers
import json
import datetime
import math
import time
from django.db.models import F,Value
import threading
from demo.snap7_plc import *
import asyncio
import websockets
from django.contrib.auth.decorators import login_required
#from .serializers import *
from rest_framework.response import Response

# Create your views here.

def index(request):
	context = {
	            'title': 'sdfsdf',
	          }
	return render(request, 'demo/index.html', context)


class ReportView:
	@login_required
	def getReport(request):
		pass


#__________________________________________Association__________________________________________________________________
# class for work with pages association

class AssociationView:
	@login_required
	def list(request):
		try:
			association = Association.objects.all()
		except:
			association = []

		context = {
	            'association': association,
	          }
		return render(request, 'association/list.html', context)
	@login_required
	def addView(request):
		form = AssociationForm()
		context = {'form':form}
		return render(request, 'association/add.html', context)
	@login_required
	def add(request):
		form1 = AssociationForm(request.POST)
		form1.save()
		return redirect("/association")
	@login_required	
	def delete(request,id):
		Point.objects.filter(id=id).delete()
		return redirect("/association")
#____________________________________________________________________________________________________________



#____________________________________ManufactureView________________________________________________________________________
# class for work woth pages Manufacture

class ManufactureView:
	@login_required
	def list(request):
		try:
			man = Manufacture.objects.all()
		except:
			man = []
		context = {
	            'zavod': man,
	          }

		return render(request, 'man/lists.html', context)
	@login_required
	def addView(request):
		form = ManufactureForm()
		context = {'form':form}
		return render(request, 'man/add.html', context)
	@login_required
	def add(request):
		form1 = ManufactureForm(request.POST)
		form1.save()
		return redirect("/manufacture")
	@login_required
	def delete(request,id):
		Manufacture.objects.filter(id=id).delete()
		return redirect("/manufacture")
#____________________________________________________________________________________________________________


#_________________________________________Department___________________________________________________________________
# class for work with pages Department

class DepartmentView:
	@login_required
	def list(request):
		try:
			department = Department.objects.all()
		except:
			department = []

		context = {
	            'department': department,
	          }
		return render(request, 'department/list.html', context)
	@login_required
	def addView(request):
		form = DepartmentForm()
		context = {'form':form}
		return render(request, 'department/add.html', context)
	@login_required
	def add(request):
		form1 = DepartmentForm(request.POST)
		form1.save()
		return redirect("/department")
	@login_required
	def delete(request,id):
		Point.objects.filter(id=id).delete()
		return redirect("/department")
#____________________________________________________________________________________________________________




#_____________________________________________________Line_______________________________________________________
# class for work with pages line

class LineView:
	@login_required
	def list(request):
		try:
			line = Line.objects.all()
		except:
			line = []
		context = {
	            'line': line,
	          }
		return render(request, 'line/list.html', context)
	@login_required
	def addView(request):
		form = LineForm()
		context = {'form':form}
		return render(request, 'line/add.html', context)
	@login_required
	def add(request):
		form1 = LineForm(request.POST)
		form1.save()
		return redirect("/line")
	@login_required
	def delete(request,id):
		Line.objects.filter(id=id).delete()
		return redirect("/line")
#____________________________________________________________________________________________________________


#____________________________________________________________________________________________________________
# class for work with pages connections

class ConnectionsView:
	@login_required
	def list(request):
		try:
			connections = Connections.objects.all()
		except:
			connections = []

		context = {
	            'connections': connections,
	          }
		return render(request, 'connections/list.html', context)
	@login_required
	def addView(request):
		form = ConnectionsForm()
		context = {'form':form}
		return render(request, 'connections/add.html', context)
	@login_required
	def add(request):
		form1 = ConnectionsForm(request.POST)
		form1.save()
		return redirect("/connections")
	@login_required
	def delete(request,id):
		Connections.objects.filter(id=id).delete()
		return redirect("/connections")
#____________________________________________________________________________________________________________




#____________________________________________________________________________________________________________
# class for work with pages points

class PointView:
	@login_required
	def list(request):
		try:
			point = Connections.objects.all()
		except:
			point = []

		context = {
	            'point': point,
	          }
		return render(request, 'point/list.html', context)
	@login_required
	def addView(request):
		form = PointForm()
		context = {'form':form}
		return render(request, 'point/add.html', context)
	@login_required
	def add(request):
		form1 = PointForm(request.POST)
		form1.save()
		return redirect("/point")
	@login_required
	def delete(request,id):
		Point.objects.filter(id=id).delete()
		return redirect("/point")
#____________________________________________________________________________________________________________


#____________________________________________________________________________________________________________
# class for view grafiks

class GraphView:
	@login_required
	def list(request):
		try:
			line = Line.objects.all()
		except:
			line = []

		context = {
	            'point': line,
	          }
		e = Data(value=12,parent_id=24)
		e.save()
		return render(request, 'demo/graphList.html', context)
	@login_required
	def viewGraph(request,id):
		line = Line.objects.filter(id=id)
		#asd = DataOEE(value=1,parent_id=7,datetimeStart="2020-07-29 12:27:27.536844+00")
		#asd.save()
		points = line[0].connections_set.all()
		res = {"chart":[],"chartD":[]}
		for j in points:
			for i in j.point_set.all():
				a = {}
				a['name'] = i.name
				if i.childModel=="real" or i.childModel=="int" :
					a['unit'] = i.unit
					a['yAxisName'] = i.yaxis
					a['stopSet'] = i.stop
					a['alarmSet'] = i.alarm
					a['warningSet'] = i.warning
					a['arrDataChart'] = list(i.data_set.annotate(x=F('datetime'),y=F('value')).order_by("x").values('x','y'))
					res['chart'].append(a)	
				if  i.childModel=="bool":
					a['unit'] = i.unit
					a['yAxisName'] = i.yaxis
					a['stopSet'] = i.stop
					a['alarmSet'] = i.alarm
					a['warningSet'] = i.warning
					a['arrDataChart'] = list(i.databoolean_set.annotate(x=F('datetime'),y=F('value')).order_by("x").values('x','y'))
					res['chart'].append(a)	
				if i.childModel=="oee":
					a['unit'] = i.unit
					print(dir(i.dataoee_set.filter(value=0).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('value')).order_by("x").values('x','x2','y')))
					obj = {"name":"VYKLUCHEN",'data':list(i.dataoee_set.filter(value=0).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
					obj1 = {"name":"RABOTA",'data':list(i.dataoee_set.filter(value=1).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
					obj2 = {"name":"PROSTOI",'data':list(i.dataoee_set.filter(value=2).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
					obj3 = {"name":"AVARIA",'data':list(i.dataoee_set.filter(value=3).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
					a['strData'] = [obj1,obj3,obj,obj2]
					res['chartD'].append(a)		
		dataLine = serializers.serialize('json', line)
		dataPoint = json.dumps(res,default=datetimeconverter)
		context = {'line': line,'dataLine':dataLine,'dataPoint':dataPoint}
		return render(request, 'demo/grafic.html', context)
	@login_required
	def updateZone(request):
		post  = request.POST
		point = Point.objects.filter(id=post['id'])
		if(post['type']=='warning'):
			point.update(warning=post['value'])
		elif(post['type']=='alarm'):
			point.update(alarm=post['value'])
		elif(post['type']=='stop'):
			point.update(stop=post['value'])
		else:
			pass
		point.save()
		return JsonResponse({'answer':'good response'})




def opros(data,points,count):
	try:
		plc1 = PlcRemoteUse(data['ip'],data['rack'],data['slot'])
		plc1.db_read = data['dbRead']
		started = True
	except:
		started = False
	if(started):
		while plc1.getdata(data['startRead'],data['endRead']):
			for j in points:
				if(j['childModel']=='real'):
					try:
						val = plc1.disassembleFloat(j['startRead'],j['endRead'])
						u = Data(value=val,parent_id=j['id'])
						u.save()
					except:
						print("error FLOAT!!")
				elif(j['childModel']=='int'):
					try:
						val = plc1.disassembleInt(j['startRead'],j['endRead'])
						val = val/1.0
						u = Data(value=val,parent_id=j['id'])
						u.save()
					except:
						print("error INT!!")
				elif(j['childModel']=='bool'):
					try:
						u = DataBoolean(value=plc1.getBit(j['startRead'],j['endRead']),parent_id=j['id'])
						u.save()
					except:
						print("error Bool!!")
				elif(j['childModel']=='q'):

					try:
						print(plc1.getOut(j['startRead'],j['endRead']))
						#u = DataBoolean(value=plc1.getBit(j['startRead'],j['endRead']),parent_id=j['id'])
						#u.save()
					except:
						print("error quite!!")
			print("data returned")
			time.sleep(10)
		if(not plc1.getdata(data['startRead'],data['endRead'])):
			print('data will be not returned')
			main(count)
			return False
	else:
		time.sleep(30)
		main(count)
		return False
		


def main(plc="all"):
	connections = Connections.objects.all()
	connection = []
	count = 0

	for i in connections:
		a = {'data':{	'name':i.name,
						'ip':i.ip,
						"rack":i.rack,
						"slot":i.slot,
						'dbRead':i.dbRead,
						"startRead":i.startRead,
						"endRead":i.endRead,
						'dbWrite':i.dbWrite
					},
			'points':i.point_set.all().values(),'count':count}
		connection.append(a)
		count+=1
	if(plc=="all"):
		for i in connection:
			threading.Thread(target=opros,args=[i['data'],i['points'],i['count']]).start()
			print('Hi! started function  - '+i['data']['name'])
	else:
		threading.Thread(target=opros,args=[connection[plc]['data'],connection[plc]['points'],plc]).start()
		print('Hi! started function  - '+connection[plc]['data']['name'])

main()




# preobrazovanie datetimestamp v unix time
def datetimeconverter(o):
    if isinstance(o, datetime.datetime):
        return math.ceil(o.timestamp()*1000)








from rest_framework.views import APIView


class LineViewAPI(APIView):
    def get(self, request,id):
        line = Line.objects.filter(parent_id=id)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = LineSerializer(line, many=True)
        return Response({"articles": serializer.data})

    def viewGraph(request,id):
        line = Line.objects.filter(id=id)
        points = line[0].connections_set.all()
        res = {"chart":[],"chartD":[]}
        for j in points:
            for i in j.point_set.all():
                a = {}
                a['name'] = i.name
                if i.childModel=="real" or i.childModel=="int" :
                    a['unit'] = i.unit
                    a['yAxisName'] = i.yaxis
                    a['stopSet'] = i.stop
                    a['alarmSet'] = i.alarm
                    a['warningSet'] = i.warning
                    a['arrDataChart'] = list(i.data_set.annotate(x=F('datetime'),y=F('value')).order_by("x").values('x','y'))
                    res['chart'].append(a)	
                if  i.childModel=="bool":
                    a['unit'] = i.unit
                    a['yAxisName'] = i.yaxis
                    a['stopSet'] = i.stop
                    a['alarmSet'] = i.alarm
                    a['warningSet'] = i.warning
                    a['arrDataChart'] = list(i.databoolean_set.annotate(x=F('datetime'),y=F('value')).order_by("x").values('x','y'))
                    res['chart'].append(a)	
                if i.childModel=="oee":
                    a['unit'] = i.unit
                    obj = {"name":"VYKLUCHEN",'data':list(i.dataoee_set.filter(value=0).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
                    obj1 = {"name":"RABOTA",'data':list(i.dataoee_set.filter(value=1).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
                    obj2 = {"name":"PROSTOI",'data':list(i.dataoee_set.filter(value=2).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
                    obj3 = {"name":"AVARIA",'data':list(i.dataoee_set.filter(value=3).annotate(x=F('datetimeStart'),x2=F('datetime'),y=F('name')).order_by("x").values('x','x2','y'))}
                    a['strData'] = [obj1,obj3,obj,obj2]
                    res['chartD'].append(a)		
        #dataLine = serializers.serialize('json', line)
        dataPoint = json.dumps(res,default=datetimeconverter)
        context = {'dataPoint':dataPoint}
        json_context = json.dumps(context,default=datetimeconverter)
        return Response({"data": json_context})
