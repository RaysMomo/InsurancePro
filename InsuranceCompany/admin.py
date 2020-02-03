# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import TransRange, TransType, TransMap
from .models import InsuranceCompany, InsuranceCompanyRate, InsuranceCompanyMinPrice
from .models import InsurancePolicy, PolicyRules


# Register your models here.

@admin.register(TransRange)
class TransRangeAdmin(admin.ModelAdmin):
    list_display = ['range_name', 'sort_code', 'status']
    list_filter = ['status', ]


@admin.register(TransType)
class TransTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'sort_code', 'status']


@admin.register(TransMap)
class TransMapAdmin(admin.ModelAdmin):
    list_display = ['trans_range', 'trans_type', 'status']
    list_filter = ('trans_range', )


@admin.register(InsuranceCompany)
class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'contact', 'telephone', 'email', 'status']
    list_filter = ['status']


@admin.register(InsuranceCompanyRate)
class InsuranceCompanyRateAdmin(admin.ModelAdmin):
    list_display = ['insurance_company', 'trans_map', 'rate']


@admin.register(InsuranceCompanyMinPrice)
class InsuranceCompanyMinPriceAdmin(admin.ModelAdmin):
    list_display = ['insurance_company', 'trans_range', 'min_price']


@admin.register(InsurancePolicy)
class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ['insurance_name', 'insurance_text', 'insurance_type', 'remark', 'status']
    # radio_fields = {'insurance_type': admin.VERTICAL}
    list_filter = ('insurance_type', 'status', )
    list_per_page = 10


@admin.register(PolicyRules)
class PolicyRulesAdmin(admin.ModelAdmin):
    list_display = ['trans_map', 'main_insurance', 'additional_insurance', 'status']
    list_filter = ('trans_map', 'status', )
    list_per_page = 10


admin.site.site_title = "某宝后台管理"
admin.site.site_header = "某宝后台管理"
