from home.views import cart
from django.contrib import admin

from . models import Services,category, cart, Contact
# Register your models here.
admin.site.register(category)
admin.site.register(Services)
admin.site.register(cart)
admin.site.register(Contact)
