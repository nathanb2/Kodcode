from oop2.bird import Bird
from oop2.dog import Dog

tooki = Bird(23)
tooki.name = "Patrick"
tooki.wings_length = 2
print(tooki.name)
print(tooki)
print("tooki max speed", tooki.get_max_speed())

nesher = Bird(12)
print(nesher.age)
nesher.age = 34
print(nesher.age)

print(nesher.name)
print(nesher)
print("nesher max speed", nesher.get_max_speed())

nesher = tooki
print(nesher.name)
print(nesher)

x = 2
y = 3
x = y
y = 4
print(x)

rotweiler = Dog(24, 3)
rotweiler.present_my_self()
nesher.present_my_self()

