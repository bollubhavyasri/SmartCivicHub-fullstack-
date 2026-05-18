from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Organization, UserProfile, Complaint

from django.db.models import Count

# 🏠 HOME
def home(request):
    return render(request, 'home.html')


# 🟢 MAIN PAGE
@login_required(login_url='login')
def mainpage(request):
    return render(request, 'mainpage.html')


# 📝 REGISTER (MISSING FIXED)
def register(request):
    orgs = Organization.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        org_id = request.POST.get('organization')
        role = request.POST.get('role')

        user = User.objects.create_user(username=username, password=password)
        org = Organization.objects.get(id=org_id)

        UserProfile.objects.create(user=user, organization=org, role=role)

        return redirect('login')

    return render(request, 'register.html', {'orgs': orgs})


# 🔐 LOGIN
def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:
            login(request, user)

            try:
                profile = UserProfile.objects.get(user=user)

                if profile.role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    return redirect('mainpage')

            except UserProfile.DoesNotExist:
                return redirect('mainpage')

        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# 👤 DASHBOARD (MISSING FIXED)
@login_required(login_url='login')
def dashboard(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'complaints': complaints})

# ➕ SUBMIT COMPLAINT
@login_required(login_url='login')
def submit_complaint(request):
    orgs = Organization.objects.all()

    if request.method == 'POST':
        Complaint.objects.create(
            user=request.user,
            organization=Organization.objects.get(id=request.POST['organization']),
            title=request.POST['title'],
            description=request.POST['description'],
            category=request.POST['category'],
            image=request.FILES.get('image')
        )
        return redirect('dashboard')

    return render(request, 'submit.html', {'orgs': orgs})


# 🛠️ ADMIN DASHBOARD (MISSING FIXED)
@login_required(login_url='login')
def admin_dashboard(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'admin':
        return redirect('dashboard')

    complaints = Complaint.objects.filter(organization=profile.organization)

    # 📊 Analytics data
    total = complaints.count()
    pending = complaints.filter(status="pending").count()
    in_progress = complaints.filter(status="in_progress").count()
    resolved = complaints.filter(status="resolved").count()

    context = {
        'complaints': complaints,
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'resolved': resolved,
    }

    return render(request, 'admin_dashboard.html', context)

# 🔄 UPDATE STATUS (MISSING FIXED)
@login_required(login_url='login')
def update_status(request, id):
    complaint = get_object_or_404(Complaint, id=id)

    if request.method == 'POST':
        complaint.status = request.POST.get('status')
        complaint.save()

    return redirect('admin_dashboard')

