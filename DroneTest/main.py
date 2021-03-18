from lib.Drone import Drone


# create drone object and report status
def main():
    print("App Start")
    print("-" * 40)
    skywalker = Drone("Red 5", 50, 140)
    print(skywalker.status())


if __name__ == '__main__':
    main()
