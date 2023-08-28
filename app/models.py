from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=40)
    models_name = models.CharField(max_length=40)

    def __str__(self):
        return self.models_name