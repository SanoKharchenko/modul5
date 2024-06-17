class Building:
    total = 0

    def __init__(self, object):
        self.object = object
        max_object = 40
        while Building.total < max_object:
            Building.total = object
            print(Building.total)
            object += 1



Build = Building(16)
