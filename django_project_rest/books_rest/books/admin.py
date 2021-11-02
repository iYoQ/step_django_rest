from django.contrib import admin
from .models import *


class StatDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'save_books', 'save_date', 'save_books_name')


admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Publishings)
admin.site.register(Review)
admin.site.register(Shop)
admin.site.register(StatData, StatDataAdmin)