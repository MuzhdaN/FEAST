from .models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import bookingForm

from reservation.models import Table


# Create your views here.
# filling the form 
def reserve_table(request):
    form = bookingForm()
    
    if request.method == 'POST':
        form = bookingForm(request.POST)

        if form.is_valid():
            form.save()
            form = bookingForm()
            messages.success(request, "Booking succesful")
            return redirect('/myBooking_list') 

            #will come back to form page and show success msg (Should be directed to other page)
            # return render(request, 'reservation/myBookings.html', {'form': form})       
        else:
            # form = bookingForm()
            return render(request, 'reservation/reservation.html', {'form': form})
    context = {'form': form}
    return render(request, 'reservation/reservation.html', context)


def myBooking_list(request):
    bookings = Table.objects.all()
    return render((request), "reservation/myBookings.html", {'bookings': bookings})


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
    

