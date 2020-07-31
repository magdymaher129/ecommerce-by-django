from django.contrib import admin
from .models import Item,Order,OrderItem
# Register your models here.
class ItemAdmen(admin.ModelAdmin):
    list_display=['title','price','avaliable']
    list_filter=('title',)
    list_editable=['avaliable']

admin.site.register(Item,ItemAdmen)
admin.site.register(Order)
admin.site.register(OrderItem)