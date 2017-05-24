from django.conf import settings
from django.db import models


class Info(models.Model):
	event_name = models.CharField('행사명', max_length=100)
	event_date = models.DateTimeField('행사일시')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='작성자')
	category_set = models.ManyToManyField('Category', '분야')
	fee = models.CharField('참가비', max_length=10, choices = (
		('free', '무료'),
		('paid', '유료'),
		))
	location = models.CharField('행사장소', max_length=200)
	link = models.URLField('링크', blank=True)
	description = models.TextField('행사내용')
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.event_name

class Category(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name
