
class Animal:

    def __init__(self, age_param: int):
        self.name: str = ""
        self.age: int = age_param

    def present_my_self(self) -> None:
        print("Hello I'm an animal, my name is", self.name,
              ", I'm", self.age, "years old")
