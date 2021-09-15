from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
def contactView(request):
    recepient_list= ['omidsoroush@t-online.de']
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            from_email = form.cleaned_data['email_address']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['omidsoroush@t-online.de'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "blog/base.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
