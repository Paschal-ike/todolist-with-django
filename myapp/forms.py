from django  import forms
from .models import *

class TaskForm(forms.ModelForm):
#priority = forms.ChoiceField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    class Meta:
        model = Task 
        fields = ['title', 'description', 'priority', 'due_date', 'completed']
        widgets =  {
            "due_date": forms.DateInput(attrs={'type':'date'}),
        }