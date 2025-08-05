from django.shortcuts import render, redirect, get_object_or_404
from .models import AMCContract
from .forms import AMCContractForm

def contract_list(request):
    contracts = AMCContract.objects.all()
    return render(request, 'infrastructure/contract_list.html', {'contracts': contracts})

def contract_detail(request, pk):
    contract = get_object_or_404(AMCContract, pk=pk)
    return render(request, 'infrastructure/contract_detail.html', {'contract': contract})

def contract_create(request):
    if request.method == 'POST':
        form = AMCContractForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('infrastructure:contract_list')
    else:
        form = AMCContractForm()
    return render(request, 'infrastructure/contract_form.html', {'form': form})

def contract_update(request, pk):
    contract = get_object_or_404(AMCContract, pk=pk)
    if request.method == 'POST':
        form = AMCContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('infrastructure:contract_list')
    else:
        form = AMCContractForm(instance=contract)
    return render(request, 'infrastructure/contract_form.html', {'form': form})

def contract_delete(request, pk):
    contract = get_object_or_404(AMCContract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        return redirect('infrastructure:contract_list')
    return render(request, 'infrastructure/contract_confirm_delete.html', {'contract': contract})
