from django.db import models
from django.utils.text import slugify

# UUID SlUG
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs) -> None:
        self.slug = slugify(self.name)
        return super(Category,self).save(*args, **kwargs)
    
    class Meta:
        
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


    
