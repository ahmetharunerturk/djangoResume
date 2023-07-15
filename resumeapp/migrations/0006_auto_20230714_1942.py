# Generated by Django 3.2.5 on 2023-07-14 17:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0005_kisiselbilgiler_hakkimda'),
    ]

    operations = [
        migrations.AddField(
            model_name='deneyim',
            name='firma',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='egitim',
            name='degree',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='kisiselbilgiler',
            name='background_photo',
            field=models.ImageField(null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AddField(
            model_name='kisiselbilgiler',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AlterField(
            model_name='deneyim',
            name='aciklama',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='egitim',
            name='aciklama',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='kisiselbilgiler',
            name='hakkimda',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]