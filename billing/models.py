from django.db import models

class Bill(models.Model):
    patient_name = models.CharField(max_length=100)
    service_description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gst_percent = models.DecimalField(max_digits=5, decimal_places=2, default=18.0)
    paid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def gst_amount(self):
        return (self.amount * self.gst_percent) / 100

    @property
    def total_amount(self):
        return self.amount + self.gst_amount

    def __str__(self):
        return f"{self.patient_name} - ₹{self.total_amount}"
