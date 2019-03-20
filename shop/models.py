from django.db import models
from django.utils.safestring import mark_safe



class Catalog(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Subcatalog(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Real(models.Model):
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    subcatalog = models.ForeignKey('Subcatalog', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.catalog}_{self.subcatalog}"

    class Meta:
        unique_together = ('catalog','subcatalog')

def save_image(instance, filename):
    return '/'.join(['shop',instance.real__catalog,instance.real__subcatalog,filename])

class Product(models.Model):
    real = models.ForeignKey('Real', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True)
    price = models.IntegerField(blank=True, default=-10)
    short_description = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True )
    image = models.ImageField(upload_to=save_image, default='default.jpg')

    def __str__(self):
        return self.name
    def get_catalog(self):
        return self.real.catalog
    def get_subcatalog(self):
        return self.real.subcatalog
    def get_image_preview(self):
        return mark_safe(f"<img src={self.image.url} width=50 height=50>")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
