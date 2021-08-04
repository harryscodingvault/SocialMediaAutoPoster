from django.shortcuts import render
from .models import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

from var.my_var import *


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_form = ContactForm(name=name, email=email, subject=subject, message=message)
        contact_form.save()

        #Send Email
        mail_subject = subject
        message = f"Name: {name}\n Email: {email}\n Message: {message}"
        to_email = EMAIL_TO
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()
        messages.success(request, 'Message submitted')
    return render(request, 'Index/contact.html')
