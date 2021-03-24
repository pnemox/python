from django.db import models
import uuid


class Drone(models.Model):
    __droneID = uuid.uuid4()
    name = models.CharField(max_length=100)
    speed = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # mph
    elevation = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # ft

    def status(self):
        if self.elevation == 0 and self.speed == 0:
            return 'Drone "{}" parked'.format(self.name)
        elif self.elevation < 0:
            return 'Drone "{}" crashed'.format(self.name)
        else:
            return 'Drone "{}" speed is {} mph at {} ft'.format(self.name, self.speed, self.elevation)

    def getID(self):
        return self.__droneID
