from lib.Drone import Drone


# test Drone object
class TestDrone:

    __droneName = "Test 1"
    __droneSpeed = 30
    __droneElevation = 100

    __droneObj = Drone(__droneName, __droneSpeed, __droneElevation)

    def test_name(self):
        assert self.__droneObj.name == "Test 1"

    def test_speed(self):
        assert self.__droneObj.speed == 30

    def test_elevation(self):
        assert self.__droneObj.elevation == 100

    def test_crash(self):
        self.__droneObj.elevation = -10
        assert self.__droneObj.status() == 'Drone "Test 1" crashed'

    def test_unique_id(self):
        __droneObj2 = Drone(self.__droneName, self.__droneSpeed, self.__droneElevation)
        assert self.__droneObj.getID() != __droneObj2.getID()

