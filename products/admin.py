from django.contrib import admin
from  .models  import Product,ProductImages,ProductReview,Brand,Category


class ProductImageTabular(admin.TabularInline):
    model = ProductImages
    

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name','flag','quantity','price']
    list_filter = ['flag','brand','category','price']
    search_fields = ['name','desc','subtitle']


# Register your models here.
admin.site.register(ProductReview)
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImages)
