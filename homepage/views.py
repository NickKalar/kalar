from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

# Sends email from form data.
def send_email(request, *args, **kwargs):

	user_name = request.GET['name']
	user_email = request.GET['email']
	user_subject = request.GET['subject']
	user_body = request.GET['emailBody']

	user_body = "Name: " + user_name + "\n\nBody:" + user_body

	if user_name and user_email and user_subject and user_body:
		try:
			print(user_name + user_email + user_subject + user_body)
			send_email(user_subject, user_body, user_email, ['kalar.noreply@gmail.com'])
		except BadHeaderError:
			print(user_name + user_email + user_subject + user_body)
			return HttpResponse("Invalid header found.")
		print(user_name + user_email + user_subject + user_body)
		return HttpResponseRedirect('home.html')
	else:
		# Form validation means we should never see this.
		return HttpResponse('Please make sure all fields are filled out.')