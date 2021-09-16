# lab work
# This Class violates all SOLID Principles, fix it in a Logical way ;
import abc
import Needs

class Greeting():
    @abc.abstractmethod
    def say_hello(self, lang: str):
        pass
# Open - Closed priniciple
class ArabicGreeting(Greeting):
    def say_hello(self, lang: str):
        return 'مرحبا'
# Single Responsibility principle
class TaxCalculator():
    def calculate_tax(self, percentage: int):
        self.salary = self.salary * percentage



# I'm not sure what class the classes below should inherit from. 
# If it is "Needs" class, then they are supposed to implement all abstract classes
# If they stand by themselves -> no connection to "Human"
# Same confusion with methods:
# - get_married(self)
# - own_company(self)
# - become_employee(self)
# They all seem to be Interface segregation, should they be saparated in the same way?

class Prayer():
    def pray(self):
        pass

class Player():
    def play_sports(self):
        pass



class Human(Needs, ArabicGreeting, TaxCalculator): 
    def __init__(self, name: str, nickname: str, salary: int, hobbies):
        self.name = name
        self.nickname = nickname
        self.salary = salary
        self.hobbies = hobbies

    # This part seems to cause Dep. Inversion
    def add_hobby(self, hobby: str) -> int:
        self.hobbies.append(hobby)
        return len(self.hobbies)

    def create_nickName(self, post_fix: str):
        self.nickname = self.name + post_fix
    
    #? May violate I
    @abc.abstractmethod
    def get_married(self):
        pass
    #? May violate I
    @abc.abstractmethod
    def own_company(self):
        pass
    #? May violate I
    @abc.abstractmethod
    def become_employee(self):
        pass

#Did't find Liskov principle(
human = Human()

