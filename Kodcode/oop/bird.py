from oop.animal import Animal


class Bird(Animal):

    wings_length = 0

    def __init__(self, age, name, wings_length):
        Animal.__init__(self, age, name)
        self.wings_length = wings_length
        #return new Bird




    def get_name(self):
        return self.name

    def set_name(self, name):
        if len(name) < 3:
            return "name length can't be less than 3"
        else:
            self.name = name