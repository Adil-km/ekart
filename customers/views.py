from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Customer
# Create your views here.

def show_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            
            user = User.objects.create( 
                username=username,
                password=password,
                email=email
                )
            customer = Customer.objects.create(
                user= user,
                address=address,
                phone=phone
            )
            return redirect('home')
        except Exception as e:
            error_message= 'Duplicate username or invalid credentials'
            messages.error(request,error_message)
    return render(request,'account.html')