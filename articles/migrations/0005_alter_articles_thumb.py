# Generated by Django 3.2.7 on 2021-09-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_articles_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to='articles/images'),
        ),
    ]
