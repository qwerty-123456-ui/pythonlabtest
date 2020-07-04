# Write a python program to calculate the area of the circle and catch appropriate user defined exception.(Hint: check for invalid radius)

import math
def area(radius):
    if type(radius) is float or type(radius) is int:
        areac=math.pi*radius*radius
    else:
        raise InvalidException("Invalid Radius")

    # print(type(radius))
    return areac

class InvalidException(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
      return(repr(self.value))

try :
    print(area('p'))
except InvalidException as e :
    print("Exception here:" +e.value)

try:
    print(area(2))
except :
    pass

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))