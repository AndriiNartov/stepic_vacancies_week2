# Generated by Django 3.2 on 2021-05-02 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('vacancies', '0009_alter_resume_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes',
                                    to='vacancies.specialty', verbose_name='Специализация'),
        ),
    ]
