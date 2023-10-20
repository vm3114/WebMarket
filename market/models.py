from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length = 128)
    email = models.CharField(max_length = 128)
    password = models.CharField(max_length = 32)
    phone = models.CharField(max_length = 12)

    def __str__(self):
        return self.name