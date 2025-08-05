from django.shortcuts import render
from flats.models import Flat
from residents.models import ResidentProfile
from complaints.models import Complaint  # Assuming Complaint model exists
from documents.models import Notice  # Assuming Notice model exists
from core.models import Message  # Assuming Message model exists

def dashboard(request):
    flat_count = Flat.objects.count()
    member_count = ResidentProfile.objects.count()
    notice_count = Notice.objects.count()
    message_count = Message.objects.count()
    complaint_count = Complaint.objects.count()
    bill_count = 0
    usage_count = 0
    contract_count = 0
    visitor_count = 0
    bills = []
    usages = []
    contracts = []
    visitors = []
    try:
        from billing.models import Bill
        bill_count = Bill.objects.count()
        bills = Bill.objects.order_by('-created_at')[:5]
    except Exception:
        pass
    try:
        from electricity.models import ElectricityUsage
        usage_count = ElectricityUsage.objects.count()
        usages = ElectricityUsage.objects.order_by('-created_at')[:5]
    except Exception:
        pass
    try:
        from infrastructure.models import AMCContract
        contract_count = AMCContract.objects.count()
        contracts = AMCContract.objects.order_by('-start_date')[:5]
    except Exception:
        pass
    try:
        from visitors.models import VisitorLog
        visitor_count = VisitorLog.objects.count()
        visitors = VisitorLog.objects.order_by('-entry_time')[:5]
    except Exception:
        pass
    notices = Notice.objects.all()[:5]
    messages = Message.objects.all()[:5]
    complaints = Complaint.objects.all()[:5]
    members = ResidentProfile.objects.select_related('user', 'flat').all()[:5]
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
