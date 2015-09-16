from django.conf.urls import url
from registration.views import StudentRegistrationView, TeamRegistrationView, StudentProfileView
from registration.views import StudentProfileUpdateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from registration.models import Student, Team
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='register/register.html')),
    url(r'^user/$', StudentRegistrationView.as_view(), name='register_user'),
    url(r'^user/success/', TemplateView.as_view(template_name='register/user/successful.html'), 
        name='user_registration_success'),
    url(r'^user/list/$', 
        staff_member_required(ListView.as_view(template_name='register/user/list.html', model=Student)), 
        name='user_list'),
    url(r'^team/$', TeamRegistrationView.as_view(), name='register_team'),
    url(r'^team/success/', 
        login_required(TemplateView.as_view(template_name='register/team/successful.html')), 
        name='team_registration_success'),
    url(r'^team/list/$', 
        ListView.as_view(template_name='register/team/list.html', model=Team), 
        name='team_list'),
    url(r'^user/profile/$', StudentProfileView.as_view(), name='user_profile'),
    url(r'^user/profile/edit/$', StudentProfileUpdateView.as_view(), name='user_profile_update'),
    url(r'^user/profile/edit/success/$', 
        TemplateView.as_view(template_name='registration/student_update_success.html'), 
        name='user_profile_update_success'),
]
