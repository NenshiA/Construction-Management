from django.db import models
from django.core.validators import MinLengthValidator


class Employee(models.Model):
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    # address = models.CharField(max_length=500)
    # city = models.CharField(max_length=100)
    # gender = models.CharField(max_length=50)
    # dob = models.DateField()
    is_emp = models.CharField(max_length=200, default="Y")

    def register(self):
        self.save()

    @staticmethod
    def get_employee_by_email(email):
        try:
            return Employee.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Employee.objects.filter(email=self.email):
            return True
        return False
