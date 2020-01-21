from django.db import models


class ClothesType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    type = models.ForeignKey(ClothesType, on_delete=models.PROTECT)
    img_path = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
