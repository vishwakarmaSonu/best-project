# Generated by Django 4.0.4 on 2022-07-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]
