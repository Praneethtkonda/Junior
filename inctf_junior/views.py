# Views.py
from django.shortcuts import redirect
from django.views.generic.edit import FormView

from django.core.mail import send_mail
from django.core.mail.message import BadHeaderError
from django.http.response import HttpResponse

from inctf_junior import settings
from inctf_junior.forms import ContactForm


def anonymous_required(func):
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL )
        if request.user.is_authenticated():
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view


class ContactFormView(FormView):
    template_name = 'contact_form/contact_form.html'
    success_url = '/contact/success/'
    form_class = ContactForm
    
    def form_valid(self, form):
        message = "{name} <{email}> said: " \
            .format(name=form.cleaned_data.get('name'), email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('body'))
        subject = '[InCTF Junior][Contact Us] ' + form.cleaned_data.get('subject').strip()
        recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]
        from_email = settings.DEFAULT_FROM_EMAIL
        try: send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        except BadHeaderError: return HttpResponse('Invalid header found.')
        return super(ContactFormView, self).form_valid(form)