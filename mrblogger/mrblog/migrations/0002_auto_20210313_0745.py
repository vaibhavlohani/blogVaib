# Generated by Django 3.1.7 on 2021-03-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='SOME STRING', max_length=130),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
