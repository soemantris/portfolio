# Generated by Django 4.1.6 on 2023-02-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nm_lengkap', models.CharField(max_length=70)),
                ('tmp_lahir', models.CharField(blank=True, max_length=70)),
                ('tgl_lahir', models.DateField(blank=True, null=True)),
                ('no_hp', models.IntegerField(blank=True, null=True)),
                ('alamat', models.TextField(max_length=300)),
                ('avatar', models.ImageField(blank=True, default='akun/akun_default.png', upload_to='akun/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
