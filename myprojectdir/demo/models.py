from django.db import models
from django.forms import ModelForm
# Create your models here.

class Association(models.Model):
	id = models.BigAutoField(primary_key=True)
	name = models.CharField(max_length=254)
	def __str__(self):
		return self.name

class Manufacture(models.Model):
	id = models.BigAutoField(primary_key=True)
	parent = models.ForeignKey('Association',on_delete=models.CASCADE)
	name = models.CharField(max_length=254)
	def __str__(self):
		return self.name

class Department(models.Model):
	id = models.BigAutoField(primary_key=True)
	parent = models.ForeignKey('Manufacture',on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Line(models.Model):
	id = models.BigAutoField(primary_key=True)
	parent = models.ForeignKey('Department',on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name


class Connections(models.Model):
	id = models.BigAutoField(primary_key=True)
	parent = models.ForeignKey('Line',on_delete=models.CASCADE)
	name = models.CharField('name connection',max_length=255)
	ip = models.CharField('ip connection plc',max_length=255)
	rack = models.IntegerField('rack connection plc')
	slot = models.IntegerField('slot connection plc')
	dbRead = models.IntegerField('db Read number plc',null=True)
	startRead = models.IntegerField('start Read address plc',null=True)
	endRead = models.IntegerField('end Read address +1 plc',null=True)
	dbWrite = models.IntegerField('db Write number plc',null=True)
	startWrite = models.IntegerField('start Write address plc',null=True)
	endWrite = models.IntegerField('end Write address +1 plc',null=True)

	whenAdd = models.DateTimeField(auto_now_add=True)

class Point(models.Model):
	SHIRT_SIZES = (
        ('real', 'Real type variable'),
        ('int', 'Int type variable'),
        ('dint', 'Double type variable'),
        ('bool', 'Boolean variable'),
        ('q', 'quit boolean variable'),
        ('i', 'input boolean variable'),
        ('m', 'Memory boolean variable'),
        ('oee', 'Data OEE'),
    )
	YAXIS_NAME = (
		('t', 'C&deg;'),
		('p', 'atm'),
		('ves', 'ves'),
		('v', 'm3 per hour'),
		('o', 'oee'),
    )
	YAXIS_UNIT = (
		('t', 'Co;'),
		('f', 'F'),
		('k', 'kg'),
		('m', 'm3 per hour'),
		('o', 'oee'),
		('mmrtst', 'mm.tr.st'),
		('s', 'kol-vo'),
		('ts', 't shtuk'),
		('P', 'Pa'),
    )
	id = models.BigAutoField(primary_key=True)
	parent = models.ForeignKey('Connections',on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	childModel =  models.CharField(max_length=50, choices=SHIRT_SIZES)
	yaxis =  models.CharField(max_length=10, choices=YAXIS_NAME)
	unit =  models.CharField(max_length=10, choices=YAXIS_UNIT)
	warning = models.FloatField('warning',null=True)
	alarm = models.FloatField('alarm',null=True)
	stop = models.FloatField('stop',null=True)
	startRead =  models.IntegerField('start  Read address plc (for bit  set number byte in plc)',null=True)
	endRead = models.IntegerField('end Read address +1 plc (for bit set bit number)',null=True)
	startWrite =  models.IntegerField('start  Write address plc ',null=True)
	endWrite = models.IntegerField('end Write address +1 plc',null=True)
	def __str__(self):
		return self.name


class Data(models.Model):
	parent = models.ForeignKey('Point',on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)
	value = models.FloatField(null=True)


class DataBoolean(models.Model):
	parent = models.ForeignKey('Point',on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)
	value = models.BooleanField(null=True)

class DataOEE(models.Model):
	parent = models.ForeignKey('Connections',on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)
	datetimeStart = models.DateTimeField(default=None, blank=True)
	value = models.IntegerField(null=True)
	name = models.IntegerField(null=True, default=0)










#forms

class AssociationForm(ModelForm):
    class Meta:
        model = Association
        fields = ['name']

class ManufactureForm(ModelForm):
    class Meta:
        model = Manufacture
        fields = ['name', 'parent']

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'parent']

class LineForm(ModelForm):
    class Meta:
        model = Line
        fields = ['name', 'parent']

class ConnectionsForm(ModelForm):
    class Meta:
        model = Connections
        fields = ['name', 'ip','rack','slot','dbRead',
        		'startRead','endRead','dbWrite','startWrite','endWrite', 'parent']


class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = ['name', 'childModel','yaxis','unit','warning','alarm','stop',
        		'startRead','endRead','startWrite','endWrite', 'parent']

