from django.db import models
from datetime import datetime

class Payment(models.Model):
    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

    card_number = models.CharField(max_length=16)
    cardholder_name = models.CharField(max_length=255)
    expiration_date = models.DateField(default=datetime.now, blank = True)
    cvv = models.CharField(max_length=4)

# Create your models here.
