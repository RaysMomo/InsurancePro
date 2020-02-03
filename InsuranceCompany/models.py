from django.db import models


class TransRange(models.Model):
    range_name = models.CharField(max_length=10, unique=True, verbose_name='运输范围')
    sort_code = models.IntegerField(verbose_name='显示排序')
    status = models.CharField(verbose_name='状态', max_length=10, choices=(('Active', '生效'),), blank=True)

    def __str__(self):
        return self.range_name

    class Meta:
        verbose_name = '运输范围'
        verbose_name_plural = '运输范围'


class TransType(models.Model):
    type_name = models.CharField(max_length=10, unique=True, verbose_name='运输方式')
    sort_code = models.IntegerField(verbose_name='显示排序')
    status = models.CharField(verbose_name='状态', max_length=10, choices=(('Active', '生效'),), blank=True)
    trans_range = models.ManyToManyField(TransRange, through='TransMap')

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = '运输方式'
        verbose_name_plural = '运输方式'


class TransMap(models.Model):
    trans_range = models.ForeignKey(TransRange, on_delete=models.CASCADE, verbose_name='运输范围')
    trans_type = models.ForeignKey(TransType, on_delete=models.CASCADE, verbose_name='运输方式')
    status = models.CharField(verbose_name='状态', max_length=10, choices=(('Active', '生效'),), blank=True)

    def __str__(self):
        return self.trans_type.__str__() + '-' + self.trans_range.__str__()

    class Meta:
        verbose_name = '运输范围与运输方式'
        verbose_name_plural = '运输范围与运输方式'
        unique_together = ('trans_range', 'trans_type',)


class InsuranceCompany(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='保险公司')
    contact = models.CharField(max_length=20, verbose_name='联系人')
    telephone = models.CharField(max_length=100, verbose_name='联系电话')
    email = models.EmailField(verbose_name='联系人邮箱')
    status = models.CharField(verbose_name='状态', max_length=10, choices=(('Active', '生效'),), blank=True)
    city = models.CharField(max_length=10, verbose_name='城市', blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = '保险公司'
        verbose_name_plural = '保险公司'


class InsuranceCompanyRate(models.Model):
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, verbose_name='保险公司')
    trans_map = models.ForeignKey(TransMap, on_delete=models.CASCADE, verbose_name='运输范围与方式')
    rate = models.DecimalField(verbose_name='费率', decimal_places=6, max_digits=10)

    def __str__(self):
        return self.insurance_company.__str__() + '-' + self.trans_map.__str__()

    class Meta:
        verbose_name = '保险公司费率'
        verbose_name_plural = '保险公司费率'


class InsuranceCompanyMinPrice(models.Model):
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.CASCADE, verbose_name='保险公司')
    trans_range = models.ForeignKey(TransRange, on_delete=models.CASCADE, verbose_name='运输范围')
    min_price = models.DecimalField(verbose_name='最低价', decimal_places=2, max_digits=4)

    def __str__(self):
        return self.insurance_company.__str__() + '-' + self.trans_range.__str__()

    class Meta:
        verbose_name = '保险公司最低价'
        verbose_name_plural = '保险公司最低价'


class InsurancePolicy(models.Model):
    insurance_name = models.CharField(max_length=20, verbose_name='险种简称')
    remark = models.CharField(max_length=255, verbose_name='备注', blank=True)
    insurance_text = models.CharField(max_length=500, verbose_name='险种内容')
    insurance_type = models.CharField(verbose_name='险种类别', choices=(('Main', '主险'), ('Additional', '附加险'),),
                                      max_length=10)
    status = models.CharField(verbose_name='状态', max_length=10, choices=(('Active', '生效'),), blank=True)

    def __str__(self):
        return self.insurance_name

    class Meta:
        verbose_name = '险种'
        verbose_name_plural = '险种'


class PolicyRules(models.Model):
    trans_map = models.ForeignKey(TransMap, on_delete=models.CASCADE, verbose_name='运输范围与方式')
    main_insurance = models.ForeignKey(InsurancePolicy, on_delete=models.CASCADE, verbose_name='主险',
                                       related_name='main_insurance')
    additional_insurance = models.ForeignKey(InsurancePolicy, on_delete=models.SET_NULL, verbose_name='附加险',
                                             related_name='additional_insurance', null=True)
    status = models.CharField(verbose_name='状态', max_length=10, choices=(('Active', '生效'),), blank=True)

    def __str__(self):
        return self.main_insurance.__str__() + '-' + self.trans_map.__str__()

    class Meta:
        verbose_name = '险种业务'
        verbose_name_plural = '险种业务'


# class CustomerInfo(models.Model):
#     pass
#
#
# class CountryMapsInsuranceCompany(models.Model):
#     pass


