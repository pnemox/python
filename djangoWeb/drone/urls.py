from django.urls import include, path
from . import views
from rest_framework import routers
from drone import views

router = routers.DefaultRouter()
router.register(r'drones', views.DroneViewSet)

urlpatterns = [
    path('', views.drone_index, name='droneIndex'),
    path('drones_with_api', views.drones_with_api, name="'droneViewApi"),
    path('api/', include(router.urls)),
    # path('drone-api/', include('rest_framework.urls', namespace='rest_framework'))
]
