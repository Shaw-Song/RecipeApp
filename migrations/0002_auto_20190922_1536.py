# Generated by Django 2.2.3 on 2019-09-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_discription',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_description',
            field=models.TextField(default='good!', max_length=200),
        ),
    ]