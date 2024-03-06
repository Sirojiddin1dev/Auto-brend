from django.urls import path
from .views import (
    # Car Views
    CarListView, CarCreateView, CarUpdateView, CarDeleteView,
    # Lease Views
    LeaseListView, LeaseCreateView, LeaseUpdateView, LeaseDeleteView,
    # Brand Views
    BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView,
    # GiveawayEntry Views
    GiveawayEntryListView, GiveawayEntryCreateView, GiveawayEntryUpdateView, GiveawayEntryDeleteView,
)

urlpatterns = [
    # Car URLs
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/create/', CarCreateView.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),

    # Lease URLs
    path('leases/', LeaseListView.as_view(), name='lease-list'),
    path('leases/create/', LeaseCreateView.as_view(), name='lease-create'),
    path('leases/<int:pk>/update/', LeaseUpdateView.as_view(), name='lease-update'),
    path('leases/<int:pk>/delete/', LeaseDeleteView.as_view(), name='lease-delete'),

    # Brand URLs
    path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),
    path('brands/<int:pk>/update/', BrandUpdateView.as_view(), name='brand-update'),
    path('brands/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),

    # GiveawayEntry URLs
    path('giveaway_entries/', GiveawayEntryListView.as_view(), name='giveaway-entry-list'),
    path('giveaway_entries/create/', GiveawayEntryCreateView.as_view(), name='giveaway-entry-create'),
    path('giveaway_entries/<int:pk>/update/', GiveawayEntryUpdateView.as_view(), name='giveaway-entry-update'),
    path('giveaway_entries/<int:pk>/delete/', GiveawayEntryDeleteView.as_view(), name='giveaway-entry-delete'),
]
