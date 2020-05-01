from django.db import models
from .validators import validate_file_extension



class Post(models.Model):

    name = models.CharField("Название",max_length=128)
    text = models.TextField("Текст",max_length=1280)
    created = models.DateTimeField("Создан", auto_now_add=True, auto_now=False)
    image = models.FileField(upload_to='images/', validators=[validate_file_extension])

    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
