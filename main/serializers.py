from rest_framework import serializers
from .models import User, Car, Lease, Brand, GiveawayEntry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'phone_number']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'brand_name', 'brand_img']


class CarSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'engine_type', 'img', 'fuel_type', 'year', 'price', 'brand']


class LeaseSerializer(serializers.ModelSerializer):
    car = CarSerializer()

    class Meta:
        model = Lease
        fields = ['id', 'car', 'monthly_payment', 'initial_payment', 'contract_months', 'allowed_mileage']


class GiveawayEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    car = CarSerializer()

    class Meta:
        model = GiveawayEntry
        fields = ['id', 'user', 'car', 'entry_date']
