# Generated by Django 4.2.3 on 2023-07-17 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.FloatField(max_length=5)),
                ('size', models.TextField()),
                ('color', models.TextField()),
            ],
        ),
    ]
