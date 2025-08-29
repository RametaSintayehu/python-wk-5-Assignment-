#create class for car 
class Car:
    def move(self):
        print("Driving") 
        #create class for plane
class Plane:
    def move(self):
        print("Flying") 
        #create class for Dog 
class Dog:
    def move(self):
        print("Running") 
        #--let"s use the classes
        car=car()      #create object of car class
        plane=plane()  #create object of plane class
        dog=dog()      #create object of dog class 

        #call the move method of each class 
        car.move() 
        plane.move() 
        dog.move() 