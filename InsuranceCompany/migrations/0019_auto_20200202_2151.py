# Generated by Django 3.0.2 on 2020-02-02 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InsuranceCompany', '0018_auto_20200201_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompanyrate',
            name='rate',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='费率'),
        ),
        migrations.CreateModel(
            name='InsuranceSlip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_code', models.CharField(max_length=20, verbose_name='序列号')),
                ('customer_id', models.IntegerField(verbose_name='投保人')),
                ('insured_object', models.CharField(max_length=128, verbose_name='被保险人')),
                ('insured_adr', models.CharField(max_length=255, null=True, verbose_name='被保险人通讯地址')),
                ('insured_contact', models.CharField(max_length=32, null=True, verbose_name='被保险人联系人')),
                ('insured_postcode', models.CharField(max_length=16, null=True, verbose_name='被保险人邮编')),
                ('insured_tel', models.CharField(max_length=32, null=True, verbose_name='被保险人联系电话')),
                ('goods_type', models.CharField(max_length=100, verbose_name='货物大类')),
                ('pack_type', models.CharField(max_length=50, verbose_name='包装方式')),
                ('shipping_mark', models.CharField(max_length=1024, verbose_name='唛头')),
                ('goods_name', models.CharField(max_length=1024, verbose_name='货物名称')),
                ('pack_and_num', models.CharField(max_length=256, verbose_name='包装及数量')),
                ('invoice', models.CharField(max_length=32, verbose_name='合同/发票号')),
                ('land_bill_no', models.CharField(max_length=32, verbose_name='提单/运单号')),
                ('train_no', models.CharField(max_length=32, verbose_name='船名/航次/车号')),
                ('port_from', models.CharField(max_length=64, verbose_name='起运地')),
                ('port_to', models.CharField(max_length=64, verbose_name='目的地')),
                ('port_transit', models.CharField(max_length=64, verbose_name='中转地')),
                ('ship_date', models.DateField(verbose_name='起运日期')),
                ('ship_date_print_format', models.CharField(max_length=20, verbose_name='起运日期打印格式')),
                ('port_compensate', models.CharField(max_length=128, verbose_name='赔付地')),
                ('special_goods_rate', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='特殊货物费率')),
                ('special_rate', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='特殊费率')),
                ('invoice_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='发票金额')),
                ('invoice_currency', models.CharField(max_length=20, verbose_name='发票金额币种')),
                ('slip_ratio', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='保单系数')),
                ('slip_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='保单金额')),
                ('slip_currency', models.CharField(max_length=20, verbose_name='保单金额币种')),
                ('is_credit_voucher', models.CharField(choices=[('Y', '是'), ('N', '否')], default='N', max_length=2, verbose_name='是否做信用凭证')),
                ('clause', models.TextField(verbose_name='条款内容')),
                ('other_clause', models.TextField(verbose_name='其他约定条款')),
                ('job_code', models.CharField(max_length=32, verbose_name='工作编号/操作人')),
                ('remark', models.CharField(max_length=1024, verbose_name='备注')),
                ('rate', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='费率')),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='总保费')),
                ('policy_number', models.CharField(max_length=32, verbose_name='保险公司保单号')),
                ('insure_date', models.DateField(verbose_name='投保日期')),
                ('sign_date', models.DateField(verbose_name='签单日期')),
                ('insurance_company_id', models.IntegerField(verbose_name='保险公司')),
                ('issuing_company_id', models.IntegerField(verbose_name='出单公司')),
                ('last_operator_id', models.IntegerField(verbose_name='最后操作人ID')),
                ('last_operate_time', models.DateTimeField(auto_now=True, null=True, verbose_name='最后操作时间')),
                ('status', models.CharField(max_length=20, verbose_name='保单状态')),
                ('actual_premium', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='实际保费')),
                ('actual_rate', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='实际费率')),
                ('exchange', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='汇率')),
                ('salesman_id', models.IntegerField(verbose_name='销售人员')),
                ('is_over_max', models.CharField(choices=[('Y', '是'), ('N', '否')], default='N', max_length=2, verbose_name='单件货物超过300万')),
                ('is_special_packing', models.CharField(choices=[('Y', '是'), ('N', '否')], default='N', max_length=2, verbose_name='是否特殊包装')),
                ('country_from', models.CharField(max_length=100, verbose_name='起运地国家')),
                ('country_to', models.CharField(max_length=100, verbose_name='目的地国家')),
                ('additional_insurance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurance_additional_insurance', to='InsuranceCompany.InsurancePolicy', verbose_name='附加险')),
                ('main_insurance', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='insurance_main_insurance', to='InsuranceCompany.InsurancePolicy', verbose_name='主险')),
                ('trans_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InsuranceCompany.TransType', verbose_name='运输方式')),
            ],
            options={
                'verbose_name': '保单',
                'verbose_name_plural': '保单',
            },
        ),
    ]