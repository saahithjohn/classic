from django.shortcuts import render, get_object_or_404, redirect
from .models import ResidentProfile
from django.contrib.auth.decorators import login_required
from .forms import ResidentProfileForm

@login_required
def resident_list(request):
    residents = ResidentProfile.objects.select_related('user', 'flat').all()
    return render(request, 'residents/resident_list.html', {'residents': residents})

@login_required
def resident_detail(request, pk):
    resident = get_object_or_404(ResidentProfile, pk=pk)
    return render(request, 'residents/resident_detail.html', {'resident': resident})

@login_required
def resident_create(request):
    if request.method == 'POST':
        form = ResidentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resident_list')
    else:
        form = ResidentProfileForm()
    return render(request, 'residents/resident_form.html', {'form': form})

@login_required
def resident_update(request, pk):
    resident = get_object_or_404(ResidentProfile, pk=pk)
    if request.method == 'POST':
        form = ResidentProfileForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('resident_detail', pk=pk)
    else:
        form = ResidentProfileForm(instance=resident)
    return render(request, 'residents/resident_form.html', {'form': form})

@login_required
def resident_delete(request, pk):
    resident = get_object_or_404(ResidentProfile, pk=pk)
    if request.method == 'POST':
        resident.delete()
        return redirect('resident_list')
    return render(request, 'residents/resident_confirm_delete.html', {'resident': resident})
