from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.specialty})"


class Patient(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} (born {self.birthdate.strftime('%Y-%m-%d')})"


class Appointment(models.Model):
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    date = models.DateTimeField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M')} - \
            {self.doctor} with {self.patient}"
