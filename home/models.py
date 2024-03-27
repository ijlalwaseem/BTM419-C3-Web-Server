from django.db import models

# Create your models here.
class Dealership(models.Model):
    # A dealership the user can select
    dealership = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        # Return a string representation of the model
        return self.dealership

class Sale(models.Model):
    # An entry about a sale
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'mysales'

    def __str__(self):
        # Return a string representation of the model
        return f'{self.product} {self.price} {self.customer_id}'

class Inventory(models.Model):
    # An entry about an inventory
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'myinventorys'

    def __str__(self):
        # Return a string representation of the model
        return f'{self.product} {self.quantity}'

class Inspection(models.Model):
    # An entry about an inspection
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    vin = models.CharField(max_length=200)
    comments = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'myinspections'

    def __str__(self):
        # Return a string representation of the model
        return f'{self.vin} {self.comments}'