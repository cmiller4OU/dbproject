from django.contrib import admin
from .models import Customers, Orders, Food

# Register your models here.

admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Food)

#register models here. next time in users and groups logging in you'll be able to see.