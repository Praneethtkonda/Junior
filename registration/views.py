from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView

from braces.views import LoginRequiredMixin, AnonymousRequiredMixin

from registration.forms import StudentRegistrationForm, TeamRegistrationForm, student_fields
from registration.models import Student


class CurrentUserMixin(object):
    model = Student

    def get_object(self, *args, **kwargs):
        try: obj = super(CurrentUserMixin, self).get_object(*args, **kwargs)
        except AttributeError: obj = self.request.user
        return obj


class StudentRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register/user/register.html"
    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = StudentRegistrationForm
    success_url = '/register/user/success/'
    
    def form_valid(self, form): 
        form.save()
        return FormView.form_valid(self, form)
    
    
class TeamRegistrationView(LoginRequiredMixin, FormView):
    template_name = "register/team/register.html"
    form_class = TeamRegistrationForm
    success_url = '/register/team/success/'
    
    def form_valid(self, form):
        form.save(commit=True)
        return FormView.form_valid(self, form)

 
class StudentProfileView(LoginRequiredMixin, CurrentUserMixin, DetailView):
    pass


class StudentProfileUpdateView(LoginRequiredMixin, CurrentUserMixin, UpdateView):
    model = Student
    fields = student_fields
    template_name_suffix = '_update_form'
    success_url = '/register/user/profile/edit/success/'