# Generated by Django 2.2 on 2019-11-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampaper', '0009_auto_20191115_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqoption',
            name='option',
            field=models.CharField(max_length=200, verbose_name='Option for Question'),
        ),
    ]