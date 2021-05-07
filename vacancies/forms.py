from django import forms

from vacancies.models import Application, Company, Resume, Specialty, Vacancy


class CompanyForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "companyName"}
        )
    )
    logo = forms.ImageField(
        widget=forms.FileInput(
            attrs={'type': 'file', 'id': 'inputGroupFile01', 'class': 'custom-file-input'}
        )
    )
    employee_count = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "companyTeam"}
        )
    )
    location = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "companyLocation"}
        )
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'rows': "4", 'id': "companyInfo"}
        )
    )

    class Meta:
        model = Company
        fields = ['name', 'logo', 'employee_count', 'location', 'description']


class VacancyForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': 'vacancyTitle'}
        )
    )
    specialty = forms.ModelChoiceField(
        required=True,
        queryset=Specialty.objects.all().prefetch_related('vacancies').only('title'),
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2', 'id': 'userSpecialization'}),
        empty_label='Выберите специализацию'
    )
    salary_min = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "number", 'id': 'vacancySalaryMin'}
        )
    )
    salary_max = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "number", 'id': 'vacancySalaryMax'}
        )
    )
    skills = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': 'vacancySkills'}
        )
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'rows': '13', 'type': "text", 'id': 'vacancyDescription'}
        )
    )

    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'salary_min', 'salary_max', 'skills', 'description']


class ApplicationForm(forms.ModelForm):
    written_username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "userName"}
        )
    )
    written_phone = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "tel", 'id': "userPhone"}
        )
    )
    written_cover_letter = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': "form-control", 'type': "text", 'id': "userMsg", 'rows': "8"}
        )
    )

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']


class ResumeForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "userName"}
        )
    )
    surname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "userSurname"}
        )
    )
    salary = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "number", 'id': "userPortfolio"}
        )
    )
    education = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': "form-control text-uppercase",
                   'type': "text",
                   'rows': '4',
                   'style': 'color:#000;',
                   'id': "userEducation"
                   }
        )
    )
    experience = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': "form-control",
                   'type': "text",
                   'rows': '4',
                   'style': 'color:#000;',
                   'id': "userExperience"
                   }
        )
    )
    portfolio = forms.URLField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': "form-control", 'type': "text", 'id': "userPortfolio"}
        )
    )
    specialty = forms.ModelChoiceField(
        required=True,
        queryset=Specialty.objects.all().prefetch_related('resumes'),
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2', 'id': 'userSpecialization'}),
        empty_label='Выберите специализацию'
    )
    status = forms.ChoiceField(
        required=True,
        choices=Resume.Status.choices,
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2', 'id': 'userReady'}
        )
    )
    grade = forms.ChoiceField(
        required=True,
        choices=Resume.Grade.choices,
        widget=forms.Select(
            attrs={'class': 'custom-select mr-sm-2', 'id': 'userQualification'}
        )
    )

    class Meta:
        model = Resume
        exclude = ['user']
