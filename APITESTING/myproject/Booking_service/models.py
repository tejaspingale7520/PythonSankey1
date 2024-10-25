from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator, EmailValidator
from Trip.models import Trip  # Ensure the Trip model is imported correctly

def generate_id(prefix):
    random_part = get_random_string(8, allowed_chars='0123456789')
    return f"{prefix}{random_part}"

class Booking(models.Model):
    ticket_id = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
        default=lambda: generate_id('TK')
    )
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE, to_field='trip_id')
    traveller_name = models.CharField(max_length=255)
    traveller_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='Traveller number must be 10 digits')]
    )
    ticket_cost = models.FloatField()
    traveller_email = models.EmailField(validators=[EmailValidator()])

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = generate_id('TK')
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_id
