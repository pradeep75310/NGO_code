from django.db import models

class VolunteerApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    interests = models.TextField(help_text="What would you like to help with?")
    photo = models.ImageField(upload_to='volunteers/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


# models.py


class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.PositiveIntegerField()  # Amount in INR paisa (e.g. 50000 = ₹500)
    payment_id = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - ₹{self.amount/100:.2f}"

# Create your models here.
