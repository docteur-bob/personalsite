# Generated by Django 2.2 on 2019-04-14 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page_projet',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
