from django.contrib import admin
from .models import Stream

# Register your models here.


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'link']
    list_display_links = ['title', 'description', 'link']
