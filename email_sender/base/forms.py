from django import forms
from django.core.exceptions import ValidationError

class EmailQueryForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter query...'}))

class GivenEmailForm(forms.Form):
    dest_email = forms.EmailField(
        label="Reception Email",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}))
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}))
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter message...'}))

def validate_excel_file(value):
    if not value.name.endswith('.xls') and not value.name.endswith('.xlsx'):
        raise ValidationError('Please upload a valid Excel file.')
    
class ExcelEmailForm(forms.Form):
    excel_file = forms.FileField(
        label="Upload Excel File", required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        validators=[validate_excel_file])
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}))
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter message...'}))

class StringEmailForm(forms.Form):
    dest_email = forms.CharField(
        label="Enter more than 1 emails",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter comma-separated emails'}))
    subject = forms.CharField(
        label="Subject",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subject'}))
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': 'Enter message...'}))
