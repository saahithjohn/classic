from django.shortcuts import render
from flats.models import Flat
from residents.models import ResidentProfile
from complaints.models import Complaint  # Assuming Complaint model exists
from documents.models import Notice  # Assuming Notice model exists
from core.models import Message  # Assuming Message model exists

def dashboard(request):
    user = request.user
    resident = None
    if user.is_authenticated:
        try:
            resident = ResidentProfile.objects.get(user=user)
        except ResidentProfile.DoesNotExist:
            resident = None
    # User-specific counts and lists
    flat_count = 1 if resident else 0
    member_count = 1 if resident else 0
    notice_count = Notice.objects.count()
    message_count = Message.objects.filter(recipient=resident).count() if resident else 0
    complaint_count = Complaint.objects.filter(resident=resident).count() if resident else 0
    bill_count = 0
    usage_count = 0
    contract_count = 0
    visitor_count = 0
    bills = []
    usages = []
    contracts = []
    visitors = []
    if resident:
        try:
            from billing.models import Bill
            bill_count = Bill.objects.filter(flat=resident.flat).count()
            bills = Bill.objects.filter(flat=resident.flat).order_by('-created_at')[:5]
        except Exception:
            pass
        try:
            from electricity.models import ElectricityUsage
            usage_count = ElectricityUsage.objects.filter(flat=resident.flat).count()
            usages = ElectricityUsage.objects.filter(flat=resident.flat).order_by('-created_at')[:5]
        except Exception:
            pass
        try:
            from visitors.models import VisitorLog
            visitor_count = VisitorLog.objects.filter(contact=resident.phone).count()
            visitors = VisitorLog.objects.filter(contact=resident.phone).order_by('-entry_time')[:5]
        except Exception:
            pass
    notices = Notice.objects.all()[:5]
    messages = Message.objects.filter(recipient=resident)[:5] if resident else []
    complaints = Complaint.objects.filter(resident=resident)[:5] if resident else []
    members = [resident] if resident else []
    return render(request, 'dashboard/dashboard.html', {
        'flat_count': flat_count,
        'member_count': member_count,
        'notice_count': notice_count,
        'message_count': message_count,
        'complaint_count': complaint_count,
        'bill_count': bill_count,
        'usage_count': usage_count,
        'contract_count': contract_count,
        'visitor_count': visitor_count,
        'notices': notices,
        'messages': messages,
        'complaints': complaints,
        'members': members,
        'bills': bills,
        'usages': usages,
        'contracts': contracts,
        'visitors': visitors,
    })
