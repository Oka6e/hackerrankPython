# __INTERFACE__
# No Implmentations and no constructors
# Interface is collection of abstract methods and constants (blueprint for designing classes)
# python interface does not have an interface syntax
    # aka API aka Protocol
# used so we don't rely on python's duck typing
# Abstract base classes let you define a class with abstract methods
#   All Subclasses must implements in order to be initialized
# __METACLASS__
# Evyerthing in python is an object
# the type for an object is the class
# the type for a class is type
#   Call metaclass to initialize a class

from abc import ABC, abstractmethod #ABC is an empty class, sets its metaclass to ABCMeta (where work is done)

class NetworkInterface(ABC): # decorator: func that uses another func, but specializes it w/o modifying it

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def transfer(self):
        pass


class RealNetwork(NetworkInterface):

    def connect(self):
        # connect to something for real
        return

    def transfer(self):
        # transfer a bunch of data
        return


class FakeNetwork(NetworkInterface):

    def connect(self):
        # don't actually connect to anything!
        return

    def transfer(self):
        # don't transfer anything!
        return

#Defines a class dynamically
# Using this method __new__ and __init__ of metaclass are executed before instantiation
# can't modify behavior of type direcly but by overriding in a subclass
def init(self):
    self.x = 10

Foo = type('Foo', (object,), {'__init__': init})
a = Foo()
a.x # returns 10


# __Interface vs Abstract Classes
# 1. If there are common features for all classes use Abstract classes
#     If the features are implemented different for all classes, use an interface
# 2. Abstract class have subclasses
#     Interface is written for implementation to be dealt with by a third party
# 3. Abstract class is a collection of abstract and/or concrete methods 
#     Concrete class is a collection of only abstract methods
# 4. Abstract class can have instance variables
#     Concrete class cannot have instance variables
#         no variables but constants
# 5. Abstract methods are implemented in its subclass
#     abstract methods of interfaces are implements in the implmentation class
# 6. Declaration of abstract class we use an abstract keyword
#     Declaration of interface class we use an interface keyword
