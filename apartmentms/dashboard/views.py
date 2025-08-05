from django.shortcuts import render
from flats.models import Flat
from residents.models import ResidentProfile

def dashboard(request):
    flat_count = Flat.objects.count()
    resident_count = ResidentProfile.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'flat_count': flat_count,
        'resident_count': resident_count,
    })
