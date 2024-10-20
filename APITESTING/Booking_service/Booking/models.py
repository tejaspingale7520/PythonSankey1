from django.db import models
import re
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from Trip.models import Trip

def validate_ticket_id(value):
    if not re.match(r'^TK\d{8}$', value):
        raise ValidationError('ID must start with "TK" and be followed by 8 digits')

class Booking(models.Model):
    ticket_id = models.CharField(primary_key=True, max_length=10, validators=[validate_ticket_id])
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    traveller_name = models.CharField(max_length=255)
    traveller_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='Traveller number must be 10 digits')]
    )
    ticket_cost = models.FloatField()
    traveller_email = models.EmailField(validators=[EmailValidator()])

    def __str__(self):
        return self.ticket_id