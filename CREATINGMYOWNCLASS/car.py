class Car:
    def __init__(self,make,model,year,speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self,speed):
        self.speed += speed
        print(f"the {self.make + " " + self.model} is now going {self.speed} km/h")
    def brake(self,speed):
        self.speed -= speed
        print(f"the {self.make + " " + self.model} is now going {self.speed} km/h")
my_car = Car(make="BMW",model="BMW Vision M Next",year="2014",speed=10000000000000000)
my_car.accelerate(100000000)
my_car.brake(1000000000)
