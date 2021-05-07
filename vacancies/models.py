from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

from stepik_vacancies.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Vacancy(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    specialty = models.ForeignKey(
        'Specialty',
        on_delete=models.CASCADE,
        related_name='vacancies',
        verbose_name='Специализация'
    )
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='vacancies', verbose_name='Компания')
    skills = models.CharField(max_length=100, verbose_name='Навыки')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    salary_min = models.IntegerField(verbose_name='Минимальная зарплата')
    salary_max = models.IntegerField(verbose_name='Максимальная зарплата')
    published_at = models.DateField(auto_now=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    location = models.CharField(max_length=100, verbose_name='Город')
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, blank=True, null=True, verbose_name='Логотип')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    employee_count = models.IntegerField(verbose_name='Количество сотрудников')
    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Владелец', blank=True, null=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=100, verbose_name='Тип вакансии')
    title = models.CharField(max_length=100, verbose_name='Название')
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR, verbose_name='Логотип')

    def __str__(self):
        return self.title


class Application(models.Model):
    written_username = models.CharField(max_length=100, verbose_name='Имя')
    written_phone = models.CharField(max_length=30, verbose_name='Телефон')
    written_cover_letter = models.TextField(verbose_name='Сопроводительное письмо')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications', verbose_name='Вакансия')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='applications',
        verbose_name='Пользователь'
    )


class Resume(models.Model):
    class Status(models.TextChoices):
        NOT_IN_SEARCH = 'NIS', _('Не ищу работу')
        CONSIDERATION = 'CON', _('Рассматриваю предложения')
        IN_SEARCH = 'INS', _('Ищу работу')

    class Grade(models.TextChoices):
        INTERN = 'INT', _('Intern')
        JUNIOR = 'JR', _('Junior')
        MIDDLE = 'MID', _('Middle')
        SENIOR = 'SNR', _('Senior')
        LEAD = 'LD', _('Lead')

    status = models.CharField(max_length=3, choices=Status.choices, verbose_name='Готовность к работе')
    grade = models.CharField(max_length=3, choices=Grade.choices, verbose_name='Квалификация')
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
        related_name='resumes',
        verbose_name='Специализация'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    salary = models.IntegerField(verbose_name='Вознаграждение')
    education = models.TextField(max_length=250, verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт работы')
    portfolio = models.URLField(verbose_name='Портфолио')
