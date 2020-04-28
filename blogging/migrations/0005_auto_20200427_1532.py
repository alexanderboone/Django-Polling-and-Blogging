# Generated by Django 2.1.1 on 2020-04-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_auto_20200427_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='blogging.Post'),
        ),
    ]