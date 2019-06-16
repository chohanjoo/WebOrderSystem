from django.db import models
from owner.models import MenuBoard
# Create your models here.

class OrderNumber(models.Model):
    menuBoard = models.ForeignKey(MenuBoard, on_delete=models.CASCADE)
    orderNumber = models.PositiveIntegerField(unique=True)
