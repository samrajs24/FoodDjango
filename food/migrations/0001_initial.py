# Generated by Django 4.2 on 2024-02-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=200)),
                ('food_desc', models.CharField(max_length=200)),
                ('food_price', models.IntegerField()),
            ],
        ),
    ]
