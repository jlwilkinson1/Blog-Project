# Generated by Django 3.1.7 on 2021-03-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]