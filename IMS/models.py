from django.db import models


class create_item(models.Model): 
   Item_name= models.CharField(max_length=100)
   Quantity=models.PositiveIntegerField()
   Quantity_buy=models.PositiveIntegerField()
   Selling_price=models.DecimalField(max_digits=10, decimal_places=2)
   sell_item=models.PositiveIntegerField(blank=True,null=True)

   def __str__(self):
      return {self.id}
   
   def save(self,*args,**kwargs):
       
       if self.Quantity and self.sell_item:
           self.Quantity=self.Quantity - self.sell_item
       if self.Quantity:
           self.Quantity=self.Quantity
       super(create_item,self).save(*args,**kwargs)

        
   
class Inventory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    iin = models.CharField(max_length=20, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    profit_earned = models.DecimalField(max_digits=10, decimal_places=2)
    revenue = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
      return {self.id}

class Orders(models.Model):
    name = models.CharField(max_length=100)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    orderdttm = models.DateTimeField()
    is_received = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    transactiondttm = models.DateTimeField()

    def __str__(self):
        return self.name       