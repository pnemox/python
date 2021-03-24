from django.shortcuts import render
import requests
from rest_framework.utils import json

from drone.models import Drone
from drone.serializers import DroneSerializer
from rest_framework import viewsets


# this view pulls data directly from the sqlite database as an array
def drone_index(request):
    drones = Drone.objects.all()
    context = {
        'drones': drones
    }
    return render(request, 'drone/index.html', context)


# this view pulls the same data from a webservice API request
def drones_with_api(request):
    response = requests.get('http://127.0.0.1:8000/drone/api/drones/')

    # conversion works for demo but I think it could be done cleaner with a library such as Pickle
    json_raw = response.json()
    drones = []

    for d in json_raw:
        drones.append(Drone(name=d['name'], speed=float(d['speed']), elevation=float(d['elevation'])))

    print("Drone Count: ")
    print(len(drones))

    return render(request, 'drone/drone_view_api.html', {
        'drones': drones
    })




# this creates the API view, normally I'd put this in a separate web app folder but it's just a demo
class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
