# Generated by Django 3.2.7 on 2021-09-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]
