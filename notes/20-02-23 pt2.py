class Car:
    def __init__(self, brand, speed=0):
        self.car_brand = brand
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed


# Ferrari doesn't have an init, so the init that is called is the one of the mother class (Car): INHERITANCE
class Ferrari(Car):
    """def __init__(self):
    # if we set this one, it doesn't use Car init method, Ferrari has its own init, and we lose attributes
    we would have to use super() to call the init of my mother class and add the new attribute: HALF INHERITANCE
        super().__init__("Ferrari")
        self.music = "classic"  # classic music by default"""

    def make_cabrio(self):  # now Ferrari is SPECIALIZED
        self.speed = 20
        self.music = "Loud"
        return "Wow"


my_car = Car("renault")   # my_car doesn't have make_cabrio (method)

your_car = Ferrari("Ferrari")  # we need to give a brand here too, since the init is the same as Car and requires so
print(your_car.car_brand)

print(your_car.speed)  # speed doesn't have to be called since we have that speed=0 (either speed or 0)
your_car.set_speed(120)
print(your_car.speed)

print(your_car.make_cabrio(), "and music is", your_car.music, "and speed is", your_car.speed)
# remember the () for it to run the method


