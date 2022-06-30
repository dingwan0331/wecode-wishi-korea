from django.db import models

from core.models import TimeStampModel

class Category(models.Model):
    name      = models.CharField(max_length = 100)
    content   = models.CharField(max_length = 255, default = '')
    image_url = models.CharField(max_length = 255, default = '')

    class Meta:
        db_table = 'categories'

class SubCategory(models.Model):
    name      = models.CharField(max_length = 100)
    content   = models.CharField(max_length = 255, default = '')
    image_url = models.CharField(max_length = 255, default = '')
    category  = models.ForeignKey('Category', on_delete = models.CASCADE)

    class Meta:
        db_table = 'sub_categories'

class Product(TimeStampModel):
    name             = models.CharField(max_length = 100)
    is_new           = models.BooleanField(default = False)
    is_vegan         = models.BooleanField(default = False)
    is_only_online   = models.BooleanField(default = False)
    is_made_in_korea = models.BooleanField(default = False)
    content          = models.TextField(max_length = 2000, default = '')
    manual           = models.TextField(max_length = 2000, default = '')
    tag              = models.CharField(max_length = 200, default = '')
    sub_category     = models.ForeignKey('SubCategory', on_delete = models.SET_NULL, null = True)
    component        = models.ManyToManyField(
        'Component', 
        through = 'ProductComponent', 
        through_fields = ('product','component')
        )

    class Meta:
        db_table = 'products'

class ImageUrl(models.Model):
    url     = models.CharField(max_length = 255, default = '')
    product = models.ForeignKey('Product', on_delete = models.CASCADE)

    class Meta:
        db_table = 'image_urls'

class Component(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        db_table = 'components'

class ProductComponent(models.Model):
    product   = models.ForeignKey('Product', on_delete = models.CASCADE)
    component = models.ForeignKey('Component', on_delete = models.CASCADE)
    important = models.BooleanField(default = False)

    class Meta:
        db_table = 'product_component'

class Item(TimeStampModel):
    price     = models.DecimalField(max_digits = 9, decimal_places = 2, default = 0.00)
    stock     = models.IntegerField(default=0)
    image_url = models.CharField(max_length = 255, default = '')
    product   = models.ForeignKey('Product', on_delete = models.CASCADE)
    size      = models.ForeignKey('Size', on_delete = models.SET_NULL, null = True)

    class Meta:
        db_table = 'items'

class Size(models.Model):
    size_g = models.IntegerField()

    class Meta:
        db_table = 'sizes'