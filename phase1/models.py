from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=300)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.department}"
