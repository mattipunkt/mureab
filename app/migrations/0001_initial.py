# Generated by Django 5.0.2 on 2024-02-21 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='No Title', max_length=400)),
                ('artist', models.CharField(default='No Artist', max_length=400)),
                ('link', models.CharField(default='https://www.youtube.com/watch?v=dQw4w9WgXcQ', max_length=300)),
                ('pub_date', models.DateField(verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('FOR', 'Dafür'), ('AGAINST', 'Dagegen'), ('NIGHT', 'Nachtrotation'), ('ABSTAIN', 'Enthaltung')], max_length=20)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.song')),
            ],
        ),
    ]