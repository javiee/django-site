from django import forms

class ContactForm(forms.Form):

    subject = forms.CharField(max_length=100)
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
