# #class test
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# # create an instance of the Person class
# person1 = Person("Alice", 30)   
# person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.   
# # create another instance of the Person class
# person2 = Person("Bob", 25)
# person2.greet()  # Output: Hello, my name is Bob and I am 25 years old.

# #inheritance test
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)  # call the constructor of the parent class
#         self.student_id = student_id

#     def display_student_info(self):
#         print(f"Student ID: {self.student_id}")
# # create an instance of the Student class
# student1 = Student("Charlie", 20, "S12345")
# student1.greet()  # Output: Hello, my name is Charlie and I am 20 years old.
# student1.display_student_info()  # Output: Student ID: S12345

#test class with methods using basic calculator operations
# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Error: Cannot divide by zero!"
#         return a / b    
# # create an instance of the Calculator class
# calc = Calculator()
# # test the methods
# print(calc.add(10, 5))        # Output: 15  
# print(calc.subtract(10, 5))   # Output: 5
# print(calc.multiply(10, 5))   # Output: 50  
# print(calc.divide(10, 5))     # Output: 2.0
# print(calc.divide(10, 0))     # Output: Error: Cannot divide by zero

#test class using a character class with health, attack and heal methods
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} points.")

    def damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage.")

# create instances of the Character class
character1 = Character("Warrior", 100)
character2 = Character("Mage", 80)
# test the methods
character1.attack(character2)  # Output: Warrior attacks Mage!
character2.damage(20)          # Output: Mage takes 20 damage.  
character1.heal(10)            # Output: Warrior heals for 10 points.
character2.heal(15)            # Output: Mage heals for 15 points.
character1.damage(30)          # Output: Warrior takes 30 damage.

print(f"{character1.name} has {character1.health} health left.")  # Output: Warrior has 80 health left.
print(f"{character2.name} has {character2.health} health left.")  # Output: Mage has 75 health left.