# Generated by Django 2.2 on 2019-04-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_page_projet_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='page_projet',
            name='img_description',
            field=models.ImageField(default='static/images/desciption_projet/no-img.jpg', upload_to='static/images/desciption_projet/'),
        ),
    ]
