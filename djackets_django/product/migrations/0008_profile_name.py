# Generated by Django 4.1.4 on 2023-01-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
