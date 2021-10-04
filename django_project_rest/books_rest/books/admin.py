from django.contrib import admin
from .models import *

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Publishings)
admin.site.register(Review)
admin.site.register(Shop)