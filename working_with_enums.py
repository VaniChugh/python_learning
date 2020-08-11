from aenum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    
Animal = Enum('Animal', 'ANT BEE CAT DOG')
print Animal
print Animal.ANT
print list(Animal)