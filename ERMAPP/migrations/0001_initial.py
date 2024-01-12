# Generated by Django 4.2.7 on 2023-12-03 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=100)),
                ('empid', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=20)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ERMAPP.position')),
            ],
        ),
    ]
