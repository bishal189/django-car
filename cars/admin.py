from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import Car
class caradmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.car_photo.url))
    thumbnail.short_description='car_photo' 
    
    list_display=('id','car_title','thumbnail','color','model','year','fuel_type','city','is_featured')
    list_display_links=('car_title','id','thumbnail')
    list_editable=('is_featured',)
    search_fields=('id','city','model','fuel_type')
    list_filter=('city','model','fuel_type')
admin.site.register(Car,caradmin)
