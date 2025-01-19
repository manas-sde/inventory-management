from djongo import models
from django.core.validators import MinValueValidator, RegexValidator, EmailValidator
from datetime import date



# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator(message="Enter a valid email address")], unique=True)
    phone = models.CharField(
        max_length=10,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d{10}$', message="Phone number must be 10 digits")
        ]
    )
    address = models.TextField()

    def __str__(self):
        return self.name
    

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.IntegerField(validators=[MinValueValidator(0)])  # Prevent negative stock
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Sale Order Model
class SaleOrder(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    sale_date = models.DateField(default=date.today)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Order {self.id} - {self.status}"


# Stock Movement Model
class StockMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('In', 'Incoming'),
        ('Out', 'Outgoing'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    movement_type = models.CharField(max_length=10, choices=MOVEMENT_CHOICES)
    movement_date = models.DateField(default=date.today)
    notes = models.TextField()

    def __str__(self):
        return f"{self.movement_type} - {self.product.name}"
