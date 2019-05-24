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
    menuBoardID = models.PositiveIntegerField()
    shopID = models.ForeignKey(Shop, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20)
    menuBoard = models.ForeignKey(MenuBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name



