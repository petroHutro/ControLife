from django.conf import settings
from .models import Task, TaskList, Purpose
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'time']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите'
            }),
            'time': forms.DateTimeInput(attrs={
                'id': "timepkr",
                'style': "width:100px;float:left;",
                'class': "form-control",
                'placeholder': "HH:MM",
            })
        }


class ListAdd(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = TaskList
        task = forms.ModelChoiceField(queryset=Task.objects.all(), to_field_name="id")
        fields = ['data', 'task']
        widgets = {
            'data': forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'required': 'required'})
        }


class PurposeForm(forms.ModelForm):
    planed = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y %H:%M'), input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = Purpose
        task = forms.ModelChoiceField(queryset=Task.objects.all(), to_field_name="id")
        fields = ['name', 'task', 'planed']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите'
            }),
            'plan': forms.DateTimeInput(attrs={
                'id': "timepkr",
                'style': "width:100px;float:left;",
                'class': "form-control",
                'placeholder': "DD-MM-YYYY HH:MM",
            })
        }
