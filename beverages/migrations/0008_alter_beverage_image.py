# Generated by Django 4.2.4 on 2023-09-03 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverages', '0007_rename_image_link_beverage_post_link_beverage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/beverages/'),
        ),
    ]
