import area as area # area is alias and all the functions inside module and can be accessed by .function.
x = area.square(56)
print(x)
area.rectangle(breadth=11, length=16)

#method 2 of calling module
from areaOfDifferentShapes import rectangle, circle #With this we don't have to give module name function can be called directly
from areaOfDifferentShapes import * # To import all
from areaOfDifferentShapes import rectangle
rectangle(12.43, 9.18)


#Method 1 is better because if you import multiple modules haveing same function it will be confusing which one to call