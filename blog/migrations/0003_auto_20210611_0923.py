# Generated by Django 3.2.4 on 2021-06-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='url',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
