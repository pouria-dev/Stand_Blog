# Generated by Django 5.0.7 on 2024-09-10 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_comment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='post',
        ),
    ]
