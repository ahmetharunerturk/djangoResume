# Generated by Django 3.2.5 on 2023-07-14 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0006_auto_20230714_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kisiselbilgiler',
            name='background_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='kisiselbilgiler',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]
