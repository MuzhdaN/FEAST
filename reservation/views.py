from .models import Table
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import reserveTableForm

from reservation.models import Table


# Create your views here.
def reserve_table(request):
    booking_form = reserveTableForm()
    
    if request.method == 'POST':
        booking_form = reserveTableForm(request.POST)

        if booking_form.is_valid():
            booking_form.save()
            booking_form = reserveTableForm()
            messages.success(
                request, "Booking succesful")
            return render(
                # redirect to confirmation page
                request, 'reservation/reservation.html', {'form': booking_form})       
        else:
            booking_form = reserveTableForm()
            return render(request, 'reservation/reservation.html', {'form': booking_form})
    context = {'form': booking_form}
    return render(request, 'reservation/reservation.html', context)
