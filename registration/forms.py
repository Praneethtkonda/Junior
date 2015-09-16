from django import forms
from django.utils.translation import ugettext_lazy as _
from bootstrap3_datetime.widgets import DateTimePicker
from captcha.fields import ReCaptchaField

from registration.models import Student, Team
from django.forms.models import ModelForm


student_widgets = {
    'first_name'    : forms.TextInput(attrs={'placeholder':_('First Name')}),
    'last_name'     : forms.TextInput(attrs={'placeholder':_('Last Name')}),
    'contact_no'    : forms.TextInput(attrs={'placeholder':_('Your Phone Number')}),
    'date_of_birth' : DateTimePicker(options={"getUTCDate": True, "pickTime": False, 
                                              "date":"fa fa-calendar", "viewMode":'years', 
                                              "format":'DD/MM/YYYY', 
                                              "defaultDate":"01/01/2000"}, 
                                     attrs={'placeholder':_('DD/MM/YYYY')}),
    'contact_no'    : forms.TextInput(attrs={'placeholder':_('Your Mobile phone number')}),
    'address'       : forms.Textarea(attrs={'placeholder':_('Residential Address'), 
                                            'rows':4, 'cols':15}),
    'city'          : forms.TextInput(attrs={'placeholder':_('City')}),
    'pincode'       : forms.TextInput(attrs={'placeholder':_('Pincode')}),
    'school_name'   : forms.TextInput(attrs={'placeholder':_('School Name')}),
    'school_address': forms.Textarea(attrs={'placeholder':_('Address of your school'), 
                                            'rows':4, 'cols':15}),
    'email'         : forms.TextInput(attrs={'placeholder':_('Enter your Email Address')}),
    'username'      : forms.TextInput(attrs={'placeholder':_('Username')})
}


student_help_text = {
    'date_of_birth' : _('Click/tap on the calendar icon'),
    'id_scanned'    : _('Upload the scanned copy of your school ID card'),
}


student_fields = ['first_name', 'last_name', 'gender', 'date_of_birth', 'address', 
                  'contact_no', 'city', 'pincode', 'standard', 'school_name', 'school_address', 
                  'id_scanned', 'email', 'username']

                  
team_fields = ['team_name', 'team_school', 'member_one', 'member_two', 'mentor_name', 
               'mentor_contact', 'mentor_email']


team_widgets = {
    'team_name'     : forms.TextInput(attrs={'placeholder':_('Team Name'), 
                                            'min_length':2, 'max_length':100}),
    'team_school'   : forms.TextInput(attrs={'placeholder':_('Name of your School'), 
                                            'min_length':2, 'max_length':100}),
    'member_one'    : forms.EmailInput(attrs={'placeholder':_('Member one Email Address')}),
    'member_two'    : forms.EmailInput(attrs={'placeholder':_('Member two Email Address')}),
    'mentor_name'   : forms.TextInput(attrs={'placeholder':_('Mentor/Guide/Principal\'s Name'), 
                                             'min_length':2, 'max_length':50}),
    'mentor_email'  : forms.EmailInput(attrs={'placeholder':_('Email Address of Mentor')}),
    'mentor_contact': forms.TextInput(attrs={'placeholder':_('Your Mentor\'s Contact no')})
}


captcha_attrs = {'theme': 'clean', 'size': 'compact'}

                  
class StudentRegistrationForm(ModelForm):
    repass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re Enter Password', 
                                                     'min_length':1, 'max_length':20}))
    captcha = ReCaptchaField(attrs=captcha_attrs, required=True)
    
    class Meta:
        model = Student
        fields = student_fields + ['password']
        help_texts = student_help_text
        widgets = student_widgets
        widgets['password'] = forms.PasswordInput(attrs={'placeholder':_('Password')})
        
    
    def clean(self):
        password, re_password = self.cleaned_data.get('password'), self.cleaned_data.get('repass')
        if password and password != re_password: 
            raise forms.ValidationError(_("Passwords don\'t match"))
        return self.cleaned_data
    
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(_('Email "%s" is already in use.') % email)
        return email
    
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Student.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(_('Username "%s" is already in use.') % username)
        return username
    
    
    def clean_repass(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('repass')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords don\'t match"))
        return password2
    
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(StudentRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit: user.save()
        return user
    
    
class StudentProfileUpdateForm(ModelForm):
    captcha = ReCaptchaField(attrs=captcha_attrs, required=True)
    
    class Meta:
        model = Student
        fields = student_fields
        help_texts = student_help_text
        widgets = student_widgets
                                                  

    def save(self, *args, **kwargs):
        kwargs['commit']=False
        obj = super(StudentProfileUpdateForm, self).save(*args, **kwargs)
        if self.request: obj.user = self.request.user; obj.save()
        return obj    
            

class TeamRegistrationForm(ModelForm):
    captcha = ReCaptchaField(attrs=captcha_attrs)
    
    class Meta:
        model = Team
        fields = team_fields 
        widgets = team_widgets
        
    
    def clean_member_one(self):
        member_one = self.cleaned_data.get('member_one')
        member_two = self.cleaned_data.get('member_two')
        if member_one == member_two:
            raise forms.ValidationError(_('Member one and Member two cannot be the same'))
        if member_one and not \
            Student.objects.exclude(pk=self.instance.pk).filter(email=member_one).exists():
            raise forms.ValidationError(_('Member with "%s" email does not exist.') % member_one)
        if member_one and not \
            Student.objects.exclude(pk=self.instance.pk).filter(email=member_one)[0].approved:
            raise forms.ValidationError(_('Member one\'s registration is under moderation'))
        if Team.objects.exclude(pk=self.instance.pk).filter(member_one=member_one).exists() or \
            Team.objects.exclude(pk=self.instance.pk).filter(member_two=member_one).exists():
            raise forms.ValidationError(_('Member one is part of another team'))
        return member_one
        
        
    def clean_member_two(self):
        member_two = self.cleaned_data.get('member_two')
        if member_two and not \
            Student.objects.exclude(pk=self.instance.pk).filter(email=member_two).exists():
            raise forms.ValidationError(_('Member with "%s" email does not exist.') % member_two)
        if member_two and not \
            Student.objects.exclude(pk=self.instance.pk).filter(email=member_two)[0].approved:
            raise forms.ValidationError(_('Member two\'s registration is under moderation'))
        if Team.objects.exclude(pk=self.instance.pk).filter(member_one=member_two).exists() or \
            Team.objects.exclude(pk=self.instance.pk).filter(member_two=member_two).exists():
            raise forms.ValidationError(_('Member one is part of another team'))
        return member_two