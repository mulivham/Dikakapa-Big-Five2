from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.core.mail import EmailMessage

from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.core.mail import send_mail,send_mass_mail
from django.http import HttpResponse
#from .models import email
from django.core.mail import EmailMultiAlternatives


def home(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        first_email = request.POST['first_email']
        first_number = request.POST['first_number']
        first_message = request.POST['first_message']

        message_html = render_to_string('message.html', {
            'first_name': first_name,
            'first_email': first_email,
            'first_number':first_number,
             'first_message': first_message
             })

        plain_message = strip_tags(message_html)


        email=EmailMultiAlternatives(

            first_name,
            first_email,
            settings.EMAIL_HOST_USER,
            ['africaviewfacts@gmail.com']

            )

        email.attach_alternative (message_html,'text/html')
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'

        email.send()

        print("message sent")

        return render(request,'contact.html',{'first_name': first_name})
    else:
        return render(request,'home.html')

def about(request):
	return render(request, 'about.html',{})


def service(request):
	return render(request, 'service.html',{})

def guard(request):
	return render(request, 'guard.html',{})

def contact(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        first_email = request.POST['first_email']
        first_number = request.POST['first_number']
        first_message = request.POST['first_message']

        message_html = render_to_string('message.html', {
            'first_name': first_name,
            'first_email': first_email,
            'first_number':first_number,
             'first_message': first_message
             })

        plain_message = strip_tags(message_html)


        email=EmailMultiAlternatives(

            first_name,
            first_email,
            settings.EMAIL_HOST_USER,
            ['africaviewfacts@gmail.com']

            )

        email.attach_alternative (message_html,'text/html')
        email.content_subtype = 'html'
        email.mixed_subtype = 'related'

        email.send()

        print("message sent")

        return render(request,'contact.html',{'first_name': first_name})
    else:
        return render(request,'contact.html')

