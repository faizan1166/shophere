from django.contrib import admin
from .models import product
from .models import Contact
from .models import Buy

# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Buy)


