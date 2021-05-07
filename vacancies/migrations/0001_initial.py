# Generated by Django 3.2 on 2021-04-28 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='company_images')),
                ('description', models.TextField(max_length=100)),
                ('employee_count', models.IntegerField()),
                ('owner',
                 models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='speciality_images')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('salary_min', models.IntegerField()),
                ('salary_max', models.IntegerField()),
                ('published_at', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                              to='vacancies.company')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                                to='vacancies.specialty')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(
                    choices=[('NIS', 'Не ищу работу'), ('CON', 'Рассматриваю предложения'), ('INS', 'Ищу работу')],
                    max_length=3)),
                ('grade', models.CharField(
                    choices=[('INT', 'Intern'), ('JR', 'Junior'), ('MID', 'Middle'), ('SNR', 'Senior'), ('LD', 'Lead')],
                    max_length=3)),
                ('specialty', models.PositiveSmallIntegerField(
                    choices=[(1, 'Фронтенд'), (2, 'Бэкенд'), (3, 'Геймдев'), (4, 'Девопс'), (5, 'Дизайн'),
                             (6, 'Продукты'), (7, 'Менеджмент')])),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=20)),
                ('education', models.CharField(max_length=250)),
                ('experience', models.TextField()),
                ('portfolio', models.URLField()),
                (
                    'user',
                    models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Aplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_username', models.CharField(max_length=100)),
                ('written_phone', models.CharField(max_length=30)),
                ('written_cover_letter', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications',
                                           to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications',
                                              to='vacancies.vacancy')),
            ],
        ),
    ]
