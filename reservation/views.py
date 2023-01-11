from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import bookingForm
from reservation.models import Table


# Create your views here.
def reserve_table(request):
    '''
    this function will show reservation form 
    if the user is registered and then will save it.
    for unregistered user, a message will be shown for sign in
    '''
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
    '''
    This function will show the reservation of the 
    currently logged-in user if she is logged in 
    otherwise sign-in page will be shown
    '''
    # if request.user.is_authenticated:
    bookings = Table.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, "reservation/myBookings.html", context)


def updateBookings(request, booking_id):
    '''
    this function will edit/update the bookings of the user
    '''
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


def deleteBooking(request, booking_id):
    '''
    this function will delete the user's booking from bookings list
    then will reconfirm deletion, after that will redirect the user
    to bookings list
    '''
    booking = Table.objects.get(id=booking_id)
    if request.method == "POST":
        booking.delete()
        return redirect('/myBooking_list')
   
    return render(request, "reservation/delete_booking.html", {'booking': booking}) 