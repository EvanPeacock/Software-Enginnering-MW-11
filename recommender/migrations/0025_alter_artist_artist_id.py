# Generated by Django 3.2.15 on 2022-11-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0024_auto_20221109_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artist_id',
            field=models.TextField(default='ec69cc01-7ab7-4728-b9dd-376786f5159f', primary_key=True, serialize=False),
        ),
    ]