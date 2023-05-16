from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    state = models.BooleanField(default=True)
    description = models.TextField()
    urlimage = models.URLField()
    rating = models.FloatField()
    idCategory = models.ManyToManyField(Category)

    def __str__(self):
        return self.title