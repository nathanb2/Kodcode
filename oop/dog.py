from oop.animal import Animal


class Dog(Animal):

    def __init__(self, age, name):
        Animal.__init__(self, age, name)
        self.aba = 0
        self.necklace_color = ""
        #return new dog

    def get_name(self):
        return self._name

