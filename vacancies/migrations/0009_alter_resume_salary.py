# Generated by Django 3.2 on 2021-05-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0008_auto_20210501_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.IntegerField(verbose_name='Вознаграждение'),
        ),
    ]