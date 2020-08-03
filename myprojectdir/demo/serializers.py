from rest_framework import serializers
from .models import Association


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = '__all__'