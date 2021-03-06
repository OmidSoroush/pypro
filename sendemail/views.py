from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
def contactView(request):
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

            msg_mail = str(first_name) + " " + str(from_email) + " " + str(message)
            try:
                send_mail(subject, msg_mail, from_email, ['omidsoroush022@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('sendemail:success')
    return render(request, "contact.html", {'form': form})


# Home page
class successView(TemplateView):
    template_name = 'success.html'

# Impressum page
class impressumView(TemplateView):
    template_name = 'impressum.html'
