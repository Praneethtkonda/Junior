from django import forms
from captcha.fields import ReCaptchaField

captcha_attrs = {'theme': 'clean', 'size': 'compact'}


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}), 
                           required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email'}), 
                            required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject'}), 
                              required=True)
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message Body'}))
    captcha = ReCaptchaField(attrs=captcha_attrs, required=True)