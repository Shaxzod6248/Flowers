# Generated by Django 4.1.4 on 2022-12-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_flower_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='describe',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flower',
            name='image',
            field=models.ImageField(null=True, upload_to='flower_images'),
        ),
    ]
