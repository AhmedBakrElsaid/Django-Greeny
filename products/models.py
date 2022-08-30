from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
FLAG_OPTION = (
    ("new","new"),
    ("feature","feature"),
    ("sale","sale"),
)
class Product (models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"))
    subtitle = models.CharField(_("subtitle"),max_length=500)
    sku = models.IntegerField(_("SKU"))
    desc = models.TextField(_("Description"),max_length=10000)
    price = models.FloatField(_("price"))
    flag = models.CharField(_("Flag"),max_length=10,choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity"))
    brand = ''
    category = ''
    


class ProductImages (models.Model):
    pass



class Brand (models.Model):
    pass



class Category (models.Model):
    pass




class ProductReview (models.Model):
    pass

