# Generated by Django 5.0.7 on 2024-08-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
