from django.db import models
from django.urls import reverse

# Create your models here.

class Report(models.Model):
    Witness_Name = models.CharField(max_length=100)
    MALE = 'm'
    FEMALE = 'f'
    GENDER_CHOICE = (
        (MALE,'male'),
        (FEMALE,'female')
    )
    Gender_Witness = models.CharField(max_length=1,choices=GENDER_CHOICE,default=MALE)
    Witness_Email = models.EmailField()
    Witness_Phone = models.CharField(max_length=17,blank=True,null=True)
    Date_of_accident = models.DateField()
    Time_of_accident = models.DateTimeField()
    YES = 'y'
    NO = 'n'
    VITAL_CHOICES = (
        (YES,'yes'),
        (NO,'no')
    )
    is_vital = models.CharField(max_length=1,choices=VITAL_CHOICES,default=NO)
    ALIMOSHO = 'Alimosho'
    AGEGE = 'Agege'
    STATUS_LOCATION = (
        (ALIMOSHO,'Alimosho'),
        (AGEGE,'Agege')
    )
    Location = models.CharField(max_length=20,choices=STATUS_LOCATION,default=AGEGE)
    number_of_vehicle_involved = models.PositiveIntegerField(default=0)
    number_of_injured = models.PositiveIntegerField(default=0)
    number_of_death = models.PositiveIntegerField(default=0)
    cause_of_accident = models.TextField(default='what is the cause?')
    description = models.TextField(default='Describe what happened')
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', default=None)
    video = models.FileField(upload_to='videos/',default=None)

    def __str__(self):
        return f'Accident report by {self.Witness_Name}'
    
    def get_absolute_url(self):
        return reverse('report', kwargs={'id': self.id})

