# Generated by Django 3.0.2 on 2020-01-27 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InsuranceCompany', '0002_auto_20200127_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transmap',
            options={'verbose_name': '运输范围与运输方式', 'verbose_name_plural': '运输范围与运输方式'},
        ),
        migrations.AlterField(
            model_name='transmap',
            name='trans_range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InsuranceCompany.TransRange', verbose_name='运输范围'),
        ),
        migrations.AlterField(
            model_name='transmap',
            name='trans_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InsuranceCompany.TransType', verbose_name='运输方式'),
        ),
        migrations.AlterUniqueTogether(
            name='transmap',
            unique_together={('trans_range', 'trans_type')},
        ),
    ]