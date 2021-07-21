from django.db import models

# Create your models here.

class Companies(models.Model):
    company_choices = (('SRL', 'S.R.L.'),
                       ('SA', 'S.A.'))
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=5, choices=company_choices)

#create, update si listare