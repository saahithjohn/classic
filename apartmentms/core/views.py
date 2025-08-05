from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from residents.models import ResidentProfile

def home(request):
    if not request.user.is_authenticated:
        return redirect('account_login')
    return redirect('dashboard:dashboard')

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

def setup_roles_and_users():
    User = get_user_model()
    # Define roles
    roles = ['Admin', 'Owner', 'Resident', 'Staff']
    for role in roles:
        Group.objects.get_or_create(name=role)
    # Provided user data
    users_data = [
        {'name': 'Admin User', 'email': 'admin@vvs.com', 'status': 'admin', 'flat_no': None, 'mobile_no': '9642476846', 'resident_id': 'ADM001'},
        {'name': 'Somayajulu Bulusu', 'email': 'somu@vvs.com', 'status': 'owner', 'flat_no': '101', 'mobile_no': '9052990359', 'resident_id': 'RES001'},
        {'name': 'Kistapuram Sathaiah', 'email': 'ksatish@vvs.com', 'status': 'owner', 'flat_no': '102', 'mobile_no': '7396043600', 'resident_id': 'RES002'},
        {'name': 'Kumar Tatta', 'email': 'kumar@vvs.com', 'status': 'owner', 'flat_no': '201', 'mobile_no': '9265968825', 'resident_id': 'RES003'},
        {'name': 'P Vishalendra Chary', 'email': 'vishal@vvs.com', 'status': 'owner', 'flat_no': '202', 'mobile_no': '7032818032', 'resident_id': 'RES004'},
        {'name': 'P Satya Sai Sreedhar', 'email': 'sridhar@vvs.com', 'status': 'owner', 'flat_no': '301', 'mobile_no': '9908338659', 'resident_id': 'RES005'},
        {'name': 'Rupa Vemarthi', 'email': 'rupa@vvs.com', 'status': 'owner', 'flat_no': '302', 'mobile_no': '9642476846', 'resident_id': 'RES006'},
        {'name': 'T Santosh Kumar', 'email': 'santosh@vvs.com', 'status': 'owner', 'flat_no': '401', 'mobile_no': '8179294164', 'resident_id': 'RES007'},
        {'name': 'VVS Infra', 'email': 'vvsinfra@vvs.com', 'status': 'owner', 'flat_no': '402', 'mobile_no': '', 'resident_id': 'RES008'},
        {'name': 'Shyam Padala', 'email': 'shyam@vvs.com', 'status': 'owner', 'flat_no': '501', 'mobile_no': '9908095581', 'resident_id': 'RES009'},
        {'name': 'G Sai Neeharika', 'email': 'neeharika@vvs.com', 'status': 'owner', 'flat_no': '502', 'mobile_no': '9573799448', 'resident_id': 'RES010'},
    ]
    for u in users_data:
        user, created = User.objects.get_or_create(username=u['email'], defaults={
            'email': u['email'],
            'first_name': u['name'].split()[0],
            'last_name': ' '.join(u['name'].split()[1:]),
        })
        if created:
            user.set_password(u['mobile_no'] or 'password123')
            user.save()
        # Assign role
        if u['status'] == 'admin':
            group = Group.objects.get(name='Admin')
        elif u['status'] == 'owner':
            group = Group.objects.get(name='Owner')
        else:
            group = Group.objects.get(name='Resident')
        user.groups.add(group)
        # Create ResidentProfile for owners with valid flat
        if u['status'] == 'owner' and u['flat_no']:
            from flats.models import Flat
            flat = Flat.objects.filter(number=u['flat_no']).first()
            if flat:
                ResidentProfile.objects.get_or_create(
                    user=user,
                    flat=flat,
                    defaults={
                        'phone': u['mobile_no'],
                        'email': u['email'],
                        'is_owner': True,
                        'is_tenant': False,
                    }
                )
