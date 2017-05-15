from django import forms
from django_summernote import fields as summer_fields
from .models import SummerNote


class PostForm(forms.ModelForm):
    class Meta:
        model = SummerNote
        fields = [ 'title', 'summer_field']
