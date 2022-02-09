# Generated by Django 4.0.1 on 2022-01-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_delete_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_team', models.CharField(max_length=100)),
                ('road_score', models.CharField(max_length=50)),
                ('home_team', models.CharField(max_length=50)),
                ('home_score', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
