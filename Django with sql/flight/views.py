from django.shortcuts import render
from .models import Flight, Passenger
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flight/index.html", {
        "flight": Flight.objects.all()
    })

def flights(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flight/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights = flight).all
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.post["passengers"]))
        passenger.flights.add(flights)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
