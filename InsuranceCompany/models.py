from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
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
