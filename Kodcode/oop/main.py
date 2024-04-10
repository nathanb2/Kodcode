from oop.dog import Dog

dog1 = Dog(20, "patrick")
dog1.age = 21
print("the name is currently empty", dog1._name)
print(dog1.age)
dog1._name = "Patrick"
print(dog1._name)

dog2 = Dog(18, "shlomo")
print(dog2._name)

dog2 = dog1
dog1._name = "shlomo"
print(dog2._name)

dog2.speek()
print(dog1._name)

x = 3
y = 2
x = y
y = 5
print(x)


