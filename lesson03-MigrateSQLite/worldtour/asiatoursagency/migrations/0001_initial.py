# Generated by Django 5.1.2 on 2024-11-14 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_country', models.CharField(max_length=64)),
                ('destination_country', models.CharField(max_length=64)),
                ('number_of_nights', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
    ]
