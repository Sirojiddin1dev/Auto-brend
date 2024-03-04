from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    age = models.IntegerField(verbose_name='Yosh', null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True, verbose_name='Telefon raqam', validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Car(models.Model):
    make = models.CharField(max_length=255, verbose_name='make')
    model = models.CharField(max_length=255, )
    engine_type = models.CharField(max_length=255)
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE)


class Lease(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    initial_payment = models.DecimalField(max_digits=10, decimal_places=2)
    contract_months = models.IntegerField()
    allowed_mileage = models.IntegerField()


class Brand(models.Model):
    brand_name = models.CharField(max_length=255)
    brand_img = models.ImageField(upload_to='brand_img/')


class GiveawayEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    entry_date = models.DateField()
