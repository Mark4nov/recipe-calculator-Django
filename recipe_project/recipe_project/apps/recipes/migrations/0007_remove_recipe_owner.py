# Generated by Django 3.2.7 on 2021-10-15 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_merge_0004_recipe_owner_0005_recipe_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='owner',
        ),
    ]
