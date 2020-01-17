# Generated by Django 2.2.2 on 2019-07-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyName', models.CharField(max_length=50)),
                ('propertyType', models.CharField(max_length=50)),
                ('propertyDesc', models.CharField(max_length=1000)),
                ('propertyCity', models.CharField(max_length=50)),
                ('propertyRent', models.IntegerField(default=0)),
                ('propertyOwner', models.CharField(max_length=50)),
                ('ownerContact', models.CharField(default=0, max_length=10)),
                ('image', models.ImageField(upload_to='for-sale')),
            ],
        ),
        migrations.CreateModel(
            name='forSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyName', models.CharField(max_length=50)),
                ('propertyType', models.CharField(max_length=50)),
                ('propertyDesc', models.CharField(max_length=1000)),
                ('propertyCity', models.CharField(max_length=50)),
                ('propertyPrice', models.IntegerField(default=0)),
                ('propertyOwner', models.CharField(max_length=50)),
                ('ownerContact', models.CharField(default=0, max_length=10)),
                ('image', models.ImageField(upload_to='for-sale')),
            ],
        ),
    ]