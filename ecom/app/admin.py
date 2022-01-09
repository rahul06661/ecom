from django.contrib import admin
from .models import Customer,Product,Cart,Orderplaced


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Orderplaced)
# Register your models here.
