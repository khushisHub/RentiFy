
# Create your views here.
# Import necessary modules and models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *

# Define a view function for the home page
def home(request):
	return render(request, 'home.html')

def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	# if request.method == "POST":
	# 	username = request.POST.get('username')
	# 	password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		# if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			# messages.error(request, 'Invalid Username')
			# return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		# user = authenticate(username=username, password=password)
		
		# if user is None:
			# Display an error message if authentication fails (invalid password)
		# 	messages.error(request, "Invalid Password")
		# 	return redirect('/login/')
		# else:
			# Log in the user and redirect to the home page upon successful login
			# login(request, user)
			# return redirect('/home/')
	
	# Render the login page template (GET request)
	return render(request, 'login.html')

def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/register/')
	
	# Render the registration page template (GET request)
	return render(request, 'register.html')



def contact(request):
	return render(request, 'contact.html')

def services(request):
	return render(request, 'services.html')

def signup(request):
	# if request.method == 'POST':
	# 	Your_name = request.POST.get('Your_name')
	# 	Your_email = request.POST.get('Your_email')
	# 	Your_phone = request.POST.get('Your_phone')
	# 	username = request.POST.get('username')
	# 	password = request.POST.get('password')
		# Check if a user with the provided username already exists
		# user = User.objects.filter(username=username)
		# if user.exists():
			# Display an information message if the username is taken
			# messages.info(request, "Username already taken!")
			# return redirect('/authentication/signup/')
		# Create a new User object with the provided information
		# user = User.objects.create_user(
		# 	Your_name=Your_name,
		# 	Your_email=Your_email,
		# 	Your_phone=Your_phone,
		# 	username=username,
		# )
		
		# Set the user's password and save the user object
		# user.set_password(password)
		# user.save()
		# Display an information message indicating successful account creation
		# messages.info(request, "Account created Successfully!")
		# return redirect('/authentication/signup/')
	return render(request, 'signup.html')


def findLease(request):
	return render(request, 'findLease.html')

def findRent(request):
	return render(request, 'findRent.html')

def postLease(request):
	return render(request, 'postLease.html')

def postRent(request):
	return render(request, 'postRent.html')


