from django.contrib import admin
from .models import TransRange, TransType, TransMap


# Register your models here.


class TransRangeAdmin(admin.ModelAdmin):
    list_display = ['range_name', 'sort_code', 'status']


class TransTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'sort_code', 'status']


class TransMapAdmin(admin.ModelAdmin):
    list_display = ['trans_range', 'trans_type', 'status', ]
    list_display_links = ['trans_range', 'trans_type']


admin.site.register(TransRange, TransRangeAdmin)
admin.site.register(TransType, TransTypeAdmin)
admin.site.register(TransMap, TransMapAdmin)
