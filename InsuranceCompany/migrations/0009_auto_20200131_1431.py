# Generated by Django 3.0.2 on 2020-01-31 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsuranceCompany', '0008_policyrules'),
    ]

    operations = [
        migrations.AddField(
            model_name='insurancecompany',
            name='city',
            field=models.CharField(blank=True, max_length=10, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='insurancecompany',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='保险公司'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='insurance_name',
            field=models.CharField(max_length=20, verbose_name='险种简称'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='remark',
            field=models.CharField(blank=True, max_length=255, verbose_name='备注'),
        ),
    ]
