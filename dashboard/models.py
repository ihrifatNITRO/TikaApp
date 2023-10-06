
from django.contrib.auth.models import User
from django.db import models
from datetime import date


class ChildInfo(models.Model):
    parent_nid = models.ForeignKey(User, on_delete=models.CASCADE)
    child_name = models.CharField(max_length=255)
    birth_date = models.IntegerField()
    birth_month = models.IntegerField(null=True, blank=True)
    birth_year = models.IntegerField()
    blood_group = models.CharField(max_length=10)
    vaccine_taken = models.PositiveIntegerField(default=0)
    last_vaccine = models.DateField(null=True, blank=True)
    next_vaccine = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    age_in_months = models.PositiveIntegerField(null=True, blank=True)

    def calculate_age_in_months(self):
        today = date.today()
        birth_month = self.birth_month
        birth_year = self.birth_year
        
        if birth_month and birth_year:
            age_in_months = (today.year - birth_year) * 12 + (today.month - birth_month)
            return age_in_months
        else:
            return None

    def save(self, *args, **kwargs):
        self.age_in_months = self.calculate_age_in_months()
        super(ChildInfo, self).save(*args, **kwargs)

    def __str__(self):
        return self.child_name