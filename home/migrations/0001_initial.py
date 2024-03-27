# Generated by Django 5.0.3 on 2024-03-26 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealership', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.dealership')),
            ],
            options={
                'verbose_name_plural': 'myinspections',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.dealership')),
            ],
            options={
                'verbose_name_plural': 'myinventorys',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('customer_id', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('dealership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.dealership')),
            ],
            options={
                'verbose_name_plural': 'mysales',
            },
        ),
    ]
