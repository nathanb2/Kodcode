class Animal:
    _name = ""
    age = 0

    def __init__(self, age, name):
        self.age = age
        self._name = name
        #return new dog


    def speek(self):
        print(self._name)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if len(name) < 3:
            return "name length can't be less than 3"
        else:
            self._name = name