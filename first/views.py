from django.shortcuts import render, get_object_or_404, redirect
from .models import List
from .forms import ListForm
# Create your views here.
def home(request):
    tasks = List.objects.all()
    return render(request, 'first/home.html',{'tasks':tasks})

# Note: Ensure that the 'first/home.html' template exists in your templates directory.

def addTask(request):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = ListForm()

    return render(request, "first/addTask.html", {'form':form})


def delete(request, id):
    task = get_object_or_404(List, pk=id)
    task = get_object_or_404(List, pk=id)
    if request.method == "GET":
        task = List.objects.get(pk=id)
        return render(request, "first/delete.html", {'task': task})
    if request.method == "POST":
        
        task.delete()
        return redirect('home')
        
    return redirect('home')

def update(request, id):
    task = get_object_or_404(List, pk=id)
    if request.method == "POST":
        form = ListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ListForm(instance=task)
    return render(request, "first/update.html", {'form':form})