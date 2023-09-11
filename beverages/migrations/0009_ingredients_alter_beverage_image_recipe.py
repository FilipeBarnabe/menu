# Generated by Django 4.2.4 on 2023-09-03 18:41

import beverages.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beverages', '0008_alter_beverage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='beverage',
            name='image',
            field=models.ImageField(blank=True, upload_to=beverages.models.upload_name),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=20)),
                ('beverage', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='beverages.beverage')),
                ('ingredient', models.ManyToManyField(to='beverages.ingredients')),
            ],
        ),
    ]
