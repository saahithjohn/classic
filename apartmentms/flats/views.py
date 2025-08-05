from django.shortcuts import render, get_object_or_404, redirect
from .models import Flat
from django.contrib.auth.decorators import login_required
from .forms import FlatForm

@login_required
def flat_list(request):
    flats = Flat.objects.all()
    return render(request, 'flats/flat_list.html', {'flats': flats})

@login_required
def flat_detail(request, pk):
    flat = get_object_or_404(Flat, pk=pk)
    return render(request, 'flats/flat_detail.html', {'flat': flat})

@login_required
def flat_create(request):
    if request.method == 'POST':
        form = FlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flat_list')
    else:
        form = FlatForm()
    return render(request, 'flats/flat_form.html', {'form': form})

@login_required
def flat_update(request, pk):
    flat = get_object_or_404(Flat, pk=pk)
    if request.method == 'POST':
        form = FlatForm(request.POST, instance=flat)
        if form.is_valid():
            form.save()
            return redirect('flat_detail', pk=pk)
    else:
        form = FlatForm(instance=flat)
    return render(request, 'flats/flat_form.html', {'form': form})

@login_required
def flat_delete(request, pk):
    flat = get_object_or_404(Flat, pk=pk)
    if request.method == 'POST':
        flat.delete()
        return redirect('flat_list')
    return render(request, 'flats/flat_confirm_delete.html', {'flat': flat})
