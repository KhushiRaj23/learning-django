from django.db import models

class Emp(models.Model):   #Emp is sub-class of Model class
    
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    salary=models.IntegerField()
      
    
    
