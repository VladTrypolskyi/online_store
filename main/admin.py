from django.contrib import admin

# Register your models here.

from .models import *


# admin.site.register(Role)
# admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Basket)
admin.site.register(Category)
# admin.site.register(ProductCategory)
admin.site.register(ProductBasket)
admin.site.register(ProductWishlist)
admin.site.register(Order)