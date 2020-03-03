class Dog:
  #A simple attempt to model a dog.

  def __init__(self, name, age):
    #__init__ con due underscore gets called automatically on each new dog created

    self.name = name
    self.age = age
  
  def sit(self):
    print(f"{self.name} is now sitting!!!")

  def roll_over(self):
    print(f"{self.name} is now rolling over!!!")

iron = Dog("Iron", 3)
iron.sit()
iron.roll_over

class Car:

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.make} {self.model}"
    return long_name.title()

  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")
  

my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()