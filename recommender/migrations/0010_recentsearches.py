# Generated by Django 3.2.15 on 2022-10-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0009_alter_playlist_playlist_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentSearches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('from_year', models.IntegerField(blank=True, null=True)),
                ('to_year', models.IntegerField(blank=True, null=True)),
                ('results', models.ManyToManyField(blank=True, null=True, to='recommender.Musicdata')),
            ],
        ),
    ]
