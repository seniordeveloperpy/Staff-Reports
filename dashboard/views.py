from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models


@login_required(login_url='dashboard:log_in')
def index(request):
    """Main section of admin"""
    user = User.objects.count()
    users = User.objects.all()
    staff = models.Staff.objects.count()
    context = {
        'user':user,
        'users':users,
        'staff':staff
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='dashboard:log_in')
def edit_profile(request, id):
    """User profile edit"""
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return redirect('dashboard:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')

        if password:
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password != confirm_password:
                pass
            else:
                user.set_password(new_password)

        user.username = username
        user.firstname = firstname
        user.surname = surname
        user.save()

        return redirect('dashboard:index')
    return render(request, 'dashboard/profile.html', {'user': user})



#Staff
def create_staff(request):
    """Add staff"""
    if request.method=="POST":
        firstname=request.POST['firstname']
        surname=request.POST['surname']
        models.Staff.objects.create(firstname=firstname, surname=surname)
    return render(request, 'dashboard/staff/create.html')


def list_staff(request):
    """List of staff"""
    staff = models.Staff.objects.all()
    context = {
        'staff':staff,
    }
    return render(request, 'dashboard/staff/list.html', context)


def update_staff(request, id):
    """Edit staff profile"""
    staff = models.Staff.objects.get(id=id)
    if request.method =='POST':
        staff.firstname=request.POST['firstname']
        staff.surname=request.POST['surname']
        staff.save()
        return redirect('dashboard:list_staff')
    return render(request, 'dashboard/staff/update.html')

        

def delete_staff(request, id):
    """Delete staff"""
    models.Staff.objects.get(id=id).delete()
    return redirect('dashboard:list_staff')




def list_attendance(request):
    """Group of reports"""
    attendance = models.Attendance.objects.all()
    context = {
        'attendance':attendance,
    }
    return render(request, 'dashboard/attendance/list.html', context)





def log_in(request):
    """Login"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
    return render(request, 'auth/login.html')


def log_out(request):
    logout(request)
    """Logout"""
    return redirect('dashboard:index')


   



