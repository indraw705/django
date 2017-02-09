from django import forms
from .models import SignUp
from phonenumber_field.modelfields import PhoneNumberField



class FeedbackForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField(required=True,
        widget=forms.Textarea)
	number = PhoneNumberField()



	
class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']
#custome validation		
	# def clean_email(self):
	# 	print self.cleaned_data.get('email')
	# 	return "abc@gmail.com"

