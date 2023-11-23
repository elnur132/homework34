from django import forms
from .models import Habit, Task

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'death_line', 'completed']        
