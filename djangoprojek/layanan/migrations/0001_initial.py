# Generated by Django 4.1.6 on 2023-02-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('work', models.CharField(max_length=80)),
                ('review', models.TextField(max_length=100)),
                ('photos', models.ImageField(default='layanan/testimony.png', upload_to='layanan/')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
