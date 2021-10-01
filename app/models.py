from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Company(models.Model):
    companies = models.ManyToManyField('self', blank=True, verbose_name="Компании-Партнеры")
    name = models.CharField("Название", max_length=255, unique=True)
    location = models.CharField("Местоположение", max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name="Владелец")
    created = models.DateTimeField("Создана", auto_now_add=True, null=True)
    updated = models.DateTimeField("Обновлена", auto_now=True, null=True)
    is_active = models.BooleanField("Статус работы", default=True)

    @property
    def employee_count(self):
        return Partnership.objects.filter(company=self).count()

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Работник", null=True)
    skills = models.TextField("Навыки/Языки", default="")

    def __str__(self):
        if self.user.last_name and self.user.first_name:
            return f"{self.user.last_name} {self.user.first_name}"
        return str(self.user)

def user_created(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)

post_save.connect(user_created, sender=User)



class Partnership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Работник")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")
    post = models.CharField("Должность", max_length=30)
    is_active = models.BooleanField("Статус партнерства", default=True)

    def __str__(self):
        return f"{self.employee} -> {self.company}"

