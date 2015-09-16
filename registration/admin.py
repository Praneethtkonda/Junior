'''
Created on 11-Sep-2015

@author: seshagiri
'''
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from registration.models import Student, Team
from registration.forms import StudentRegistrationForm, TeamRegistrationForm


class StudentChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on the user, but replaces the password field 
    with admin's password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Student
        fields = ('email', 'username', 'password', 'is_admin', 'approved')

    def clean_password(self):
        """
        Regardless of what the user provides, return the initial value. This is done here, rather 
        than on the field, because the field does not have access to the initial value
        """
        return self.initial["password"]


class StudentAdmin(UserAdmin):
    """
    Form to add and change user instances
    """
    
    form = StudentChangeForm
    add_form = StudentRegistrationForm
    search_fields = ('first_name', 'username', 'email', )
    ordering = ('approved', )
    filter_horizontal = ()    
    list_display = ('email', 'username', 'first_name', 'last_name', 'date_joined', 'city', 'state', 
                    'school_name', 'school_address', 'approved', 'is_admin', 'id_scanned')
    list_filter = ('date_joined', 'approved', )
    fieldsets = (
        (_('User Credentials'), {'fields': ('email', 'username', 'password', )}),
        (_('Personal info'), {
                           'classes': ('grp-collapse grp-closed',), 
                           'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 
                                      'address', 'contact_no', 'city', 'state', 'pincode', )
        }),
        (_('Academics info'), {
                           'classes': ('grp-collapse grp-closed',), 
                           'fields': ('standard', 'school_name', 'school_address',)
        }),
        (_('Scanned Id Card'), {'fields' : ('id_scanned',)}),
        (_('Permissions'), {'fields': ('is_admin', 'approved',)}),
    )
    
    add_fieldsets = (
        (_('User Credentials'), {'fields': ('email', 'username', 'password', 'repass', )}),
        (_('Permissions'), {'fields': ('is_admin', 'approved',)}),
        (_('Captcha'), {'fields': ('captcha',)}),
    ) 
   
   
class TeamChangeForm(forms.ModelForm):
    """
    A form for updating teams
    """
    class Meta:
        model = Team
        fields = ('team_name', 'team_school', 'member_one', 'member_two', 'qualified', 
                  'mentor_name', 'mentor_contact', 'mentor_email') 


class TeamAdmin(admin.ModelAdmin):
    """
    Form to add and change Team instances
    """
    form = TeamRegistrationForm
    add_form = TeamChangeForm
    list_filter = search_fields = ('team_name', 'team_school',)
    list_display = ('team_name', 'team_school', 'member_one', 'member_two', 'qualified', 
                  'mentor_name', 'mentor_contact', 'mentor_email')
    list_fieldsets = (
                          (_('Team Info'), {'fields': ('team_name', 'team_school', )}),
        (_('Member Info'), {
                            'classes': ('grp-collapse grp-closed',),
                            'fields': ('member_one', 'member_two',)
        }),
        (_('Mentor Info'), {
                            'classes': ('grp-collapse grp-closed',),
                            'fields': ('mentor_name', 'mentor_email', 'mentor_contact',)
        }),
        (_('Qualification'), {'fields': ('qualified',)}),
    )
    add_fieldsets = (
        (_('Team Info'), {'fields': ('team_name', 'team_school', )}),
        (_('Member Info'), {
                            'classes': ('grp-collapse grp-closed',),
                            'fields': ('member_one', 'member_two',)
        }),
        (_('Mentor Info'), {
                            'classes': ('grp-collapse grp-closed',),
                            'fields': ('mentor_name', 'mentor_email', 'mentor_contact',)
        }),
        (_('Qualification'), {'fields': ('qualified',)}),
        (_('Captcha'), {'fields': ('captcha',)}),
    )


admin.site.register(Team, TeamAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.unregister(Group)