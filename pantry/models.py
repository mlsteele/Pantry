from django.db import models
# from django.core.urlresolvers import reverse

class Grocery(models.Model):
    name        = models.CharField(max_length=255)
    count       = models.IntegerField(default=1)
    description = models.CharField(max_length=255, default="")
    created     = models.DateTimeField(auto_now_add=True)
    expires     = models.DateTimeField()

    class Meta:
        ordering = ['-count']

class Recipe(models.Model):
    name        = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default="")
    created     = models.DateTimeField(auto_now_add=True)
    ingredients = models.ManyToManyField(Grocery)
