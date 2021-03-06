# Generated by Django 2.2.2 on 2019-07-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestateHome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyName', models.CharField(max_length=50)),
                ('propertyType', models.CharField(max_length=50)),
                ('propertyDesc', models.CharField(max_length=1000)),
                ('propertyCity', models.CharField(max_length=50)),
                ('propertyOwner', models.CharField(max_length=50)),
                ('businessType', models.CharField(max_length=50)),
                ('ownerContact', models.CharField(default=0, max_length=10)),
                ('image', models.ImageField(upload_to='to-sell')),
            ],
        ),
    ]
