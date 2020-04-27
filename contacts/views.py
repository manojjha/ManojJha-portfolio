from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone

from django.core.files.storage import FileSystemStorage
from .forms import ContactForm

from django.http import HttpResponse


def email(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            email = EmailMessage(subject,message,email_from,recipient_list)
            email.send()
            return redirect('contact:contacts')

        else:
            return render(request,'contact_Form/contacts.html',{'form' : form})

    else:
        form = ContactForm()
        return render(request, 'contact_Form/contacts.html', {'form':form})


