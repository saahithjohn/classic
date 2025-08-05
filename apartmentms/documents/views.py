from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice
from django.contrib.auth.decorators import login_required
from .forms import NoticeForm

@login_required
def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'documents/notice_list.html', {'notices': notices})

@login_required
def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(request, 'documents/notice_detail.html', {'notice': notice})

@login_required
def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notice_list')
    else:
        form = NoticeForm()
    return render(request, 'documents/notice_form.html', {'form': form})

@login_required
def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            return redirect('notice_detail', pk=pk)
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'documents/notice_form.html', {'form': form})

@login_required
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        notice.delete()
        return redirect('notice_list')
    return render(request, 'documents/notice_confirm_delete.html', {'notice': notice})
