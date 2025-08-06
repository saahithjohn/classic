from django.shortcuts import render, get_object_or_404, redirect
from .models import Complaint
from django.contrib.auth.decorators import login_required
from .forms import ComplaintForm

@login_required
def complaint_list(request):
    complaints = Complaint.objects.select_related('resident').all()
    return render(request, 'complaints/complaint_list.html', {'complaints': complaints})

@login_required
def complaint_detail(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    return render(request, 'complaints/complaint_detail.html', {'complaint': complaint})

@login_required
def complaint_create(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('complaints:complaint_list')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/complaint_form.html', {'form': form})

@login_required
def complaint_update(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    if request.method == 'POST':
        form = ComplaintForm(request.POST, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('complaint_detail', pk=pk)
    else:
        form = ComplaintForm(instance=complaint)
    return render(request, 'complaints/complaint_form.html', {'form': form})

@login_required
def complaint_delete(request, pk):
    complaint = get_object_or_404(Complaint, pk=pk)
    if request.method == 'POST':
        complaint.delete()
        return redirect('complaint_list')
    return render(request, 'complaints/complaint_confirm_delete.html', {'complaint': complaint})
