from django.contrib import admin
from .models import Info, Category

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
	list_display = ['event_name', 'event_date','author', 'fee']
	list_display_links = ['event_name']

admin.site.register(Category)
