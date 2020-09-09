"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from demo import urls
from demo.views import *
from .routers import router
from django.views.generic import TemplateView
urlpatterns = [
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('df/', TemplateView.as_view(template_name='fan/index.html')),
    path('admin/', admin.site.urls),
    path('',index,name='start'),
    # url for manufacure
    path('association/',AssociationView.list,name='association'),
    path('association/add/',AssociationView.addView,name='associationAdd'),
    path('association/get/add',AssociationView.add,name='associationGetAdd'),
    path('association/get/<int:id>/delete',AssociationView.delete,name='associationGetDelete'),
    # url for manufacure
    path('manufacture/',ManufactureView.list,name='manufacture'),
    path('manufacture/add/',ManufactureView.addView,name='manufactureAdd'),
    path('manufacture/get/add',ManufactureView.add,name='manGetAdd'),
    path('manufacture/get/<int:id>/delete',ManufactureView.delete,name='manGetDelete'),
    # url for department
    path('department/',DepartmentView.list,name='department'),
    path('department/add/',DepartmentView.addView,name='departmentAdd'),
    path('department/get/add',DepartmentView.add,name='departmentGetAdd'),
    path('department/get/<int:id>/delete',DepartmentView.delete,name='departmentGetDelete'),
    # url for Line
    path('line/',LineView.list,name='line'),
    path('line/add/',LineView.addView,name='lineAdd'),
    path('line/get/add',LineView.add,name='lineGetAdd'),
    path('line/get/<int:id>/delete',LineView.delete,name='lineGetDelete'),
    # url for connections
    path('connections/',ConnectionsView.list,name='connections'),
    path('connections/add/',ConnectionsView.addView,name='connectionsAdd'),
    path('connections/get/add',ConnectionsView.add,name='connectionsGetAdd'),
    path('connections/get/<int:id>/delete',ConnectionsView.delete,name='connectionsGetDelete'),
    # url for point
    path('point/',PointView.list,name='point'),
    path('point/add/',PointView.addView,name='pointAdd'),
    path('point/get/add',PointView.add,name='pointGetAdd'),
    path('point/get/<int:id>/delete',PointView.delete,name='pointGetDelete'),

    #url for view data in graph on line ordering
    path('graph/view/list/all',GraphView.list,name='graphListAll'),
    path('graph/view/<int:id>/all',GraphView.viewGraph,name='graphAll'),
    path('graph/update/value/granica',GraphView.updateZone,name='updateGranica'),







    path('api/Lines/<int:id>/get/', LineViewAPI.as_view()),
    path('api/GrapLine/<int:id>/get/', LineViewAPI.viewGraph),
]
