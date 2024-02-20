class Empty:
    pass  # empty class


# self + dot + something = ATTRIBUTE
# attributes can be used in any function from the class, not like local variables which can only be used where defined
# attributes are special variables attached to the object (internal variables of the object)

# methods are functions inside the class

# INIT METHOD: used when you want to create an object, and initializes(creates) the object
# its good practice to have all attributes in init method, but you can add them on the fly
class Car:
    def __init__(self, brand):  # self=object itself, this parameter is always expected as the first of a method
        # when you move from class to object you use the init method, if it's not there, nothing happens
        self.car_brand = brand  # brand is a local variable that can only be used in this function
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        return 100

    def get_speed(self):
        return self.speed

    def get_brand_nationality(self):
        if self.car_brand == "renault":
            return "France"
        elif self.car_brand == "ferrari":
            return "Italy"


# my_car and your_car are objects, and in each method, they act as "self" since they are before the dot
my_car = Car("renault")
print(my_car.get_speed())  # speed is 0
my_car.set_speed(80)
print(my_car.get_speed())  # speed is 80

print(my_car.get_brand_nationality())

your_car = Car("ferrari")
print(your_car.speed)  # these two lines act the same way
print(your_car.get_speed())

