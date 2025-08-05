from django.shortcuts import render, redirect, get_object_or_404
from .models import VisitorLog
from .forms import VisitorLogForm

def visitor_list(request):
    visitors = VisitorLog.objects.all()
    return render(request, 'visitors/visitor_list.html', {'visitors': visitors})

def visitor_detail(request, pk):
    visitor = get_object_or_404(VisitorLog, pk=pk)
    return render(request, 'visitors/visitor_detail.html', {'visitor': visitor})

def visitor_create(request):
    if request.method == 'POST':
        form = VisitorLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors:visitor_list')
    else:
        form = VisitorLogForm()
    return render(request, 'visitors/visitor_form.html', {'form': form})

def visitor_update(request, pk):
    visitor = get_object_or_404(VisitorLog, pk=pk)
    if request.method == 'POST':
        form = VisitorLogForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitors:visitor_list')
    else:
        form = VisitorLogForm(instance=visitor)
    return render(request, 'visitors/visitor_form.html', {'form': form})

def visitor_delete(request, pk):
    visitor = get_object_or_404(VisitorLog, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('visitors:visitor_list')
    return render(request, 'visitors/visitor_confirm_delete.html', {'visitor': visitor})
