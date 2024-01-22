import pandas as pd
from django.shortcuts import render
from django.core.mail import send_mail
# from .forms import email_form

def send_email(request):
    context = None
    return render(request, 'index.html', context)
