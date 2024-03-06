from django.urls import path
from .views import *

urlpatterns = [
    path('car_by_make/', car_by_make),
    path('car_by_model/', car_by_model),
    path('car_by_engine_type/', car_by_engine_type),
    path('car_by_fuel_type/', car_by_fuel_type),
    path('car_by_year/', car_by_year),
    path('car_by_price/', car_by_price),
    path('car_by_brand/', car_by_brand),
    path('Lease_by_car/', Lease_by_car),
    path('Lease_by_monthly_payment/', Lease_by_monthly_payment),
    path('Lease_by_initial_payment/', Lease_by_initial_payment),
    path('Lease_by_contract_months/', Lease_by_contract_months),
    path('Lease_by_allowed_mileage/', Lease_by_allowed_mileage),
    path('Brand_by_brand_name/', Brand_by_brand_name),
    path('GiveawayEntry_by_user/', GiveawayEntry_by_user),
    path('GiveawayEntry_by_car/', GiveawayEntry_by_car),
    path('GiveawayEntry_by_entry_date/', GiveawayEntry_by_entry_date),

]