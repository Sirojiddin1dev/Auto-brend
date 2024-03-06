from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from .serializers import *


@api_view(["GET"])
def car_by_make(request):
    make = request.GET.get('make')
    car = Car.objects.filter(make__icontains=make)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def car_by_model(request):
    model = request.GET.get('model')
    car = Car.objects.filter(model__icontains=model)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def car_by_engine_type(request):
    engine_type = request.GET.get('engine_type')
    car = Car.objects.filter(engine_type__icontains=engine_type)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def car_by_fuel_type(request):
    fuel_type = request.GET.get('fuel_type')
    car = Car.objects.filter(fuel_type__icontains=fuel_type)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def car_by_year(request):
    year = request.GET.get('year')
    car = Car.objects.filter(year__icontains=year)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def car_by_price(request):
    price = request.GET.get('price')
    car = Car.objects.filter(price__icontains=price)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def car_by_brand(request):
    brand = request.GET.get('brand')
    car = Car.objects.filter(brand__icontains=brand)
    ser = CarSerializer(car, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Lease_by_car(request):
    car = request.GET.get('car')
    lease = Lease.objects.filter(car__icontains=car)
    ser = LeaseSerializer(lease, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Lease_by_monthly_payment(request):
    monthly_payment = request.GET.get('monthly_payment')
    lease = Lease.objects.filter(monthly_payment__icontains=monthly_payment)
    ser = LeaseSerializer(lease, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Lease_by_initial_payment(request):
    initial_payment = request.GET.get('initial_payment')
    lease = Lease.objects.filter(initial_payment__icontains=initial_payment)
    ser = LeaseSerializer(lease, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Lease_by_contract_months(request):
    contract_months = request.GET.get('contract_months')
    lease = Lease.objects.filter(contract_months__icontains=contract_months)
    ser = LeaseSerializer(lease, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Lease_by_allowed_mileage(request):
    allowed_mileage = request.GET.get('allowed_mileage')
    lease = Lease.objects.filter(allowed_mileage__icontains=allowed_mileage)
    ser = LeaseSerializer(lease, many=True)
    return Response(ser.data)


@api_view(["GET"])
def Brand_by_brand_name(request):
    brand_name = request.GET.get('brand_name')
    brand = Brand.objects.filter(brand_name__icontains=brand_name)
    ser = BrandSerializer(brand, many=True)
    return Response(ser.data)


@api_view(["GET"])
def GiveawayEntry_by_user(request):
    user = request.GET.get('user')
    giveawayEntry = GiveawayEntry.objects.filter(user__icontains=user)
    ser = GiveawayEntrySerializer(giveawayEntry, many=True)
    return Response(ser.data)


@api_view(["GET"])
def GiveawayEntry_by_car(request):
    car = request.GET.get('car')
    giveawayEntry = GiveawayEntry.objects.filter(car__icontains=car)
    ser = GiveawayEntrySerializer(giveawayEntry, many=True)
    return Response(ser.data)


@api_view(["GET"])
def GiveawayEntry_by_entry_date(request):
    entry_date = request.GET.get('entry_date')
    giveawayEntry = GiveawayEntry.objects.filter(entry_date__icontains=entry_date)
    ser = GiveawayEntrySerializer(giveawayEntry, many=True)
    return Response(ser.data)