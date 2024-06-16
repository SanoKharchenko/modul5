class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


Buld1 = Building(2, 'Магазин')
Bild2 = Building(4,'Квартира')
print(Buld1 == Bild2)