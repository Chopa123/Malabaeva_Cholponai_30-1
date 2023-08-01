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


class Review(models.Model):
    choices = ((i, "*" * i) for i in range(1, 6))
    text = models.TextField()
    rating = models.IntegerField(choices=choices, default=0)
    products = models.ForeignKey(product, on_delete=models.CASCADE, related_name='reviews')
