def add(*args):
    """
    args simply means arguments: It is a way in python
    to pass unlimited or unspecified numbers of arguments to your function.
    It does this by packing the arguments into a tuple and as such we can
    actually access the arguments using the index like this args[i]
    """
    result = 0
    for n in args:
        result += n
    print(result)


add(3, 4, 8, 9, 12, 17, 17, 8, 90)
add(1, 2, 3)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)