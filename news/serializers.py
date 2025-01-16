from rest_framework import serializers

from .models import News


class NewsDetailSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = News
        fields = [
            'id', 
            'title', 
            'main_image', 
            'preview_image',
            'content', 
            'publication_date', 
            'author', 
            'author_username'
        ]
        
class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title', 
            'main_image', 
            'content', 
            'publication_date'
        ]