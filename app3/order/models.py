from django.db import models
from django.contrib.auth.models import User
from library.models.phone import Phone
# Create your models here.
class PaymetStatus(models.TextChoices):
    PENDING = "На рассмотрении"
    PROCESSED = "В обработке"
    SHIPPED = "Отправлен"
    DELIVERED = "Доставлен"

class Order(models.TextChoices):
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=PaymetStatus)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} for {self.customer_user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.phone} for {self.order}"