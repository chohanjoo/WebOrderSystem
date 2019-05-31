from django.db import models
from owner.models import MenuBoard
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=20)
    menuBoard = models.ForeignKey(MenuBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name



