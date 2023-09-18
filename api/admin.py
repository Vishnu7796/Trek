from django.contrib import admin
from .models import TrekDetail, Photo

# Register your models here.
@admin.register(TrekDetail)
class TrekDetailsAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','imageFK','category','location']
    list_display_links = ['name','imageFK']


@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id','imageName','image']
    list_display_links = ['imageName']
