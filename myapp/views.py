from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'task_list.html', context)

def task_details(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {'task':task}
    return render(request, 'task_details.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print("Submitted form data:", request.POST)
        if form.is_valid():
            form.save()
            print("Form is valid. Redirecting...")
            return redirect('task_list')
        else:
            print("Form is not valid. Debug form errors:", form.errors)
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'task_create.html', context)


def task_update(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'task_update.html', context)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')