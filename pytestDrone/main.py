from lib.Drone import Drone


# Create drone object and report status
# -- Unit testing for the Drone class is located in the "test" folder
def main():
    print("App Start")
    print("-" * 40)
    skywalker = Drone("Red 5", 50, 140)
    print(skywalker.status())


if __name__ == '__main__':
    main()
