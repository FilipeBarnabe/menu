# Generated by Django 4.2.4 on 2023-08-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beverages', '0005_alter_beveragetype_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beverage',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='beveragetype',
            options={'ordering': ['type_name']},
        ),
        migrations.AddField(
            model_name='beverage',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
