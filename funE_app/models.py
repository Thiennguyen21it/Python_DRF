from django.db import models

# Create your models here.

class User(models.Model): 
     id = models.AutoField(primary_key=True)
     email = models.EmailField(max_length=24)
     username = models.CharField(max_length=12)
     first_name = models.CharField(max_length=12)
     last_name = models.CharField(max_length=12)
     
     def __str__ (self):
         return self.username
     


