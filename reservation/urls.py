from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
    path('myBooking_list/', views.myBooking_list, name='myBooking_list'), 
    path('update_bookings/<booking_id>', views.updateBookings, name='update_bookings'),
    path('delete_booking/<booking_id>', views.deleteBooking, name='delete_booking'),
]
