# Generated by Django 4.1.1 on 2022-09-28 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=10, max_digits=19)),
                ('amount', models.IntegerField()),
                ('discount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('code', models.IntegerField()),
                ('fk_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.category')),
            ],
        ),
    ]
