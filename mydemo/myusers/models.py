from django.db import models
from django.contrib.auth.models import User
from django.core import validators
import os
from address.models import Country, State, City

# Create your models here.
GENDER_FIELD_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

PROFILE_FIELD_CHOICES = (
    ('0', 'Additional'),
    ('1', 'Profile'),
)

def image_upload_path(instance, filename):
    return os.path.join("images", filename)

class UserProfile(models.Model):
	user = models.ForeignKey(User, verbose_name="User", related_name="myusers", null=False, on_delete=models.CASCADE)
	# # firstname = models.CharField(verbose_name="First Name", null=False, max_length=50,
	#                         help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
	#                         validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
	image = models.ImageField(upload_to=image_upload_path, verbose_name="User Image", null=True, blank=True)
	gender = models.CharField(verbose_name="Gender", choices=GENDER_FIELD_CHOICES, null=False, max_length=15)
	dob = models.DateField(verbose_name="Date of birth")
	created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)
	time_of_birth = models.TimeField(verbose_name="Time of birth")
	place_of_birth = models.ForeignKey(City, verbose_name='Place of birth', related_name="placeOfBirth", null=False, on_delete=models.CASCADE)
	address = models.CharField(verbose_name="Address", null=False, max_length=255)
	country = models.ForeignKey(Country, verbose_name='Country', related_name="country", null=False, on_delete=models.CASCADE)
	state = models.ForeignKey(State, verbose_name='State', related_name="state", null=False, on_delete=models.CASCADE)
	city = models.ForeignKey(City, verbose_name='City', related_name="city", null=False, on_delete=models.CASCADE)
	pincode = models.CharField(verbose_name="Pincode", null=False, max_length=20)
	phone_no = models.IntegerField(verbose_name="Phone Number", null=False, max_length=15)
	height = models.FloatField(verbose_name="Height", null=False, max_length=15)
	weight = models.FloatField(verbose_name="Weight", null=False, max_length=15)
	# relegion = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# mothertoung = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# cast = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# sub_cast = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# gotra = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# manglik = models.IntegerField(verbose_name="Phone Number", null=False, max_length=15)
	# material_status = models.IntegerField(verbose_name="Phone Number", null=False, max_length=15)
	# smoke = models.CharField(verbose_name="Phone Number", null=False, max_length=15)
	# drink = models.CharField(verbose_name="Phone Number", null=False, max_length=15)
	# dite = models.CharField(verbose_name="Phone Number", null=False, max_length=15)
	# bio = models.TextField(verbose_name="Phone Number", null=False, max_length=15)
	# education = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# occupaion = models.ForeignKey(verbose_name="Phone Number", null=False, max_length=15)
	# salary = models.IntegerField(verbose_name="Phone Number", null=False, max_length=15)



	class Meta:
		db_table = "user_profile"
		verbose_name = "User Profile"
		verbose_name_plural = "User Profiles"

	def __str__(self):
		return f'{self.id}'


class UserImage(models.Model):
	user_profile = models.ForeignKey(UserProfile, verbose_name="User Profile", related_name="myprofile", null=False, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_upload_path, verbose_name="User Image", null=True, blank=True)
	image_type = models.CharField(verbose_name="Image Type", choices=PROFILE_FIELD_CHOICES, null=False, max_length=15)
	created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)


	class Meta:
		db_table = "user_image"
		verbose_name = "User Image"
		verbose_name_plural = "User Images"

	def __str__(self):
		return f'{self.id}'