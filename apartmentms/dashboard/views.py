from django.shortcuts import render
from flats.models import Flat
from residents.models import ResidentProfile
from complaints.models import Complaint  # Assuming Complaint model exists
from documents.models import Notice  # Assuming Notice model exists
from core.models import Message  # Assuming Message model exists

def dashboard(request):
    flat_count = Flat.objects.count()
    member_count = ResidentProfile.objects.count()
    notice_count = Notice.objects.count() if 'documents' in globals() else 0
    message_count = Message.objects.count() if 'core' in globals() else 0
    complaint_count = Complaint.objects.count() if 'complaints' in globals() else 0
    notices = Notice.objects.all()[:5] if 'documents' in globals() else []
    messages = Message.objects.all()[:5] if 'core' in globals() else []
    complaints = Complaint.objects.all()[:5] if 'complaints' in globals() else []
    members = ResidentProfile.objects.select_related('user', 'flat').all()[:5]
    return render(request, 'dashboard/dashboard.html', {
        'flat_count': flat_count,
        'member_count': member_count,
        'notice_count': notice_count,
        'message_count': message_count,
        'complaint_count': complaint_count,
        'notices': notices,
        'messages': messages,
        'complaints': complaints,
        'members': members,
    })
