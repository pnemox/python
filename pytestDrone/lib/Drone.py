# simple test class
import uuid


class Drone:

    def __init__(self, name="Anonymous Drone", speed=0, elevation=0):
        self.__droneID = uuid.uuid4()
        self.name = name
        self.speed = speed  # mph
        self.elevation = elevation  # ft

    def status(self):
        if self.elevation == 0 and self.speed == 0:
            return 'Drone "{}" parked'.format(self.name)
        elif self.elevation < 0:
            return 'Drone "{}" crashed'.format(self.name)
        else:
            return 'Drone "{}" speed is {} mph at {} ft'.format(self.name, self.speed, self.elevation)

    def getID(self):
        return self.__droneID
