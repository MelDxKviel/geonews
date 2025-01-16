from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import News
from .serializers import NewsDetailSerializer, NewsCreateSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-publication_date')
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return NewsCreateSerializer
        return NewsDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
