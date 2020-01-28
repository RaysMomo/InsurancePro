from django.db import models
from multiselectfield import MultiSelectField


class TransRange(models.Model):
    status_choices = (('Active', u'生效'),)
    range_name = models.CharField(max_length=10, unique=True, verbose_name='运输范围')
    sort_code = models.IntegerField(verbose_name='显示排序')
    status = MultiSelectField(u'状态', choices=status_choices, blank=True)

    def __str__(self):
        return self.range_name

    class Meta:
        verbose_name = '运输范围'
        verbose_name_plural = '运输范围'


class TransType(models.Model):
    status_choices = (('Active', u'生效'),)
    type_name = models.CharField(max_length=10, unique=True, verbose_name='运输方式')
    sort_code = models.IntegerField(verbose_name='显示排序')
    status = MultiSelectField(u'状态', choices=status_choices, blank=True)
    trans_range = models.ManyToManyField(TransRange, through='TransMap')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '运输方式'
        verbose_name_plural = '运输方式'


class TransMap(models.Model):
    status_choices = (('Active', u'生效'),)
    trans_range = models.ForeignKey(TransRange, on_delete=models.CASCADE, verbose_name='运输范围')
    trans_type = models.ForeignKey(TransType, on_delete=models.CASCADE, verbose_name='运输方式')
    status = MultiSelectField(u'状态', choices=status_choices, blank=True)

    def __str__(self):
        return self.trans_type.__str__() + '-' + self.trans_range.__str__()

    class Meta:
        verbose_name = '运输范围与运输方式'
        verbose_name_plural = '运输范围与运输方式'
        unique_together = ('trans_range', 'trans_type',)


class InsuranceCompany(models.Model):
    status_choices = (('Active', u'生效'),)
    company_name = models.CharField(max_length=100, unique=True, verbose_name='保险公司')
    contact = models.CharField(max_length=20, verbose_name='联系人')
    telephone = models.CharField(max_length=100, verbose_name='联系电话')
    email = models.EmailField(verbose_name='联系人邮箱')
    status = MultiSelectField(u'状态', choices=status_choices, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '保险公司'
        verbose_name_plural = '保险公司'


class InsuranceCompanyRate(models.Model):
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, verbose_name='保险公司')
    trans_map = models.ForeignKey(TransMap, on_delete=models.CASCADE, verbose_name='运输范围与方式')
    rate = models.DecimalField(verbose_name='费率', decimal_places=6, max_digits=7)

    def __str__(self):
        return self.insurance_company.__str__() + '-' + self.trans_map.__str__()

    class Meta:
        verbose_name = '保险公司费率'
        verbose_name_plural = '保险公司费率'


