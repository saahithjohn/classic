from django.shortcuts import render, redirect, get_object_or_404
from .models import ElectricityUsage
from .forms import ElectricityUsageForm

def usage_list(request):
    usages = ElectricityUsage.objects.all()
    return render(request, 'electricity/usage_list.html', {'usages': usages})

def usage_detail(request, pk):
    usage = get_object_or_404(ElectricityUsage, pk=pk)
    return render(request, 'electricity/usage_detail.html', {'usage': usage})

def usage_create(request):
    if request.method == 'POST':
        form = ElectricityUsageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:usage_list')
    else:
        form = ElectricityUsageForm()
    return render(request, 'electricity/usage_form.html', {'form': form})

def usage_update(request, pk):
    usage = get_object_or_404(ElectricityUsage, pk=pk)
    if request.method == 'POST':
        form = ElectricityUsageForm(request.POST, instance=usage)
        if form.is_valid():
            form.save()
            return redirect('electricity:usage_list')
    else:
        form = ElectricityUsageForm(instance=usage)
    return render(request, 'electricity/usage_form.html', {'form': form})

def usage_delete(request, pk):
    usage = get_object_or_404(ElectricityUsage, pk=pk)
    if request.method == 'POST':
        usage.delete()
        return redirect('electricity:usage_list')
    return render(request, 'electricity/usage_confirm_delete.html', {'usage': usage})
