# Generated by Django 5.0.6 on 2024-05-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_querymodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querymodel',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
