from datetime import datetime 
from pickle import FALSE
from re import T
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from random import randint,randrange

from traitlets import Instance


inc_status=(
    ('open','open'),('in progress','in progress'),('closed','closed')
)
inc_priority=(
    ('low',"low"),('medium','medium'),('high','high')
)


def incident_no():
    x='RMG'+str(randint(10000,99999)) + str(datetime.now().year)
    if incident.objects.filter(incident_number=x).exists()==True:
        return incident_no()
    else:
        return x




class incident(models.Model):
    incident_number = models.CharField(unique=True,max_length=12,editable=False)
    reporter_name= models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=15,null=False,blank=False)
    incident_details = models.TextField(null=False,blank=False,editable=True)
    priority =  models.CharField(max_length=6,choices=inc_priority,default='high',editable=True)
    incident_status = models.CharField(max_length=11,choices=inc_status,default='open',editable=True)
    reported_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.incident_number


    def save(self,*args,**kwargs):
        self.incident_number=incident_no()
        super(incident,self).save(*args,**kwargs)
    
    

    