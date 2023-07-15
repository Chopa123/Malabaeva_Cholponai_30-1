from django.db import models

class product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField(max_length=5)
    size = models.TextField()
    color = models.TextField()




