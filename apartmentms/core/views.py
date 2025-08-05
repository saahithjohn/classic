from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

def home(request):
    return render(request, 'core/home.html')

@login_required
def message_list(request):
    messages = Message.objects.all()
    return render(request, 'core/message_list.html', {'messages': messages})

@login_required
def message_detail(request, pk):
    message = get_object_or_404(Message, pk=pk)
    return render(request, 'core/message_detail.html', {'message': message})

@login_required
def message_create(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:message_list')
    else:
        form = MessageForm()
    return render(request, 'core/message_form.html', {'form': form})

@login_required
def message_update(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('core:message_detail', pk=pk)
    else:
        form = MessageForm(instance=message)
    return render(request, 'core/message_form.html', {'form': form})

@login_required
def message_delete(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == 'POST':
        message.delete()
        return redirect('core:message_list')
    return render(request, 'core/message_confirm_delete.html', {'message': message})
