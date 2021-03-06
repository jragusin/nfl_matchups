# Generated by Django 4.0.1 on 2022-01-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0015_delete_games'),
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
                ('draw', models.BooleanField()),
                ('date', models.DateField()),
            ],
        ),
    ]
