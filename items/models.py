from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=101)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'