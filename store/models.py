from django.db import models
from django.utils.text import slugify

# UUID SlUG
# Create your models here.

def upload_image(instance,file_name:str):
    extension = file_name.split('.')[1] 
    return f'category/{instance.name}.{extension}'

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(upload_to=upload_image, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super(Category,self).save(*args, **kwargs)
    
    class Meta:
        
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Size(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=150)  

    def __str__(self):
        return self.name  




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField( max_length=250)
    slug = models.SlugField(blank=True,null=True)
    price = models.FloatField()
    discription = models.TextField()
    size = models.ManyToManyField(Size,blank=True,null=True)
    color = models.ManyToManyField(Color, blank=True,null=True)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save(*args, **kwargs)
    


def image_upload(instance,file_Name:str):
    extension = file_Name.split('.')[1]
    return f'Products/{instance.product.name}.{extension}'

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.product.name
    
    
## One to One ------> User --> Profile
## Many to One ------> Category to Product
## Many to Many -----> Youtube video <------> person
