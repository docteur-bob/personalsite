# Generated by Django 2.2 on 2019-04-14 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20190414_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page_projet',
            name='img_description',
            field=models.ImageField(default='desciption_projet/no-img.jpg', upload_to='description_projet/'),
        ),
    ]
