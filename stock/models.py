from django.db import models

class StockItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class SoldItem(models.Model):
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sold_date = models.DateTimeField(auto_now_add=True)

class AvailableStock(models.Model):
    stock_item = models.ForeignKey(StockItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.stock_item.name} - {self.quantity} available"
