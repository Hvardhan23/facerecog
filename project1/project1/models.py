from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Concern(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=100)
    concern_title = models.CharField(max_length=200)
    concern_description = models.TextField()

    def __str__(self):
        return self.title
