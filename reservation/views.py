from .models import Table
from django.shortcuts import render
# from django.http import HttpResponse

from reservation.models import Table


# Create your views here.
def reserve_table(request):
    return render(request, 'reservation/reservation.html')
