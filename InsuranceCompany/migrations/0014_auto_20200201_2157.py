# Generated by Django 3.0.2 on 2020-02-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InsuranceCompany', '0013_auto_20200201_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', '生效')], max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='insurance_type',
            field=models.CharField(choices=[('Main', '主险'), ('Additional', '附加险')], max_length=10, verbose_name='险种类别'),
        ),
        migrations.AlterField(
            model_name='insurancepolicy',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', '生效')], max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='policyrules',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', '生效')], max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='transmap',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', '生效')], max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='transrange',
            name='status',
            field=models.CharField(blank='Inactive', choices=[('Active', '生效')], max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='transtype',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', '生效')], max_length=10, verbose_name='状态'),
        ),
    ]
