import os

from PIL import Image

from django.db import models
from django.contrib.auth.models import User

from django_summernote.fields import SummernoteTextField


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    main_image = models.ImageField(upload_to='news/images/', verbose_name='Изображение')
    preview_image = models.ImageField(upload_to='news/previews/', verbose_name='Превью')
    content = SummernoteTextField(verbose_name='Текст новости')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='news')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.main_image:
            img = Image.open(self.main_image.path)
            img.thumbnail((200, 200))
            
            preview_dir = os.path.join(
            os.path.dirname(self.main_image.path).replace("images", "previews"))
            preview_path = os.path.join(preview_dir, os.path.basename(self.main_image.path))
            
            img.save(preview_path)
            
            
            self.preview_image.name = os.path.relpath(
                preview_path,
                self.main_image.storage.location
            )
            super().save(update_fields=['preview_image'])
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
