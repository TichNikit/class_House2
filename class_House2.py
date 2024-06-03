class House():
    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

home = House()

home.setNewNumberOfFloors(5)

print(home.numberOfFloors)

home.setNewNumberOfFloors(7)
home.setNewNumberOfFloors(77)
home.setNewNumberOfFloors(777)

print(home.numberOfFloors)