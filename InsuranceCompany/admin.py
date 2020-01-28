from django.contrib import admin
from .models import TransRange, TransType, TransMap
from .models import InsuranceCompany, InsuranceCompanyRate


# Register your models here.


class TransRangeAdmin(admin.ModelAdmin):
    list_display = ['range_name', 'sort_code', 'status']


class TransTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'sort_code', 'status']


class TransMapAdmin(admin.ModelAdmin):
    list_display = ['trans_range', 'trans_type', 'status', ]
    list_display_links = ['trans_range', 'trans_type']


class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact', 'telephone', 'email']


class InsuranceCompanyRateAdmin(admin.ModelAdmin):
    list_display = ['insurance_company', 'trans_map', 'rate']
    list_display_links = ['insurance_company', 'trans_map']


admin.site.register(TransRange, TransRangeAdmin)
admin.site.register(TransType, TransTypeAdmin)
admin.site.register(TransMap, TransMapAdmin)
admin.site.register(InsuranceCompany, InsuranceCompanyAdmin)
admin.site.register(InsuranceCompanyRate, InsuranceCompanyRateAdmin)

admin.site.site_title = "某宝后台管理"
admin.site.site_header = "某宝后台管理"
