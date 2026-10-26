from django.db import models

class Adhar(models.Model):
    adhar_name= models.CharField(max_lenth=100)
    adhar_number= models.CharField(max_length=12)
    dob=models.DateField()
    address= models.CharField(max_length=100)
    image=models.CharField()
    created_at= models.DateTimeField(auto_now_add=0)
    updated_at= models.DateTimeField(auto_now=0)
    
    
    #search= Adhar.objects.filter(adhar_name ='shakshi')
    
    