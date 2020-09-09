from rest_framework import routers
from demo.viewsets import *
from django.urls import path


router = routers.DefaultRouter()
router.register(r'Association', AssociationViewSet)
router.register(r'Manufacture', ManufactureViewSet)
router.register(r'Department', DepartmentViewSet)


router.register(r'Line', LineViewSet)


