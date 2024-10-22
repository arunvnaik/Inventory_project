# models.py

from django.db import models

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
