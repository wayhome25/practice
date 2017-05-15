from django.core.urlresolvers import reverse
from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields

class SummerNote(summer_model.Attachment):
	title = models.CharField(max_length=100, verbose_name='제목')
	summer_field = summer_fields.SummernoteTextField(default='')

	def get_absolute_url(self):
		return reverse('board:post_detail', args=[self.id])

	def __str__(self):
		return self.title
