# Generated by Django 3.0.2 on 2020-02-01 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InsuranceCompany', '0017_auto_20200201_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policyrules',
            name='additional_insurance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='additional_insurance', to='InsuranceCompany.InsurancePolicy', verbose_name='附加险'),
        ),
    ]
