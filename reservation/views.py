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
            messages.success(
                request, "Booking succesful")
            redirect('/myBooking_list/')
            return render(
                request, 'reservation/myBookings.html', {'form': form})       
        else:
            form = bookingForm()
            return render(request, 'reservation/reservation.html', {'form': form})
    context = {'form': form}
    return render(request, 'reservation/reservation.html', context)


def myBooking_list(request):
    bookings = Table.objects.all()
    return render((request), "reservation/myBookings.html", {'bookings': bookings})