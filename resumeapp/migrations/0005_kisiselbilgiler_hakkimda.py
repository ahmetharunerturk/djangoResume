# Generated by Django 3.2.5 on 2023-07-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0004_kisiselbilgiler_meslek'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisiselbilgiler',
            name='hakkimda',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
