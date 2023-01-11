from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import bookingForm
from reservation.models import Table


# Create your views here.
def reserve_table(request):
    form = bookingForm() 
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            form = bookingForm()
            messages.success(request, "Booking succesful")
            return redirect('/myBooking_list')      
        else:
            form = bookingForm()
            return render(request, 'reservation/reservation.html', {'form': form})
    context = {'form': form}
    return render(request, 'reservation/reservation.html', context)


@login_required
def myBooking_list(request):
    # if request.user.is_authenticated:
    bookings = Table.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, "reservation/myBookings.html", context)


# this function will edit/update the bookings of the user
def updateBookings(request, booking_id):
    edit = Table.objects.get(id=booking_id)
    form = bookingForm(instance=edit)   
    if request.method == 'POST':
        form = bookingForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            form = bookingForm()   
            return redirect('/myBooking_list') 
            messages.success(request, "Booking succesful")
    return render(request, "reservation/edit_booking.html", {'form': form}) 


# this function will confirm the deletion of booking and then delete it
def deleteBooking(request, booking_id):
    booking = Table.objects.get(id=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('/myBooking_list')
   
    return render(request, "reservation/delete_booking.html", {'booking': booking}) 