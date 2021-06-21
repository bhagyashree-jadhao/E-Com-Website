from django.contrib import admin
from ecomweb.models import*
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
     list_display=['title']

     prepopulated_fields={'slug':('title',)}



admin.site.register(Product,ProductAdmin)
admin.site.register(Custemer)