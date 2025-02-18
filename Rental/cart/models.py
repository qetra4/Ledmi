from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Cart(models.Model):
    product = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"

    def get_absolute_url(self):
        return reverse("cart:cart_detail")


