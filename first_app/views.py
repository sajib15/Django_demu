from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def index(request):
    My_Dict ={'insert_me': " Hello I am from views.py"}
    return render(request,'index.html', context=My_Dict)

# Create your views here.
# Sample device data
devices = [
    {'name': 'Router', 'ip_address': '192.168.1.1', 'details': 'Main gateway'},
    {'name': 'Server', 'ip_address': '192.168.1.10', 'details': 'Web server'},
    {'name': 'Printer', 'ip_address': '192.168.1.20', 'details': 'Office printer'}
]

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'form': 'Invalid login credentials.'})
    return render(request, 'login.html')

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html', {'devices': devices, 'username': user.username})
    # return render(request, 'dashboard.html', {'devices': devices})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
