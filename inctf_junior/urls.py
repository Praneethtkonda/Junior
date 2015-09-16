from django.conf.urls import include, url
from registration import urls as reg_urls
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import  static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from inctf_junior import settings
from inctf_junior.views import anonymous_required, ContactFormView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="general/home.html"), name='home'),
    url(r'^about/', TemplateView.as_view(template_name="general/about.html"), name='about'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^register/', include(reg_urls), name='register'),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^user/login/$', 
        anonymous_required(auth_views.login), 
        {'template_name': 'registration/login.html'},
        name='login'),
    url(r'^user/logout/$', 
        auth_views.logout, 
        {'template_name': 'registration/logout.html'}, 
        name='logout'),
    url(r'^password/change/$', 
        auth_views.password_change,
        {'template_name': 'registration/passwd_change.html'}, 
        name='password_change'),
    url(r'^password_change/done/$', 
        auth_views.password_change_done,
        {'template_name': 'registration/passwd_change_done.html'}, 
        name='password_change_done'),
    url(r'^password/reset/$', 
        anonymous_required(auth_views.password_reset), 
        {'template_name': 'registration/passwd_reset.html', 
        'email_template_name':'registration/passwd_reset_email.html'},
        name='password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 
        anonymous_required(auth_views.password_reset_confirm),
        {'template_name': 'registration/passwd_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$', anonymous_required(auth_views.password_reset_complete),  
        {'template_name': 'registration/passwd_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^password/reset/done/$', 
        anonymous_required(auth_views.password_reset_done), 
        {'template_name': 'registration/passwd_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^contact/$', ContactFormView.as_view(), name='contact_form'),
    url(r'^contact/success/$', 
        TemplateView.as_view(template_name='contact_form/contact_form_sent.html'), 
        name='contact_form_sent'),
]


# Serve '/media/id_scanned/' for viewing scanned id cards

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)