from django.shortcuts import render
from market.models import Register
from django.contrib import messages

# Create your views here.

def home(request):
	context = {}
	return render(request, 'home.html', context)

def cart(request):
	context = {}
	return render(request, 'cart.html', context)

def buy(request):
	context = {}
	return render(request, 'buy.html', context)

def register(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		password = request.POST.get('password')

		acc = Register(name = name, email=email, phone=phone, password=password)
		acc.save()
		messages.success(request, 'Your account has been created!')

	return render(request, 'register.html')