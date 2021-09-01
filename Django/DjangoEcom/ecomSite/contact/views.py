from django.shortcuts import render
from .models import ContactModel, About
from django.contrib import messages
from django.core.mail import EmailMessage

from my_vars.vars import *


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_form = ContactModel(name=name, email=email, subject=subject, message=message)
        contact_form.save()

        #Send Email
        mail_subject = subject
        message = f"Name: {name}\n Email: {email}\n Message: {message}"
        to_email = EMAIL_TO
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        messages.success(request, 'Message submitted')
    return render(request, 'index/contact.html')



def about(request):
    about_data = About.objects.all()[0]
    context = {
        'about': about_data,
    }
    return render(request, 'index/about.html', context)