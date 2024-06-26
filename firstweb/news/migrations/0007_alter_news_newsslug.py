# Generated by Django 5.0.3 on 2024-04-01 17:23

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_news_newsslug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsSlug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='news_title', unique=True),
        ),
    ]
