# Generated by Django 3.2.4 on 2021-06-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='new_field',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]