from rest_framework import viewsets
from .models import Association
from .serializers import ArticleSerializer
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Association.objects.all()
    serializer_class = ArticleSerializer