from django.db import models

class Favorito(models.Model):
    name = models.CharField(max_length=150)
    image = models.URLField(null=True, blank=True)
    house = models.CharField(max_length=100, null=True, blank=True)
    actor = models.CharField(max_length=150, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name