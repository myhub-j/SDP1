# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
            send_mail(
                'Welcome to The Phagyul Newsletter – Embracing the Essence of Indian Culture.',

                'I hope this mail finds you well.'
                'It is with immense pleasure that we extend our warmest welcome to you as a new member of our Phagyul community. Your interest in the Indian Cultural Management System reflects a shared passion for the profound and diverse heritage that India, with its myriad hues, offers to the world.'
                'As we embark on this journey together, we invite you to explore the myriad facets of Indian culture through our newsletter. Let us celebrate the past, engage with the present, and envision a culturally vibrant future.'

                'regards'
                'Team-Phagyul',


                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            # You can add more logic here, like saving the email to a database
            return HttpResponseRedirect('cuisines/')  # Redirect to a success page
    else:
        form = NewsletterForm()
    return render(request, 'newsletter.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully')
                return render(request, 'login.html')
        else:
            messages.info(request, 'password do not match')
            return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def cuisines(request):
    return render(request, 'cuisines.html')


def dance_froms(request):
    return render(request, 'dance_froms.html')


def monuments(request):
    return render(request, 'monuments.html')


def festivals(request):
    return render(request, 'festivals.html')


def about(request):
    return render(request, 'about.html')


def faq(request):
    return render(request, 'faq.html')

def Blogs(request):
    return render(request,'blog-post.html')

def contact(request):
    return render(request,'contact.html')

# def redirect_to_cuisines(request):
#     url = reverse('cuisines')
#     return redirect(url)
#
# def redirect_to_dance_froms(request):
#     url = reverse('dance_froms')
#     return redirect(url)
#
# def redirect_to_monuments(request):
#     url = reverse('monuments')
#     return redirect(url)
#
# def redirect_to_festivals(request):
#     url = reverse('festivals')
#     return redirect(url)
