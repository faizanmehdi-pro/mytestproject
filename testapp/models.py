import random
import string
import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from datetime import datetime
from PIL import Image
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.conf import settings
# Renaming the uploaded image


class Staff(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.PROTECT)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    postal = models.IntegerField(null=True, blank=True)
    country = CountryField(blank_label='Select Country', null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    birthdate = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True, null=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user.first_name)

    def save(self, *args, **kwargs):
        super(Staff, self).save(*args, **kwargs)
        # Opening the image using Pillow
        picture = Image.open(self.profile_pic.path)
        # Checking if image has size greater than (150, 150).
        if picture.height > 150 or picture.width > 150:
            # Making it strict to (150, 150) size.
            output_size = (150, 150)
            # We can use resize but to avoid format restrictions, going with thumbnail.
            picture.thumbnail(output_size)
            picture.save(self.profile_pic.path, quality=40)

    # def remove_profile_pic(self):
    #     self.user.staff.profile_pic.delete(save=False)  # delete old image file
    #     self.user.staff.profile_pic = 'default.jpg'  # set default image
    #     self.user.staff.save()


# @receiver(pre_save, sender=Staff)
# def overwrite_previous_file(sender, instance, **kwargs):
#     if instance.pk:
#         try:
#             # Getting the old profile_pic
#             old_profile_pic = Staff.objects.get(pk=instance.pk).profile_pic
#         except Staff.DoesNotExist:
#             return
#         else:
#             # Getting new profile_pic
#             new_profile_pic = instance.profile_pic
#             # Checking if old profile_pic and new profile_pic is from same user
#             # then overwriting new profile_pic over old one.
#             if old_profile_pic and old_profile_pic.url == new_profile_pic.url:
#                 old_profile_pic.delete(save=False)
#

