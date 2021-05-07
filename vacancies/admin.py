from django.contrib import admin

from .models import Application, Company, Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    model = Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    model = Application
