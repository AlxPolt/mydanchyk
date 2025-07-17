from django.db import models

class Court(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    adaptive_support = models.BooleanField(default=False)
    booking_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.city})"


class Slot(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.court.name} - {self.date} {self.time}"
