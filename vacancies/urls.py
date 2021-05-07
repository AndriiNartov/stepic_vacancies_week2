from django.urls import path

from .views import \
    AllVacanciesView, CompanyDetail, IndexView, MyCompanyCreateView,  MyCompanyEditView,\
    MyCompanyVacanciesList, MyCompanyVacancyCreate, MyCompanyVacancyEdit, MyResumeCreateView, MyResumeEditView, \
    send_vacancy_response_view, SearchView, propose_to_create_company_view, propose_to_create_resume_view, \
    VacancyDetail, VacanciesBySpecialtyView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vacancies', AllVacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<slug:specialty>', VacanciesBySpecialtyView.as_view(), name='vacancies_by_specialty'),
    path('companies/<int:pk>', CompanyDetail.as_view(), name='companies'),
    path('vacancies/<int:pk>', VacancyDetail.as_view(), name='vacancy'),
    path('vacancies/<int:pk>/send', send_vacancy_response_view, name='send'),
    path('mycompany/letsstart', propose_to_create_company_view, name='propose_mycompany_create'),
    path('mycompany/create', MyCompanyCreateView.as_view(), name='mycompany_create'),
    path('mycompany', MyCompanyEditView.as_view(), name='mycompany_edit'),
    path('mycompany/vacancies', MyCompanyVacanciesList.as_view(), name='mycompany_vacancies_list'),
    path('mycompany/vacancies/create', MyCompanyVacancyCreate.as_view(), name='mycompany_vacancy_create'),
    path('mycompany/vacancies/<int:pk>', MyCompanyVacancyEdit.as_view(), name='mycompany_vacancy_edit'),
    path('search/', SearchView.as_view(), name='search'),
    path('myresume/letsstart', propose_to_create_resume_view, name='propose_myresume_create'),
    path('myresume/create', MyResumeCreateView.as_view(), name='myresume_create'),
    path('myresume', MyResumeEditView.as_view(), name='myresume_edit'),

]
