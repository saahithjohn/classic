from django.shortcuts import render, redirect, get_object_or_404
from .models import Bill
from .forms import BillForm

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'billing/bill_list.html', {'bills': bills})

def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'billing/bill_detail.html', {'bill': bill})

def bill_create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('billing:bill_list')
    else:
        form = BillForm()
    return render(request, 'billing/bill_form.html', {'form': form})

def bill_update(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('billing:bill_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'billing/bill_form.html', {'form': form})

def bill_delete(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('billing:bill_list')
    return render(request, 'billing/bill_confirm_delete.html', {'bill': bill})
