from django.db import models

# Create your models here.
class Recipient(models.Model):
    salutation = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    postcard_message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"