# Generated by Django 2.2 on 2019-04-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20190415_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page_projet',
            name='img_description',
            field=models.ImageField(default='description_projets/no-img.jpg', upload_to='description_projets/'),
        ),
    ]
