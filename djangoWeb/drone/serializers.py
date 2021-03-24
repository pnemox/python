from drone.models import Drone
from rest_framework import serializers


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = ['name', 'speed', 'elevation']