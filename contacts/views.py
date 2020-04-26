from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone

from django.core.files.storage import FileSystemStorage
from .forms import ContactForm


def email(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()

            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            document = request.FILES.get('document')
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            base_dir = '/media/documents/'
            email.attach_file('media/documents/'+str(document))
            email.send()
        
        else:
            return render(request,'contact_Form/contacts.html',{'form' : form})

    else:
        form = ContactForm()
        return render(request, 'contact_Form/contacts.html', {'form':form})

