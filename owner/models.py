from django.db import models
from django.conf import settings
# Create your models here.
class Shop(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =models.CASCADE,primary_key=True)
    shopID = models.PositiveIntegerField(unique=True)
    shopName = models.CharField(max_length=30)
    openDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shopName


class MenuBoard(models.Model):
    menuBoardName = models.CharField(max_length=20)
    menuBoardID = models.BigIntegerField()
    shopID = models.ForeignKey(Shop,to_field='shopID', on_delete=models.CASCADE)

    def __str__(self):
        return self.menuBoardName