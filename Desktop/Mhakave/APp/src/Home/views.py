from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import FeedbackForm,SignUpForm

# Create your views here.
import datetime
def Home(request):
	title = "Welcome"
	now = datetime.datetime.now()
	
	form = SignUpForm(request.POST or None)
	context = {
		"title" : title,
		"form" : form,
		"now" : now
		
	}
	if form.is_valid():
		form.save()
		
		if(user.is_authenticated):
			context ={

			"title":"Thanks",
			"now" : now
			

			}
	
	return render(request, "Home.html", context)


def Feedback(request):
	feedback_form = FeedbackForm(request.POST or None)
	if feedback_form.is_valid():
		form_email = feedback_form.cleaned_data.get("email")
		form_message = feedback_form.cleaned_data.get("message")
		form_full_name = feedback_form.cleaned_data.get("full_name")
		form_mob_num = feedback_form.cleaned_data.get("number")


		subject = 'Site Contact Form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'indrajitnarvekar@gmail.com']
		raw_html_message = '''
		<h1>hello Admin</h1>
		'''

		contact_message = '''
				
			%s : %s from %s
		'''%(form_full_name, form_message, form_email)
		send_mail(subject,contact_message, from_email, to_email, fail_silently=False)
	context = {
	"contact_form" : feedback_form,
	}
	return render(request,"forms.html",context)

def Contact(request):
	return render(request,"contact.html",{})

