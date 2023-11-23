from django.shortcuts import render, redirect
from django.views import View
from .models import Habit, Task
from .forms import HabitForm, TaskForm

class HabitListView(View):
    def get(self, request):
        habits = Habit.objects.all()
        return render(request, 'habit_list.html', {'habits': habits})

class HabitCreateView(View):
    def get(self, request):
        form = HabitForm()
        return render(request, 'habit_form.html', {'form': form})

    def post(self, request):
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('habit-list')
        return render(request, 'habit_form.html', {'form': form})

class HabitUpdateView(View):
    def get(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id)
        form = HabitForm(instance=habit)
        return render(request, 'habit_form.html', {'form': form})

    def post(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id)
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit-list')
        return render(request, 'habit_form.html', {'form': form})

class HabitDeleteView(View):
    def post(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id)
        habit.delete()
        return redirect('habit-list')

class TaskListView(View):
    def get(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id)
        tasks = Task.objects.filter(habit=habit)
        return render(request, 'task_list.html', {'habit': habit, 'tasks': tasks})

class TaskCreateView(View):
    def get(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id)
        form = TaskForm()
        return render(request, 'task_form.html', {'habit': habit, 'form': form})

    def post(self, request, habit_id):
        habit = Habit.objects.get(id=habit_id)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.habit = habit
            task.save()
            return redirect('task-list', habit_id=habit_id)
        return render(request, 'task_form.html', {'habit': habit, 'form': form})

class TaskUpdateView(View):
    def get(self, request, habit_id, task_id):
        habit = Habit.objects.get(id=habit_id)
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'task_form.html', {'habit': habit, 'form': form})

    def post(self, request, habit_id, task_id):
        habit = Habit.objects.get(id=habit_id)
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list', habit_id=habit_id)
        return render(request, 'task_form.html', {'habit': habit, 'form': form})

class TaskDeleteView(View):
    def post(self, request, habit_id, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('task-list', habit_id=habit_id)
    



    


