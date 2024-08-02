from django.contrib import admin
from .models import Category,Product,Size,Color,Image
# Register your models here.



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id','name','slug'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name','price','stock','created_at','updated_at'

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = 'name',
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = 'name',
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = 'product',



