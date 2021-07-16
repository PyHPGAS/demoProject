from django.db import models
from django.contrib.auth.models import User
from django.core import validators
import os

# Create your models here.
GENDER_FIELD_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
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


	class Meta:
		db_table = "user_profile"
		verbose_name = "User Profile"
		verbose_name_plural = "User Profiles"

	def __str__(self):
		return f'{self.id}'