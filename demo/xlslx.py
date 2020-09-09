from openpyxl import Workbook
import datetime


class XLSLX:
	__init__(self):
    	self.response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    def report(self,name,DATA):
    	wb = Workbook()
    	ws = wb.active
    	self.response['Content-Disposition'] = 'attachment; filename='+"_act__" + name + '.xlsx'