class Admin(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.PROTECT)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=1024, blank=True, null=True)
    postal = models.CharField(max_length=255, blank=True, null=True)
    country = CountryField(blank_label='Select Country', null=True, blank=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    birthdate = models.DateField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='images/', default='images/default.jpg', blank=True, null=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

    def save(self, *args, **kwargs):
        super(Admin, self).save(*args, **kwargs)
        # Opening the image using Pillow
        picture = Image.open(self.profile_pic.path)
        # Checking if image has size greater than (150, 150).
        if picture.height > 150 or picture.width > 150:
            # Making it strict to (150, 150) size.
            output_size = (150, 150)
            # We can use resize but to avoid format restrictions, going with thumbnail.
            picture.thumbnail(output_size)
            picture.save(self.profile_pic.path, quality=40)
    #
    # def remove_profile_pic(self):
    #     self.user.admin.profile_pic.delete(save=False)  # delete old image file
    #     self.user.admin.profile_pic = 'default.jpg'  # set default image
    #     self.user.admin.save()


# @receiver(pre_save, sender=Admin)
# def overwrite_previous_file(sender, instance, **kwargs):
#     if instance.pk:
#         try:
#             # Getting the old profile_pic
#             old_profile_pic = Admin.objects.get(pk=instance.pk).profile_pic
#         except Admin.DoesNotExist:
#             return
#         else:
#             # Getting new profile_pic
#             new_profile_pic = instance.profile_pic
#             # Checking if old profile_pic and new profile_pic is from same user
#             # then overwriting new profile_pic over old one.
#             if old_profile_pic and old_profile_pic.url != new_profile_pic.url:
#                 old_profile_pic.delete(save=False)


class Company(models.Model):
    HEADOFFICE = 'H'
    BRANCH = 'B'

    TYPE_CHOICES = (
        (HEADOFFICE, 'Head Office'),
        (BRANCH, 'Branch'),
    )

    name = models.CharField(max_length=255)
    license_name = models.CharField(max_length=255, null=True, blank=True)
    license_file = models.FileField(upload_to='files/', null=True, blank=True)
    email = models.EmailField()
    logistics_email = models.EmailField(null=True, blank=True)
    technical_support_email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    phone = models.CharField(max_length=255)
    trn = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Category(models.Model):
    company = models.ManyToManyField(Company, blank=True)
    title = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    company = models.ManyToManyField(Company, blank=True)
    category = models.ForeignKey(Category, related_name='sub_categories', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sub_Category'
        verbose_name_plural = 'Sub_Categories'


class SubSubCategory(models.Model):
    company = models.ManyToManyField(Company, blank=True)
    sub_category = models.ForeignKey(SubCategory, related_name='sub_sub_categories', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sub_Sub_Category'
        verbose_name_plural = 'Sub_Sub_Categories'


class Currency(models.Model):
    title = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True)
    country = CountryField(blank_label='Select Country')
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class Brand(models.Model):
    company = models.ManyToManyField(Company, blank=True)
    title = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True, blank=True)
    brand_logo = models.ImageField(upload_to='brand_logo/', null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    url = models.SlugField(default='', editable=False, max_length=200, null=True, blank=True)
    seo_title = models.TextField(null=True, blank=True)
    seo_keywords = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.TextField(null=True, blank=True)
    new_field = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    # Generating the unique url for each brand
    def save(self, *args, **kwargs):
        # Generating the random string of length 10 which will be added at end of url to make it unique
        random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(7))
        # Formatting the string as we want url
        slug_str = "%s %s" % (self.title, random_string)
        slug_str = slug_str.lower()
        # Slugifying them(Putting hyphens in place of spaces)
        self.url = slugify(slug_str)
        super(Brand, self).save(**kwargs)


class VATCategory(models.Model):
    code = models.CharField(max_length=255, default='')
    description_name = models.CharField(max_length=255, null=True, blank=True)
    value = models.IntegerField()
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'VAT_Category'
        verbose_name_plural = 'VAT_Categories'


class ProductType(models.Model):
    code = models.CharField(max_length=255, default='')
    description_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.description_name


class ProductGroup(models.Model):
    code = models.CharField(max_length=255, default='')
    description_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.description_name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    code_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    website = models.URLField(null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


class Csv(models.Model):
    file_name = models.FileField(upload_to='csv')
    uploaded_time = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.uploaded_time)


class WareHouse(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    # product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.PROTECT)
    code_name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.company.name

    class Meta:
        verbose_name = 'WareHouse'
        verbose_name_plural = 'WareHouses'


#################################
### Models of Product Module ###
#################################
class Product(models.Model):
    company = models.ManyToManyField(Company, blank=True)
    vat = models.ForeignKey(VATCategory, null=True, blank=True, on_delete=models.PROTECT)
    product_type = models.ForeignKey(ProductType, null=True, blank=True, on_delete=models.PROTECT)
    product_group = models.ForeignKey(ProductGroup, null=True, blank=True, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, null=True, blank=True, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, default='', on_delete=models.PROTECT)
    warehouse = models.ForeignKey(WareHouse, null=True, blank=True, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, null=True, blank=True, on_delete=models.PROTECT)
    sub_sub_category = models.ForeignKey(SubSubCategory, null=True, blank=True, on_delete=models.PROTECT)

    title = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    barcode = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, default='')
    quantity = models.IntegerField(null=True, blank=True)
    web_price = models.DecimalField(max_digits=10, decimal_places=2)
    web_active = models.BooleanField(default=True, blank=True)
    status = models.BooleanField()
    url = models.SlugField(default='', unique=True, editable=False, max_length=200, null=True, blank=True)
    serial_number = models.CharField(unique=True, editable=False, max_length=200, null=True, blank=True)
    warrenty = models.CharField(max_length=255, null=True, blank=True)
    EAN_number = models.CharField(unique=True, max_length=255, null=True, blank=True)
    edit_by = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True, blank=True, null=True)
    # internal_code = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Products'

    # Generating the unique url for each product item
    def save(self, *args, **kwargs):
        # Generating 10 digit random alpha_numeric random string for serial number
        random_string_for_serial_number = ''.join(
            random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
        # Putting random number in serial number
        self.serial_number = random_string_for_serial_number

        # Generating 10 digit random numeric random string for EAN number
        random_digits_for_EAN_number = ''.join(
            random.SystemRandom().choice(string.digits + string.digits) for _ in range(13))
        self.EAN_number = random_digits_for_EAN_number

        # Generating the random string of length 10 which will be added at end of url to make it unique
        random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
        # Putting optional as a string in start of url
        optional = "buy a"
        # Formatting the string as we want url to be (buy-a-<product-title>-<brand>-<category>
        slug_str = "%s %s %s %s %s" % (optional, self.title, self.brand.title, self.category.title, random_string)
        slug_str = slug_str.lower()
        # Slugifying them(Putting hyphens in place of spaces)
        self.url = slugify(slug_str)
        super(Product, self).save(**kwargs)


class WareHouseStock(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)
    warehouse = models.ForeignKey(WareHouse, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.PROTECT)
    warehouse_address = models.TextField(blank=True, null=True)
    total_quantity = models.IntegerField(null=True, blank=True)
    available_quantity = models.IntegerField(null=True, blank=True)
    reserved_quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.warehouse_address)

    class Meta:
        verbose_name_plural = 'WareHouses Stock'


