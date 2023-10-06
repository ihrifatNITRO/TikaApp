
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
# class Get_Details(models.Model):
#     nid = models.CharField(max_length=20, primary_key=True,
#           validators=[RegexValidator(r'^\d+$', 'Only digits are allowed.')])
#     password = models.CharField(max_length=100)


# def __str__(self):
#     return self.name