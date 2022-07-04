from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    img = models.ImageField(upload_to='Job/%Y/%m/%d', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата')
    price = models.PositiveIntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class MyHistory(models.Model):
    description = models.TextField(verbose_name='История')
    img = models.ImageField(upload_to='History/%Y/%m/%d', verbose_name='Фото')
    date = models.DateTimeField(verbose_name='Дата', help_text='2000-2005')
    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return f'{self.date}'

    class Meta:
        verbose_name = 'Истоия'
        verbose_name_plural = 'Истории'


class Email(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    email = models.EmailField(verbose_name='Aдрес электронной почты')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return f'{self.email}'
