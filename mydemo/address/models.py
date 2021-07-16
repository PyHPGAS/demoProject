from django.db import models
from django.core import validators

# Create your models here.
class Country(models.Model):
    name = models.CharField(verbose_name="Country Name", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "country"
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, verbose_name="Country", related_name="state", null=False, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="State Name", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "state"
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return f'{self.id}-{self.country}-{self.name}'

class City(models.Model):
    state = models.ForeignKey(State, verbose_name="State", related_name="city", null=False, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="City Name", null=False, max_length=50,
                            help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
                            validators=[validators.RegexValidator(r'^[\w .@+-_]+$', 'Enter a valid name. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')])
    status = models.BooleanField(verbose_name="Status", null=False, default=False)
    created_at = models.DateTimeField(verbose_name="Date (created)", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Date (updated)", auto_now=True)

    class Meta:
        db_table = "city"
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return f'{self.id}-{self.state}-{self.name}'
