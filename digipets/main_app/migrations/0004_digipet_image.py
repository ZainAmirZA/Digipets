# Generated by Django 4.0.4 on 2022-05-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_digipet_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='digipet',
            name='image',
            field=models.ImageField(default='main_app\\static\\digipets\x07ssets\x07nimals\\{species}\x01.svg', upload_to=''),
        ),
    ]
