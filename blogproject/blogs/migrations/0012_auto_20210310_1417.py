# Generated by Django 3.1.7 on 2021-03-10 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_auto_20210310_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default='C:/Users/jlwil/blogproject/blogproject/blogs/tempdefault.jpg', upload_to='blogs'),
        ),
    ]
