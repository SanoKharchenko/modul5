class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = int(numberOfFloors)
        print(numberOfFloors)

    def setNewNumberOfFloors(self, floors):
        self.floors = floors
        numberOfFloors = floors
        print(numberOfFloors)


f1 = House(0)
f1.setNewNumberOfFloors(10)
