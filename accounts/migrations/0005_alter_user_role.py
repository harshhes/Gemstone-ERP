# Generated by Django 4.1.5 on 2023-02-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_supplierdetail_purchaseorder_purchasememo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('DE', 'Default Role'), ('BO', 'Business Owner'), ('AA', 'Account Admin'), ('PM', 'Purchase Manager'), ('SM', 'Sales Manager'), ('SA', 'Sales & Accounting'), ('OA', 'Operations Associate')], default='DE', max_length=2),
        ),
    ]
