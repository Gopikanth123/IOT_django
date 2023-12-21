from django.db import models

class Testing(models.Model):
    can_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    snf = models.DecimalField(max_digits=5, decimal_places=2)
    clr = models.DecimalField(max_digits=5, decimal_places=2)
    adc_water = models.DecimalField(max_digits=5, decimal_places=2)
