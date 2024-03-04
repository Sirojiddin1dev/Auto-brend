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
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.username


class Car(models.Model):
    make = models.CharField(max_length=255, verbose_name='Ishlab chiqaruvchi')
    model = models.CharField(max_length=255, verbose_name='Model')
    engine_type = models.CharField(max_length=255, verbose_name='Dvigatel turi')
    img = models.ImageField(upload_to='car_img/', verbose_name='Avtomobil surati')
    fuel_type = models.CharField(max_length=50, verbose_name='Yoritqich turi')
    year = models.IntegerField(verbose_name='Ishlab chiqarilgan yil')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narx')
    brand = models.ForeignKey(to='Brand', on_delete=models.CASCADE, verbose_name='Ishlab chiqaruvchi brand')


class Lease(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Arendaga olish')
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Oylik to\'lov')
    initial_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Boshlang\'ich to\'lov')
    contract_months = models.IntegerField(verbose_name='Muddat')
    allowed_mileage = models.IntegerField(verbose_name='Yo\'l qilishga ruxsat berilgan masofa')


class Brand(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name='Brand nomi')
    brand_img = models.ImageField(upload_to='brand_img/', verbose_name='Brand rasmi')


class GiveawayEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Foydalanuvchi')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Avto')
    entry_date = models.DateField(verbose_name='Kirish sanasi')
