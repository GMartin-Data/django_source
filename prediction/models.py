from django.db import models

from .enums import *

    
class LoanApplication(models.Model):
    # city = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=2, choices=USState.choices(), null=False, blank=False)
    bank = models.CharField(max_length=50, null=False, blank=False)
    bank_state = models.CharField(max_length=2, choices=USState.choices(), null=False, blank=False)
    naics = models.CharField(max_length=100, choices=Naics.choices(), null=False, blank=False)
    term = models.PositiveSmallIntegerField(null=False, blank=False)
    new_exist = models.CharField(max_length=1, choices=YesNo.choices(), null=False, blank=False)
    no_emp = models.PositiveSmallIntegerField(null=False, blank=False)
    create_job = models.PositiveSmallIntegerField(null=False, blank=False)
    retained_job = models.PositiveSmallIntegerField(null=False, blank=False)
    franchise = models.CharField(max_length=1, choices=YesNo.choices(), null=False, blank=False)
    urban_rural = models.CharField(max_length=1, choices=UrbanRural.choices(), null=False, blank=False)
    rev_line_cr = models.CharField(max_length=7, choices=RevLineCr.choices(), null=False, blank=False)
    low_doc = models.CharField(max_length=1, choices=YesNo.choices(), null=False, blank=False)
    gr_appv = models.FloatField(null=False, blank=False)
    sba_appv = models.FloatField(null=False, blank=False)
