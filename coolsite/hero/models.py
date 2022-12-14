from django.db import models
from django.urls import reverse

class Cat(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name='Описание')
    stats = models.TextField(blank=True, verbose_name='Статы')
    photo = models.ImageField(upload_to="photos/cats/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    coll = models.ForeignKey('Collection', on_delete = models.PROTECT, null = True, verbose_name='Коллекция', related_name='get_cats')

    class Meta:
        verbose_name = 'Коты'
        verbose_name_plural = 'Коты'
        ordering = ['coll', 'time_create']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs = {'catname': self.slug})



class Collection(models.Model):
    name = models.CharField(max_length=255, db_index = True, verbose_name="Коллекция")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/")

    class Meta:
        verbose_name = 'Коллекции'
        verbose_name_plural = 'Коллекции'
        ordering = ["id"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print(self.name)
        return reverse('coll', kwargs = {'collname': self.slug})