class ProductFinancial(models.Model):
    product = models.ForeignKey(Product, related_name='product_financial', on_delete=models.PROTECT)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_without_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_with_tax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    web_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    web_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    edit_by = models.CharField(max_length=255, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Products Financials'


class Related(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.product)


class Alternative(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.product)


class Accessories(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.product)


class BoughtTogether(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.product)


class ProductRelation(models.Model):
    product = models.ForeignKey(Product, related_name='product_relations', on_delete=models.PROTECT)
    related = models.ManyToManyField(Related, blank=True)
    alternative = models.ManyToManyField(Alternative, blank=True)
    accessories = models.ManyToManyField(Accessories, blank=True)
    bought_together = models.ManyToManyField(BoughtTogether, blank=True)

    fast_moving = models.BooleanField(default=False, blank=True)
    discountinue = models.BooleanField(default=False, blank=True)
    new = models.BooleanField(default=False, blank=True)
    clearance = models.BooleanField(default=False, blank=True)
    special_offer = models.BooleanField(default=False, blank=True)
    featured = models.BooleanField(default=False, blank=True)
    limited_edition = models.BooleanField(default=False, blank=True)
    refurbishment = models.BooleanField(default=False, blank=True)
    edit_by = models.CharField(max_length=255, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Products Relations'


class ProductProperty(models.Model):
    product = models.ForeignKey(Product, related_name='product_property', on_delete=models.PROTECT)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='item_images/%Y/%m', null=True, blank=True)
    image2 = models.ImageField(upload_to='item_images/%Y/%m', null=True, blank=True)
    image3 = models.ImageField(upload_to='item_images/%Y/%m', null=True, blank=True)
    image4 = models.ImageField(upload_to='item_images/%Y/%m', null=True, blank=True)
    image5 = models.ImageField(upload_to='item_images/%Y/%m', null=True, blank=True)
    image6 = models.ImageField(upload_to='item_images/%Y/%m', null=True, blank=True)
    view = models.CharField(max_length=1024, null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    youtube = models.CharField(max_length=1024, null=True, blank=True)
    catalog_file = models.FileField(upload_to='catalog_files', null=True, blank=True)
    edit_by = models.CharField(max_length=255, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Products Properties'


class ProductSpecs(models.Model):
    product = models.ForeignKey(Product, related_name='product_specs', on_delete=models.PROTECT)
    weight = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)
    seo_title = models.CharField(max_length=1024, null=True, blank=True)
    seo_keywords = models.CharField(max_length=255, null=True, blank=True)
    seo_description = models.CharField(max_length=1024, null=True, blank=True)
    edit_by = models.CharField(max_length=255, null=True, blank=True)
    specs1_title = models.CharField(max_length=255, null=True, blank=True)
    specs1_value = models.CharField(max_length=255, null=True, blank=True)
    specs2_title = models.CharField(max_length=255, null=True, blank=True)
    specs2_value = models.CharField(max_length=255, null=True, blank=True)
    specs3_title = models.CharField(max_length=255, null=True, blank=True)
    specs3_value = models.CharField(max_length=255, null=True, blank=True)
    specs4_title = models.CharField(max_length=255, null=True, blank=True)
    specs4_value = models.CharField(max_length=255, null=True, blank=True)
    specs5_title = models.CharField(max_length=255, null=True, blank=True)
    specs5_value = models.CharField(max_length=255, null=True, blank=True)
    specs6_title = models.CharField(max_length=255, null=True, blank=True)
    specs6_value = models.CharField(max_length=255, null=True, blank=True)
    specs7_title = models.CharField(max_length=255, null=True, blank=True)
    specs7_value = models.CharField(max_length=255, null=True, blank=True)
    specs8_title = models.CharField(max_length=255, null=True, blank=True)
    specs8_value = models.CharField(max_length=255, null=True, blank=True)
    specs9_title = models.CharField(max_length=255, null=True, blank=True)
    specs9_value = models.CharField(max_length=255, null=True, blank=True)
    specs10_title = models.CharField(max_length=255, null=True, blank=True)
    specs10_value = models.CharField(max_length=255, null=True, blank=True)
    specs11_title = models.CharField(max_length=255, null=True, blank=True)
    specs11_value = models.CharField(max_length=255, null=True, blank=True)
    specs12_title = models.CharField(max_length=255, null=True, blank=True)
    specs12_value = models.CharField(max_length=255, null=True, blank=True)
    specs13_title = models.CharField(max_length=255, null=True, blank=True)
    specs13_value = models.CharField(max_length=255, null=True, blank=True)
    specs14_title = models.CharField(max_length=255, null=True, blank=True)
    specs14_value = models.CharField(max_length=255, null=True, blank=True)
    specs15_title = models.CharField(max_length=255, null=True, blank=True)
    specs15_value = models.CharField(max_length=255, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Products Specifications'


####################################
###### Marketing Module #######
####################################
class Coupon(models.Model):
    # OneToMany Relation with Brands and Categories
    brand = models.ManyToManyField(Brand, blank=True)
    category = models.ManyToManyField(Category, blank=True)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    max_discount = models.CharField(max_length=255, default=None)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    single_use = models.BooleanField(default=False, blank=True)
    coupon_logo = models.ImageField(null=True, blank=True)
    coupon_banner = models.ImageField(null=True, blank=True)
    fast_moving = models.BooleanField(default=False, blank=True)
    discountinue = models.BooleanField(default=False, blank=True)
    new = models.BooleanField(default=False, blank=True)
    clearance = models.BooleanField(default=False, blank=True)
    special_offer = models.BooleanField(default=False, blank=True)
    featured = models.BooleanField(default=False, blank=True)
    limited_edition = models.BooleanField(default=False, blank=True)
    refurbishment = models.BooleanField(default=False, blank=True)
    active = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Coupons'


class Coupon_Usage(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    number_of_usage = models.IntegerField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.coupon)

    class Meta:
        verbose_name_plural = 'Coupons Usage'


class Campaign(models.Model):
    # ManyToMany Relation with Brands, Categories and Coupon
    brand = models.ManyToManyField(Brand, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    coupon = models.ForeignKey(Coupon, null=True, blank=True, on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    campaign_logo = models.ImageField(null=True, blank=True)
    campaign_banner = models.ImageField(null=True, blank=True)
    active = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Campaigns'


class Campaign_Coupon_Usage(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT)
    number_of_usage = models.IntegerField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.compaign)

    class Meta:
        verbose_name_plural = 'Campaigns Coupons Usage'


####################################
### Customer and Order Module ####
####################################
# class Country(models.Model):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return str(self.name)
#
#
# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.PROTECT)
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=50)
#
#     def __str__(self):
#         return str(self.name)


class Customer(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=255)
    postal_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(default='')
    flat = models.CharField(max_length=100, null=True, blank=True)
    building = models.CharField(max_length=100, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    near_landmark = models.CharField(max_length=100, null=True, blank=True)
    default_address = models.BooleanField(default=False, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    status = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Customers'


class Order(models.Model):
    # Choices for Payment types
    CASH_ON_DELIVERY = 'CASH_ON_DELIVERY'
    ONLINE_PAYMENT = 'ONLINE_PAYMENT'
    PAYMENT_CHOICES = (
        (CASH_ON_DELIVERY, 'Cash On Delivery'),
        (ONLINE_PAYMENT, 'Online Payment'),
    )

    # Choices for Order Status
    COMPLETE = 'COMPLETE'
    PENDING = 'PENDING'
    DELIVERED = 'DELIVERED'
    CANCELED = 'CANCELED'
    PARTIAL_DELIVERED = 'PARTIAL_DELIVERED'
    ORDER_STATUS = (
        (COMPLETE, 'Complete'),
        (PENDING, 'Pending'),
        (DELIVERED, 'Delivered'),
        (CANCELED, 'Canceled'),
        (PARTIAL_DELIVERED, 'Partial Delivered'),
    )
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    coupon = models.ForeignKey(Coupon, on_delete=models.PROTECT, null=True, blank=True)
    code = models.SlugField(unique=True, max_length=20)  # Generate at backend
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.CharField(max_length=100, null=True, blank=True)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    total_quantity = models.IntegerField()
    tax = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    shipment_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS, default='PENDING', null=True, blank=True)
    redeem_currency = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    redeem = models.BooleanField(null=True, blank=True)
    # To track from where the order has been posted
    api = models.BooleanField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer.name)

    class Meta:
        verbose_name_plural = 'Orders'

    def save(self, *args, **kwargs):
        # Generating the random unique digits of length 4
        random_digits_for_code = ''.join(
            random.SystemRandom().choice(string.digits + string.digits) for _ in range(9))
        optional = 'S'
        # Formatting the string as S-<random numbers>
        slug_number = "%s %s" % (optional, random_digits_for_code)
        slug_number = slug_number.upper()
        self.code = slugify(slug_number)
        super(Order, self).save(**kwargs)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(null=True, blank=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.order.customer)

    class Meta:
        verbose_name_plural = 'Orders Details'


class OrderReservation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    reserved_quantity = models.IntegerField(null=True, blank=True)
    processed = models.BooleanField()

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.order.customer)


class Stock(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    total_quantity = models.IntegerField(null=True, blank=True)
    available_quantity = models.IntegerField(null=True, blank=True)
    reserved_quantity = models.IntegerField(null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.product)


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    api = models.BooleanField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Complain(models.Model):
    NOT_AS_DESCRIBED = 'NOT_AS_DESCRIBED'
    DEFECT = 'DEFECT'
    INITIATE_CANCELLATION_OR_RETURN = 'INITIATE_CANCELLATION_OR_RETURN'
    DELAY_OF_SHIPMENT = 'DELAY_OF_SHIPMENT'
    MISSING_PARTS_OR_ACCESSORIES = 'MISSING_PARTS_OR_ACCESSORIES'
    INCOMPLETE_QUANTITY = 'INCOMPLETE_QUANTITY'
    TOTALLY_DIFFERENT_ITEMS = 'TOTALLY_DIFFERENT_ITEMS'
    WARRANTY_ISSUE = 'WARRANTY_ISSUE'
    NOT_INTERESTED_IN_ITEM = 'NOT_INTERESTED_IN_ITEM'

    COMPLAIN_TYPE = (
        (NOT_AS_DESCRIBED, 'Not As Described'),
        (DEFECT, 'Defect'),
        (INITIATE_CANCELLATION_OR_RETURN, 'Initiate Cancellation or Return'),
        (DELAY_OF_SHIPMENT, 'Delay of the Shipment'),
        (MISSING_PARTS_OR_ACCESSORIES, 'Missing Parts or Accessories'),
        (INCOMPLETE_QUANTITY, 'Incomplete quantity'),
        (TOTALLY_DIFFERENT_ITEMS, 'Totally Different Items'),
        (WARRANTY_ISSUE, 'Warranty Issue'),
        (NOT_INTERESTED_IN_ITEM, 'Not interested in Item')
    )

    ACTIVE = 'ACTIVE'
    COMPLETE = 'COMPLETE'
    PROCESSING = 'PROCESSING'

    COMPLAIN_STATUS = (
        (ACTIVE, 'Active'),
        (COMPLETE, 'Complete'),
        (PROCESSING, 'Processing')
    )
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    message = models.TextField(null=True, blank=True)
    type_of_complaint = models.CharField(max_length=100, choices=COMPLAIN_TYPE, null=True, blank=True)
    status = models.CharField(max_length=100, choices=COMPLAIN_STATUS)
    api = models.BooleanField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.order)


class Wishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    api = models.BooleanField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer)


class Queries(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'

    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    newsletter = models.BooleanField(default=False, blank=True)
    api = models.BooleanField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)

    # Custom Fields
    custom_int = models.IntegerField(null=True, blank=True)
    custom_float = models.FloatField(null=True, blank=True)
    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_longtext = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='events/', null=True, blank=True)
    image1 = models.ImageField(upload_to='events/', null=True, blank=True)
    image2 = models.ImageField(upload_to='events/', null=True, blank=True)
    image3 = models.ImageField(upload_to='events/', null=True, blank=True)
    image4 = models.ImageField(upload_to='events/', null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    video_link = models.CharField(max_length=1024, null=True, blank=True)
    map_location = models.CharField(max_length=1024, null=True, blank=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    status = models.BooleanField(default=True, blank=True)
    api = models.BooleanField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)

    # Custom Fields
    custom_int = models.IntegerField(null=True, blank=True)
    custom_float = models.FloatField(null=True, blank=True)
    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_longtext = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    # def save(self, *args, **kwargs):
    #     super(Event, self).save(*args, **kwargs)
    #     # Opening the image1 using Pillow
    #     picture = Image.open(self.image1.path)
    #     # Checking if image has size greater than (150, 150).
    #     if picture.height > 150 or picture.width > 150:
    #         # Making it strict to (150, 150) size.
    #         output_size = (150, 150)
    #         # Making the thumbnail and saving it to the thumbnail column.
    #         picture.thumbnail(output_size)
    #         picture.save(self.thumbnail.path, quality=40)


class LoyaltyPoints(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.BooleanField()
    exclude_brands = models.ManyToManyField(Brand, blank=True)
    exclude_categories = models.ManyToManyField(Category, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)


class TrackPoints(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    earned = models.BooleanField(null=True, blank=True)
    used = models.BooleanField(null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer.name)


class EarnedPoints(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer.name)


class RemainingPoints(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True, blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    equal_currency = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer.name)


class UsedPoints(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    points = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_int_3 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_float_3 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_3 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_3 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_date_3 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.customer.name)


class Author(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    published_posts = models.CharField(max_length=100, null=True, blank=True)
    status = models.BooleanField()

    # Custom Fields
    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)
    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)
    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)
    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)
    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)
    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    Published = 'Published'
    Draft = 'Draft'

    STATUS_CHOICES = (
        (Published, 'Published'),
        (Draft, 'Draft'),
    )

    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    url = models.SlugField(max_length=200, default='', editable=False, unique=True)
    publish = models.DateTimeField(auto_now_add=True)
    published_by = models.CharField(max_length=100, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True, choices=STATUS_CHOICES)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    # Custom Fields
    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        # Generating the random string of length 10 which will be added at end of url to make it unique
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        slug_url = "%s%s" % (self.title, x)

        # Slugifying them(Putting hyphens in place of spaces)
        self.url = slugify(slug_url)
        super(Post, self).save(**kwargs)


class RelatedPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.post)


class RelatedItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, blank=True)
    status = models.BooleanField(default=True, blank=True)

    def __str__(self):
        return str(self.item)


class PostRelation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=True, blank=True)
    related_item = models.ManyToManyField(RelatedItem, blank=True)
    related_posts = models.ManyToManyField(RelatedPost, blank=True)

    def __str__(self):
        return str(self.post)


class PostStatistics(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, null=True, blank=True)
    views = models.CharField(max_length=50, null=True, blank=True)
    likes = models.CharField(max_length=50, null=True, blank=True)
    comments = models.CharField(max_length=50, null=True, blank=True)

    # Custom Fields
    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)


class Comments(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    # Custom Fields
    custom_int_1 = models.IntegerField(null=True, blank=True)
    custom_int_2 = models.IntegerField(null=True, blank=True)

    custom_float_1 = models.FloatField(null=True, blank=True)
    custom_float_2 = models.FloatField(null=True, blank=True)

    custom_string_1 = models.CharField(max_length=255, null=True, blank=True)
    custom_string_2 = models.CharField(max_length=255, null=True, blank=True)

    custom_longtext_1 = models.CharField(max_length=1024, null=True, blank=True)
    custom_longtext_2 = models.CharField(max_length=1024, null=True, blank=True)

    custom_date_1 = models.DateField(null=True, blank=True)
    custom_date_2 = models.DateField(null=True, blank=True)

    custom_datetime_1 = models.DateTimeField(null=True, blank=True)
    custom_datetime_2 = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.text)
