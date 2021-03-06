# Generated by Django 2.1.1 on 2020-04-27 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='posts', to='blogging.Category'),
        ),
    ]
