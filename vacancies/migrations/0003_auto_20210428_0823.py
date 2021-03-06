# Generated by Django 3.2 on 2021-04-28 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0002_rename_aplication_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications',
                                    to='vacancies.vacancy', verbose_name='Вакансия'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_cover_letter',
            field=models.TextField(verbose_name='Сопроводительное письмо'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=models.CharField(max_length=30, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_username',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.IntegerField(verbose_name='Количество сотрудников'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(upload_to='company_images', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE,
                                       to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.CharField(max_length=250, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.TextField(verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.CharField(
                choices=[('INT', 'Intern'), ('JR', 'Junior'), ('MID', 'Middle'), ('SNR', 'Senior'), ('LD', 'Lead')],
                max_length=3, verbose_name='Квалификация'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='portfolio',
            field=models.URLField(verbose_name='Портфолио'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.CharField(max_length=20, verbose_name='Вознаграждение'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.PositiveSmallIntegerField(
                choices=[(1, 'Фронтенд'), (2, 'Бэкенд'), (3, 'Геймдев'), (4, 'Девопс'), (5, 'Дизайн'), (6, 'Продукты'),
                         (7, 'Менеджмент')], verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.CharField(
                choices=[('NIS', 'Не ищу работу'), ('CON', 'Рассматриваю предложения'), ('INS', 'Ищу работу')],
                max_length=3, verbose_name='Готовность к работе'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='surname',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                       verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.CharField(max_length=100, verbose_name='Тип вакансии'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='speciality_images', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                    to='vacancies.company', verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(max_length=100, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(verbose_name='Максимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(verbose_name='Минимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.CharField(max_length=100, verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies',
                                    to='vacancies.specialty', verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
