from django.contrib import admin
from .models import User, Executive, Customer

# Register your models here.
admin.site.register(User)
admin.site.register(Executive)
admin.site.register(Customer)