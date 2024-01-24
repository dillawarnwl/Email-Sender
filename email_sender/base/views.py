from django.core.mail import EmailMultiAlternatives, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .forms import GivenEmailForm, ExcelEmailForm, StringEmailForm
import openpyxl

def from_given_email(request):
    form = GivenEmailForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        subject = form.cleaned_data['subject']
        recipient = form.cleaned_data['dest_email']
        message = form.cleaned_data['message']

        html_content = render_to_string('content_html.html', {'message': message})

        try:
            msg = EmailMultiAlternatives(
                subject, message, 'dillawar612@gmail.com', [recipient])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            messages.success(request, "Email sent successfully!")
            return render(request, 'success.html')
        except BadHeaderError:
            return HttpResponse("Invalid header found")
    else:
        context = {'form': form}
        return render(request, 'given_email_form.html', context)



def read_excel_data(excel_file):
    workbook = openpyxl.load_workbook(excel_file)
    sheet = workbook.active

    email_addresses = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        email = row[0]
        
        if email:
            email_addresses.append(email)

    return email_addresses

def send_emails(request, email_addresses, subject, message):
    for email_address in email_addresses:
        
        html_content = render_to_string('content_html.html', {'message': message})  
        email = EmailMessage(
            subject,
            html_content,
            'dillawar612@gmail.com',  
            [email_address],
        )
        email.content_subtype = 'html'  
        email.send()

def from_excel(request):
    if request.method == 'POST':
        form = ExcelEmailForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = form.cleaned_data['excel_file']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_addresses = read_excel_data(excel_file)
            
            send_emails(request, email_addresses, subject, message)

            
            messages.success(request, 'Emails sent successfully.')

            
            return render(request, 'success.html')

    else:
        form = ExcelEmailForm()

    context = {'form': form}
    return render(request, 'excel_form.html', context)

def from_string(request):
    form = StringEmailForm(request.POST or None)
    if form.is_valid():
        email_string = form.cleaned_data['dest_email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        email_addresses = [email.strip() for email in email_string.split(',') if email.strip()]
        send_emails(request, email_addresses, subject, message)

        messages.success(request, 'Emails sent successfully.')
        return render(request, 'success.html')
    context = {'form': form}
    return render(request, 'string_form.html', context)
