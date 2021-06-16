from django.contrib import admin
from .models import Pizzeria
from .models import Image

admin.site.register(Image)
admin.site.register(Pizzeria)