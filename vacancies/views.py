from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from vacancies.forms import ApplicationForm, CompanyForm, ResumeForm, VacancyForm
from vacancies.models import Application, Company, Resume, Specialty, Vacancy

import os


class IndexView(ListView):
    print(os.environ.get('AWS_STORAGE_BUCKET_NAME'))
    model = Specialty
    template_name = 'vacancies/index.html'
    context_object_name = 'specialties'
    query_examples_list = ['Python', 'Flask', 'Django', 'Парсинг', 'ML']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.all().prefetch_related('vacancies')
        context['companies'] = Company.objects.all().prefetch_related('vacancies')
        context['query_examples_list'] = self.query_examples_list
        return context


class AllVacanciesView(ListView):
    model = Vacancy
    template_name = 'vacancies/all_vacancies.html'

    def get_queryset(self):
        return Vacancy.objects.all().select_related('company').select_related('specialty')


class VacanciesBySpecialtyView(ListView):
    model = Vacancy
    template_name = 'vacancies/specialty_vacancies.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self
                                      .kwargs['specialty']) \
            .select_related('specialty') \
            .select_related('company')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialty_name'] = Specialty.objects.filter(code=self.kwargs['specialty'])[0].title
        return context


class CompanyDetail(DetailView):
    model = Company
    template_name = 'vacancies/company.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["back"] = self.request.META.get('HTTP_REFERER')
        context['vacancies'] = Vacancy.objects.filter(company=self.kwargs['pk']).select_related('specialty')
        return context


class VacancyDetail(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Vacancy.objects.filter(pk=self.kwargs['pk']).select_related('company').select_related('specialty')

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.vacancy = Vacancy.objects.get(pk=self.kwargs['pk'])
            if request.user.is_authenticated:
                user = request.user
                application.user = user
            application.save()
        return redirect('send', self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm
        return context


def send_vacancy_response_view(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    return render(request, 'vacancies/sent.html', {
        'vacancy': vacancy,
    })


def propose_to_create_company_view(request):
    if Company.objects.filter(owner=request.user):
        return redirect('mycompany_edit')
    return render(request, 'vacancies/company-create.html')


class MyCompanyCreateView(CreateView):
    form_class = CompanyForm
    template_name = 'vacancies/company-edit.html'

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.owner = request.user
            form.save()
        return redirect('/')


class MyCompanyEditView(LoginRequiredMixin, UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'vacancies/company-edit.html'
    success_url = '/'

    def get_object(self, queryset=None):
        try:
            obj = Company.objects.get(owner=self.request.user)
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class MyCompanyVacanciesList(ListView):
    model = Vacancy
    template_name = 'vacancies/vacancy-list.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(company__owner=self.request.user).prefetch_related('applications')


class MyCompanyVacancyCreate(CreateView):
    form_class = VacancyForm
    template_name = 'vacancies/vacancy-edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applications'] = Application.objects.filter(vacancy__company__owner=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = Company.objects.get(owner=self.request.user)
            form.save()
        return redirect('mycompany_vacancies_list')


class MyCompanyVacancyEdit(LoginRequiredMixin, UpdateView):
    model = Vacancy
    form_class = VacancyForm
    template_name = 'vacancies/vacancy-edit.html'
    pk_url_kwarg = 'pk'
    success_url = '/mycompany/vacancies'


class SearchView(ListView):
    template_name = 'vacancies/search.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        return Vacancy.objects.filter(
            Q(title__icontains=self.request.GET.get('s').strip()) |
            Q(description__icontains=self.request.GET.get('s').strip())
        ).select_related('company')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['query'] = self.request.GET.get('s')
        return context


def propose_to_create_resume_view(request):
    resume = Resume.objects.filter(user=request.user)
    if not resume:
        return render(request, 'vacancies/resume-create.html')
    return redirect('myresume_edit')


class MyResumeCreateView(CreateView):
    form_class = ResumeForm
    template_name = 'vacancies/resume-edit.html'

    def post(self, request, *args, **kwargs):
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = self.request.user
            form.save()
        return redirect('/')


class MyResumeEditView(LoginRequiredMixin, UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'vacancies/resume-edit.html'
    success_url = '/'

    def get_object(self, queryset=None):
        try:
            obj = Resume.objects.get(user=self.request.user)
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


def custom_handler404(request, exception):
    return HttpResponseNotFound('Здесь ничего нет')


def custom_handler500(request):
    return HttpResponseServerError('На сервере что-то сломалось')
