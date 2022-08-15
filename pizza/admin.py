from django.contrib import admin
from .models import customers
from .models import products,Post

# Register your models here.
admin.site.register(customers)
admin.site.register(products)
admin.site.register(Post)