class InsuranceSlip(models.Model):
    insurance_code = models.CharField(max_length=20, verbose_name='序列号')
    customer_id = models.IntegerField(verbose_name='投保人')
    insured_object = models.CharField(max_length=128, verbose_name='被保险人')
    insured_adr = models.CharField(max_length=255, verbose_name='被保险人通讯地址', null=True)
    insured_contact = models.CharField(max_length=32, verbose_name='被保险人联系人', null=True)
    insured_postcode = models.CharField(max_length=16, verbose_name='被保险人邮编', null=True)
    insured_tel = models.CharField(max_length=32, verbose_name='被保险人联系电话', null=True)
    goods_type = models.CharField(max_length=100, verbose_name='货物大类')
    pack_type = models.CharField(max_length=50, verbose_name='包装方式')
    shipping_mark = models.CharField(max_length=1024, verbose_name='唛头')
    goods_name = models.CharField(max_length=1024, verbose_name='货物名称')
    pack_and_num = models.CharField(max_length=256, verbose_name='包装及数量')
    invoice = models.CharField(max_length=32, verbose_name='合同/发票号')
    land_bill_no = models.CharField(max_length=32, verbose_name='提单/运单号')
    train_no = models.CharField(max_length=32, verbose_name='船名/航次/车号')
    trans_type = models.ForeignKey(TransType, on_delete=models.SET_NULL, verbose_name='运输方式', null=True)
    port_from = models.CharField(max_length=64, verbose_name='起运地')
    port_to = models.CharField(max_length=64, verbose_name='目的地')
    port_transit = models.CharField(max_length=64, verbose_name='中转地')
    ship_date = models.DateField(verbose_name='起运日期')
    ship_date_print_format = models.CharField(max_length=20, verbose_name='起运日期打印格式')
    port_compensate = models.CharField(max_length=128, verbose_name='赔付地')
    special_goods_rate = models.DecimalField(verbose_name='特殊货物费率', decimal_places=6, max_digits=10)
    special_rate = models.DecimalField(verbose_name='特殊费率', decimal_places=6, max_digits=10)
    invoice_value = models.DecimalField(verbose_name='发票金额', decimal_places=2, max_digits=10)
    invoice_currency = models.CharField(max_length=20, verbose_name='发票金额币种')
    slip_ratio = models.DecimalField(verbose_name='保单系数', decimal_places=6, max_digits=10)
    slip_value = models.DecimalField(verbose_name='保单金额', decimal_places=2, max_digits=10)
    slip_currency = models.CharField(max_length=20, verbose_name='保单金额币种')
    is_credit_voucher = models.CharField(max_length=2, verbose_name='是否做信用凭证', choices=(('Y', '是'), ('N', '否')),
                                         default='N')
    main_insurance = models.ForeignKey(InsurancePolicy, on_delete=models.SET_NULL, null=True, verbose_name='主险',
                                       related_name='insurance_main_insurance')
    additional_insurance = models.ForeignKey(InsurancePolicy, on_delete=models.SET_NULL, null=True,
                                             verbose_name='附加险', related_name='insurance_additional_insurance')
    clause = models.TextField(verbose_name='条款内容')
    other_clause = models.TextField(verbose_name='其他约定条款')
    job_code = models.CharField(max_length=32, verbose_name='工作编号/操作人')
    remark = models.CharField(max_length=1024, verbose_name='备注')
    rate = models.DecimalField(verbose_name='费率', decimal_places=6, max_digits=10)
    premium = models.DecimalField(verbose_name='总保费', decimal_places=2, max_digits=10)
    policy_number = models.CharField(max_length=32, verbose_name='保险公司保单号')
    insure_date = models.DateField(verbose_name='投保日期')
    sign_date = models.DateField(verbose_name='签单日期')
    insurance_company_id = models.IntegerField(verbose_name='保险公司')
    issuing_company_id = models.IntegerField(verbose_name='出单公司')
    last_operator_id = models.IntegerField(verbose_name='最后操作人ID')
    last_operate_time = models.DateTimeField(verbose_name='最后操作时间', auto_now=True, null=True)  # 使用save时会自动更新
    status = models.CharField(max_length=20, verbose_name='保单状态')
    actual_premium = models.DecimalField(verbose_name='实际保费', decimal_places=2, max_digits=10)
    actual_rate = models.DecimalField(verbose_name='实际费率', decimal_places=6, max_digits=10)
    exchange = models.DecimalField(verbose_name='汇率', decimal_places=6, max_digits=10)
    salesman_id = models.IntegerField(verbose_name='销售人员')
    is_over_max = models.CharField(max_length=2, verbose_name='单件货物超过300万', choices=(('Y', '是'), ('N', '否')),
                                   default='N')
    is_special_packing = models.CharField(max_length=2, verbose_name='是否特殊包装', choices=(('Y', '是'), ('N', '否')),
                                          default='N')
    country_from = models.CharField(max_length=100, verbose_name='起运地国家')
    country_to = models.CharField(max_length=100, verbose_name='目的地国家')

    def __str__(self):
        return self.insurance_code

    class Meta:
        verbose_name = '保单'
        verbose_name_plural = '保单'
