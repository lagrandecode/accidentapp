from django.db import models

# Create your models here.

class Report(models.Model):
    Witness_Name = models.CharField(max_length=100)
    Witness_Email = models.EmailField()
    Witness_Phone = models.CharField(max_length=17,blank=True,null=True)
    
