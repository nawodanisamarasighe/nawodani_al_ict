# Generated by Django 2.2 on 2019-11-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exampaper', '0010_auto_20191115_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mcqquestion',
            name='question',
            field=models.CharField(max_length=500, verbose_name='The MCQ Question'),
        ),
    ]
