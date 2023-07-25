from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField(max_length=5)
    size = models.TextField()
    color = models.TextField()
    categories = models.ManyToManyField(Category)
    icon = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title