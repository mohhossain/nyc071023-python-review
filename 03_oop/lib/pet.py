#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 
    
    
    # {
    #     name: 'Ronil',
    #     age: 23
    # }


class Pet:
    # pass
# 3. ✅ Demonstrate __init__   
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 
    def __init__(self, breed, name, age):
        self.name = name
        self.breed = breed
        self.age = age
    

# class Car:
    
#     def __init__(self, brand, model, year = 2000):
#         self.brand = brand
#         self.year = year
#         self.model = model

# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg
            
    def print_pet_details(self):
        print(f'name: {self.name} \nage: {self.age} \nbreed: {self.breed}')

    # def __str__(self):
    #     return f'The pet name is {self.name}, it is {self.age} year old, and a {self.breed}'

    def __repr__(self):
        return f'name: {self.name} \nage: {self.age} \nbreed: {self.breed}'
# Demonstrate instances 
    # Different Instances are Different Objects
# Demonstrate __init__
# Demonstrate instance method
# Demonstrate the self keyword 
# Stretch Goals
# Demonstrate object properties

class Car:
    
    def __init__(self, brand, model, year = 2000):
        self.brand = brand
        self.year = year
        self.model = model
        self.speed = 0
        
    def drive(self):
        self.speed = 50
        return 'The car is driving'
    
    def accelerate(self):
        self.speed += 10
        return f'The speed now is {self.speed}mph'
    
    def stop(self):
        self.speed = 0
        return 'The car stopped!'

# Instances 

# Run in ipdb session
# rose == cookie
#   False

#Read Attributes 
# rose.name -> rose
# rose.age -> 11

#Update
# rose.age -> 11
# rose.age = 12
# rose.age -> 12

