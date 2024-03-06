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
    path('Lease_by_car/', lease_by_car),
    path('Lease_by_monthly_payment/', lease_by_monthly_payment),
    path('Lease_by_initial_payment/', lease_by_initial_payment),
    path('Lease_by_contract_months/', lease_by_contract_months),
    path('Lease_by_allowed_mileage/', lease_by_allowed_mileage),
    path('Brand_by_brand_name/', brand_by_brand_name),
    path('GiveawayEntry_by_user/', giveaway_entry_by_user),
    path('GiveawayEntry_by_car/', giveaway_entry_by_car),
    path('GiveawayEntry_by_entry_date/', giveaway_entry_by_entry_date),

]