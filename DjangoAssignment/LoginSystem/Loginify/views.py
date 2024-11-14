from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserDetails
from django.contrib import messages

def hello_world(request):
    return HttpResponse("Hello, world!")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
        else:
            UserDetails.objects.create(username=username, email=email, password=password)
            messages.success(request, "Signup successful!")
            return redirect('login')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email and password:  # Check that both fields are provided
            try:
                user = UserDetails.objects.get(email=email, password=password)
                messages.success(request, "Login successful!")
                return render(request, 'success.html', {'user': user})
            except UserDetails.DoesNotExist:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Both email and password are required.")
    return render(request, 'login.html')


def get_all_users(request):
    users = UserDetails.objects.all()
    return render(request, 'all_users.html', {'users': users})

def get_user(request, email):
    user = UserDetails.objects.get(email=email)
    return render(request, 'user_detail.html', {'user': user})

def update_user(request, email):
    user = UserDetails.objects.get(email=email)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('all_users')
    return render(request, 'update_user.html', {'user': user})

def delete_user(request, email):
    user = UserDetails.objects.get(email=email)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('all_users')
