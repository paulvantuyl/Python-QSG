# Include the dataclases module
from dataclasses import dataclass

# Define a new class
@dataclass
class Customer:
    name: str
    city: str

# Dataclass features
    # The init argument instructs dataclass decorator to auto generate 
    # __init__ method (default = True)
    # 
    # The repr argument allows our class to represent itself as a 
    # string (default = True)
    # 
    # The eq argument allows for comparison of 2 objects from same class 
    # using the == operator (default = True)
    # 
    # The order argument (default = False) creates the __lt__, __le__,
    # __gt__, and __ge__ methods (<, <=, >, >=). Similar to 
    # eq argument, allow for comparisons
    # 
    # The frozen argument makes objects from this class read only when
    # set to True
@dataclass(init=True, repr=True, eq=True, order=False, frozen=False)