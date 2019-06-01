from django.db import models

# Create your models here.
class Shop(models.Model):
    shopID = models.PositiveIntegerField()
    shopName = models.CharField(max_length=30)
    masterName = models.CharField(max_length=10)
    openDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shopName


class MenuBoard(models.Model):
    menuBoardName = models.CharField(max_length=20)
    menuBoardID = models.BigIntegerField()
    shopID = models.ForeignKey(Shop, on_delete=models.CASCADE)