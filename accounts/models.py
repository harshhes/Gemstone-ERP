from datetime import date
import pycountry
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from .mixins import Timestampedmodel
from django.core.files.storage import FileSystemStorage
from django.db import models
from rest_framework.exceptions import ValidationError


class User(AbstractUser,Timestampedmodel):
    roles = [
    ('DE', 'Default Role'),
    ('BO', 'Business Owner'),
    ('AA', 'Account Admin'),
    ('PM', 'Purchase Manager'),
    ('SM', 'Sales Manager'),
    ('SA', 'Sales & Accounting'), # custom role
    ('OA', 'Operations Associate'), # custom role

]
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=20, null=True, blank=True)
    business_name = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=2, choices=roles, default='DE')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class SupplierDetail(Timestampedmodel):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class PurchaseMemo(Timestampedmodel):
    memo_id = models.AutoField(primary_key=True)
    memo_date = models.DateField()
    supplier = models.ForeignKey(SupplierDetail, on_delete=models.PROTECT)
    item_ref = models.TextField()
    item_weight = models.FloatField()
    item_variety = models.CharField(max_length=30)
    item_shape =models.CharField(max_length=30)
    item_series = models.CharField(max_length=30)
    item_unit_price = models.IntegerField()
    item_price = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_purchased = models.BooleanField(default=False)
    is_returned = models.BooleanField(default=False)


class PurchaseOrder(Timestampedmodel):
    po_id = models.AutoField("POID",primary_key=True)
    purchase_date = models.DateField()
    supplier = models.ForeignKey(SupplierDetail, on_delete=models.PROTECT)
    item_ref = models.TextField()
    item_weight = models.FloatField()
    item_variety = models.CharField(max_length=30)
    item_shape =models.CharField(max_length=30)
    item_series = models.CharField(max_length=30)
    item_unit_price = models.IntegerField()
    item_price = models.IntegerField()


class Item(Timestampedmodel):
    category_choices = [
        ('single', 'Single'),
        ('parcel', 'Parcel'),
        ('jewelry', 'Jewelry'),
    ]
    types = [
        ('C&P', 'Cut & Polish'),
        ('rough', 'Rough'),
    ]
    calibrated_parcel = [
            ('parcel',(
                ('none', 'None'),
                ('yes', 'Yes'),
                ('no', 'No')
        ))]
    
    weight_options = [
        ('ct','ct'),
        ('gm','gm'),
        ('kg','kg'),
        ('lb','lb'),
        ('oz','oz'),

    ]

    variety_choices = [
        ('ruby','Ruby'),
        ('sapphire','Sapphire'),
        ('others','Others'),
    ]
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
    ]

    NUMBER_CHOICES = [(i, i) for i in range(1, 51)]
    ownership_choices = [
        ('FO', 'Full Ownership'),
        ("OM","On Memo"),
        ("partnership","Partnership")
    ]
    #for stone images
    MAX_IMAGES = 10
    MAX_IMAGE_SIZE = 3 * 1024 * 1024 # 3 MB

    category = models.CharField(max_length=10, choices=category_choices, default='single')
    type = models.CharField(max_length=10, choices=types, default='rough')
    reference = models.AutoField(primary_key=True)
    calibrated = models.CharField(max_length=10, choices=calibrated_parcel, default='none')
    weight_value = models.DecimalField(max_digits=5,decimal_places=2)
    weight_unit = models.CharField(max_length=2, choices=weight_options, default='ct')
    variety = models.CharField(max_length=10, choices=variety_choices, default='ruby')
    color = models.CharField(max_length=10,choices=COLOR_CHOICES,default='red',null=True, blank=True)
    number = models.IntegerField(choices=NUMBER_CHOICES, default=1,null=True, blank=True)
    purchase_date = models.DateField(default=date.today)
    date_added = models.DateField(auto_now_add=True, editable=False)
    country = models.CharField(max_length=100, choices=[(country.alpha_2, country.name) for country in pycountry.countries],null=True, blank=True)
    ownership_type = models.CharField(max_length=20, choices=ownership_choices, default='FO')
    supplier = models.ForeignKey(SupplierDetail, on_delete=models.PROTECT)
    stone_images = models.ImageField(upload_to='images/', storage=FileSystemStorage(), blank=True, null=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.rate:
            self.total = self.rate * self.weight_value

        if self.pk is None:
            if Item.objects.count() >= self.MAX_IMAGES:
                raise ValidationError(f'You can only upload up to {self.MAX_IMAGES} images.')
        if self.stone_images:
            if self.stone_images.size > self.MAX_IMAGE_SIZE:
                raise ValidationError(f'Image size must not exceed {self.MAX_IMAGE_SIZE / 1024 / 1024} MB')
        super().save(*args, **kwargs)

# class ImageUploader(models.Model):
#     MAX_IMAGES = 10
#     MAX_IMAGE_SIZE = 3 * 1024 * 1024 # 3 MB

   