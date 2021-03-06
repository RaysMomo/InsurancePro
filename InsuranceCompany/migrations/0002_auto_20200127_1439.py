# Generated by Django 3.0.2 on 2020-01-27 14:39

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('InsuranceCompany', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Active', '生效')], max_length=6, verbose_name='状态')),
            ],
        ),
        migrations.AlterModelOptions(
            name='transrange',
            options={'verbose_name': '运输范围', 'verbose_name_plural': '运输范围'},
        ),
        migrations.AlterField(
            model_name='transrange',
            name='status',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Active', '生效')], max_length=6, verbose_name='状态'),
        ),
        migrations.CreateModel(
            name='TransType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=10, unique=True, verbose_name='运输方式')),
                ('sort_code', models.IntegerField(verbose_name='显示排序')),
                ('status', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Active', '生效')], max_length=6, verbose_name='状态')),
                ('trans_range', models.ManyToManyField(through='InsuranceCompany.TransMap', to='InsuranceCompany.TransRange')),
            ],
            options={
                'verbose_name': '运输方式',
                'verbose_name_plural': '运输方式',
            },
        ),
        migrations.AddField(
            model_name='transmap',
            name='trans_range',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InsuranceCompany.TransRange'),
        ),
        migrations.AddField(
            model_name='transmap',
            name='trans_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InsuranceCompany.TransType'),
        ),
    ]
