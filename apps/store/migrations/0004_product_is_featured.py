# Generated by Django 4.0.3 on 2022-03-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_category_options_category_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]