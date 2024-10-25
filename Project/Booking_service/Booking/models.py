from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator, EmailValidator

def generate_sequential_id(prefix, last_id=None):
    if last_id is None:
        return f"{prefix}00000001"
    else:
        last_int = int(last_id[len(prefix):])
        new_int = last_int + 1
        new_id = f"{prefix}{str(new_int).zfill(8)}"
        return new_id

class Booking(models.Model):
    ticket_id = models.CharField(
        max_length=10,
        primary_key=True,
        unique=True,
    )
    trip_id = models.CharField(max_length=10)
    traveller_name = models.CharField(max_length=255)
    traveller_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex='^\d{10}$', message='Traveller number must be 10 digits')]
    )
    ticket_cost = models.FloatField()
    traveller_email = models.EmailField(validators=[EmailValidator()])

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            last_booking = Booking.objects.all().order_by('Ticket_id').last()
            if not last_booking:
                self.ticket_id = generate_sequential_id('TK')
            else:
                self.ticket_id = generate_sequential_id('TK', last_booking.ticket_id)
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_id
