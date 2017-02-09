from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render,redirect
from .forms import UserLoginForm, UserRegisterForm



# Create your views here.
def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/")
	
	context = {
	"form" : form, "title" : title 
	}
	
	return render(request, "login.html" , context )


def register_view(request):
	title ="Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		# new_user = authenticate(username=user.username, password=password)
		# login(request, new_user)
		return redirect("/login")


	context = {
		"form_regiseter" : form,
		"title" : title
	}
	return render(request, "register.html" , context )



def logout_view(request):
	logout(request)
	return redirect("/")
	return render(request, "" , {} )