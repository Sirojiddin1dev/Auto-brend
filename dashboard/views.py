from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import *
from main.serializers import CarSerializer, LeaseSerializer, BrandSerializer, GiveawayEntrySerializer


# Car Views
class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


# Lease Views
class LeaseListView(ListAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer


class LeaseCreateView(ListCreateAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated]


class LeaseUpdateView(UpdateAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated]


class LeaseDeleteView(DestroyAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    permission_classes = [IsAuthenticated]


# Brand Views
class BrandListView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandCreateView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


class BrandUpdateView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


class BrandDeleteView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


# GiveawayEntry Views
class GiveawayEntryListView(ListAPIView):
    queryset = GiveawayEntry.objects.all()
    serializer_class = GiveawayEntrySerializer


class GiveawayEntryCreateView(ListCreateAPIView):
    queryset = GiveawayEntry.objects.all()
    serializer_class = GiveawayEntrySerializer
    permission_classes = [IsAuthenticated]


class GiveawayEntryUpdateView(UpdateAPIView):
    queryset = GiveawayEntry.objects.all()
    serializer_class = GiveawayEntrySerializer
    permission_classes = [IsAuthenticated]


class GiveawayEntryDeleteView(DestroyAPIView):
    queryset = GiveawayEntry.objects.all()
    serializer_class = GiveawayEntrySerializer
    permission_classes = [IsAuthenticated]
