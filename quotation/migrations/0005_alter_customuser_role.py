# Generated by Django 5.0.6 on 2024-07-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotation', '0004_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(max_length=200),
        ),
    ]
