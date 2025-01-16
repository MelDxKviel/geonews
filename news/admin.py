from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import News

@admin.register(News)
class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    fields = ('title', 'main_image', 'content', 'author')
    search_fields = ('title', 'content', 'author__username')
    list_display = ('title', 'publication_date', 'author')
