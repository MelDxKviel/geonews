from django.contrib import admin

from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'main_image', 'content', 'author')
    list_display = ('title', 'publication_date', 'author')
