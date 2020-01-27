from django.contrib import admin
from .models import TransRange


# Register your models here.


class TransRangeAdmin(admin.ModelAdmin):
    list_display = ['range_name', 'sort_code', 'status']


admin.site.register(TransRange, TransRangeAdmin)
