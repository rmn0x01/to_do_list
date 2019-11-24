from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        #fields = '__all__'
        exclude = ['author']

        widgets = {
            'deadline' : forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'})
        }