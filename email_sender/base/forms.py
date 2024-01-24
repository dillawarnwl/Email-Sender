from django import forms

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

class ExcelEmailForm(forms.Form):
    excel_file = forms.FileField(
        label="Upload Excel File", required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
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
