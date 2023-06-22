from django.db import models

# Class Recipients for the people receiving a postcard
# features = salutation, first name, last name, email 
class Recipient(models.Model):
    salutation = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"