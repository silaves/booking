from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    # Service endpoints
    path('client/', ClientView.as_view(), name='client'),
    path('client/<int:pk>/', ClientView.as_view(), name='client'),
    path('room-type/', RoomTypeView.as_view(), name='room-type'),
    path('room-type/<int:pk>/', RoomTypeView.as_view(), name='room-type'),
    path('room/', RoomView.as_view(), name='room'),
    path('room/<int:pk>/', RoomView.as_view(), name='room'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('booking/<int:pk>/', BookingView.as_view(), name='booking'),
    path('payment-method/', PaymentMethodView.as_view(), name='payment-method'),
    path('payment-method/<int:pk>/', PaymentMethodView.as_view(), name='payment-method'),
    path('payment/<int:pk>/', PaymentView.as_view(), name='payment'),
    path('booking/<int:pk_booking>/payment/', PaymentView.as_view(), name='payment'),
    path('booking/finished/<int:pk>/', SaleView.as_view(), name='finished'),
    path('booking/sale/', SaleListView.as_view(), name='sale'),
]
