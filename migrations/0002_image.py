# Generated by Django 4.1.7 on 2023-03-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TMA3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=140)),
                ('image_location', models.CharField(max_length=140)),
                ('image_caption', models.CharField(max_length=140)),
            ],
        ),
    ]