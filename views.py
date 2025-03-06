from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm

def task_list(request):
    query = request.GET.get('search', '')  # Get search query from request
    tasks = Task.objects.filter(Q(title__icontains=query)) if query else Task.objects.all() # Filter tasks by search
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'search_query': query})

def task_create(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskCreateForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Create Task'})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskUpdateForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Update Task'})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})