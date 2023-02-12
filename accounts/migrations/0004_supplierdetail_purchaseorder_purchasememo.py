# Generated by Django 4.1.5 on 2023-02-12 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_role_alter_user_business_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupplierDetail',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('supplier_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('po_id', models.AutoField(primary_key=True, serialize=False, verbose_name='POID')),
                ('purchase_date', models.DateField()),
                ('item_ref', models.TextField()),
                ('item_weight', models.FloatField()),
                ('item_variety', models.CharField(max_length=30)),
                ('item_shape', models.CharField(max_length=30)),
                ('item_series', models.CharField(max_length=30)),
                ('item_unit_price', models.IntegerField()),
                ('item_price', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.supplierdetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseMemo',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('memo_id', models.AutoField(primary_key=True, serialize=False)),
                ('memo_date', models.DateField()),
                ('item_ref', models.TextField()),
                ('item_weight', models.FloatField()),
                ('item_variety', models.CharField(max_length=30)),
                ('item_shape', models.CharField(max_length=30)),
                ('item_series', models.CharField(max_length=30)),
                ('item_unit_price', models.IntegerField()),
                ('item_price', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_purchased', models.BooleanField(default=False)),
                ('is_returned', models.BooleanField(default=False)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.supplierdetail')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
