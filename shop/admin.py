from django.contrib import admin
from .models import Product,Catalog,Subcatalog, Real


admin.site.register(Catalog)
admin.site.register(Subcatalog)
admin.site.register(Real)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','price','get_image_preview','get_catalog', 'get_subcatalog')
    list_display_links = ('id',)
    list_filter = ('real__catalog', )
    list_editable = ('name',)
