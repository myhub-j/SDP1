from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import NewsletterForm
from django.urls import reverse


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                send_mail(
                    'Thanks for subscribing!',
                    'You have successfully subscribed to our newsletter.',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

            except Exception as e:
                print("Error occured: ", e)

            # You can add more logic here, like saving the email to a database
            return HttpResponseRedirect('cuisines/')  # Redirect to a success page
    else:
        form = NewsletterForm()
    return render(request, 'newsletter.html', {'form': form})


def index(request):
    # Logic to fetch data about cuisines
    # cuisines_data = [...]  # Example data
    return render(request, 'cuisines/index.html')
