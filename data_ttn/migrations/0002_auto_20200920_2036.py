# Generated by Django 3.1.1 on 2020-09-20 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_ttn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_ttn',
            name='badge',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data_ttn',
            name='Zone',
            field=models.CharField(choices=[('Zone 1', 'Zone 1'), ('Zone 2', 'Zone 2'), ('Zone 3', 'Zone 3')], max_length=10),
        ),
    ]