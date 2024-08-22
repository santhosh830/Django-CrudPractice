# Generated by Django 5.1 on 2024-08-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('employee_id', models.IntegerField(max_length=8)),
                ('email', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=3)),
            ],
        ),
    ]
