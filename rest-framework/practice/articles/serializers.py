from rest_framework import serializers
from .models import Article

class AriticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
        
        
class AriticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'