from abc import ABC, abstractmethod

class Parent(ABC):
    
    @abstractmethod
    def abc(self):
        print("ABC")
        
        
class Child1(Parent):
    def display(self):
        print("DIsplayed the result")
        
    def abc(self):
        print("ABC from child class")
        
c1 = Child1()
c1.abc()
c1.display()