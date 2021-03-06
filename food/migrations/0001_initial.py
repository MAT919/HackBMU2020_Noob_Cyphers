# Generated by Django 3.0.2 on 2020-02-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('headimg', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('img4', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='GravityRev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.TextField()),
                ('revowner1', models.CharField(max_length=100)),
                ('revowner2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='KarimRev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.TextField()),
                ('revowner1', models.CharField(max_length=100)),
                ('revowner2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MilkbarRev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.TextField()),
                ('revowner1', models.CharField(max_length=100)),
                ('revowner2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantsAgra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='RestaurantsDelhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='SorrentoRev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rev', models.TextField()),
                ('revowner1', models.CharField(max_length=100)),
                ('revowner2', models.CharField(max_length=100)),
            ],
        ),
    ]
