from django.contrib import admin
from . models import Team
from django.utils.html import format_html

# Register your models here.
class Teamadmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius:50px"/>'.format(object.photo.url))
    thumbnail.short_description='photo' 
    
    
    list_display=('id','thumbnail','first_name','last_name','desgination','created_date')
    list_display_links=('id','thumbnail','first_name','last_name') 
    search_fields=('first_name','last_name','desgination')
    list_filter=('desgination',)
admin.site.register(Team,Teamadmin)
