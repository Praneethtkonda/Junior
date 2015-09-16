from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

# Lists
GENDER = (('M', _('Male')), ('F', _('Female')))

STANDARD = (('9', _('9th Standard')), ('10', _('10th Standard')),
            ('11', _('11th Standard')), ('12', _('12th Standard')))

LIST_OF_STATES = (
    ('1',_('Andhra Pradesh')), ('2',_('Arunachal Pradesh')),
    ('3',_('Assam')), ('4',_('Bihar')),
    ('5',_('Chhattisgarh')), ('6',_('Goa')),
    ('7',_('Gujarat')), ('8',_('Haryana')),
    ('9',_('Himachal Pradesh')), ('10',_('Jammu and Kashmir')),
    ('11',_('Jharkhand')), ('12',_('Karnataka')),
    ('13',_('Kerala')), ('14',_('Madhya Pradesh')),
    ('15',_('Maharashtra')), ('16',_('Manipur')),
    ('17',_('Meghalaya')), ('18',_('Mizoram')),
    ('19',_('Nagaland')), ('20',_('Orissa')),
    ('21',_('Punjab')), ('22',_('Rajasthan')),
    ('23',_('Sikkim')), ('24',_('Tamil Nadu')),
    ('25',_('Tripura')), ('26',_('Uttar Pradesh')),
    ('27',_('Uttarakhand')), ('28',_('West Bengal')),
    ('29',_('New Delhi')))

# Model Manager
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, email and password.
        """
        if not email:raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(email, username, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
# Models
class Student(AbstractBaseUser):
    """
    Extends the default User profiles of Django. The fields of this model can be obtained by the 
    user.get_profile method and it's extended by the django-profile application.
    """
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(_('First Name'), max_length=32, blank=True, null=True, 
                                  validators=[RegexValidator(regex='^[A-Za-z]*$')])
    last_name = models.CharField(_('Last Name'), max_length=32, blank=True, null=True,
                                 validators=[RegexValidator(regex='^[A-Za-z]*$')])
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER, blank=True, null=True)
    contact_no = models.CharField(_('Phone Number'), max_length=11, 
                                  validators=[RegexValidator(
                                         regex='^[0-9]*$',
                                         message='Invalid characters in the phone number.')], 
                                  help_text=_('11 digits maximum'), blank=True, null=True)
    date_of_birth = models.DateField(_('Birth Date'), blank=True, null=True)
    address = models.CharField(_('Home Address'), max_length=1000, blank=True, null=True)
    state = models.CharField(_('State'), max_length=2, choices=LIST_OF_STATES, 
                             blank=True, null=True)
    city = models.CharField(_('City'), max_length=30, blank=True, null=True)
    pincode = models.IntegerField(_('Pincode'), 
                                  validators=[MaxValueValidator(799999),MinValueValidator(110000)], 
                                  help_text=_('6 digits maximum'), blank=True, null=True)
    standard = models.CharField(_('Standard'), choices=STANDARD, max_length=2, 
                                blank=True, null=True)
    school_name = models.CharField(_('School Name'), max_length=150, blank=True, null=True)
    school_address = models.CharField(_('School Address'), max_length=255, blank=True, null=True)
    id_scanned = models.ImageField(_('School ID Scanned'), upload_to='id_scanned/%Y/%m/%d',
                                   blank=True, null=True)
    approved = models.BooleanField(_('Approved'), default=False)
    email = models.EmailField(_('Email'), db_index=True, unique=True)
    username = models.CharField(_('username'), max_length=32, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
    def get_full_name(self):
        return (self.first_name, self.last_name)

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    
class Team(models.Model):
    """
    Team model
    """
    team_id = models.AutoField(primary_key=True)
    team_name = models.CharField(_('Team Name'), max_length=100, blank=False, unique=True)
    team_school = models.CharField(_('Team School'), max_length=100, blank=True, null=True)
    member_one = models.EmailField(_('Member One'), blank=False)
    member_two = models.EmailField(_('Member Two'), blank=True, null=True)
    mentor_name = models.CharField(_('Mentor Name'), max_length=50, blank=True, null=True)
    mentor_email = models.EmailField(_('Mentor Email'), blank=True, null=True)
    mentor_contact = models.CharField( _('Mentor Contact No'), max_length=15, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    qualified = models.BooleanField(default=True)
    
    
    class Meta:
        unique_together = (('team_name', 'member_one', 'member_two'))