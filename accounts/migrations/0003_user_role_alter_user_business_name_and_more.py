# Generated by Django 4.1.5 on 2023-02-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_created_at_user_updated_at_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('DE', 'Default Role'), ('BO', 'Business Owner'), ('AA', 'Account Admin'), ('PM', 'Purchase Manager'), ('SM', 'Sales Manager')], default='DE', max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='business_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
