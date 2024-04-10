from oop2.animal import Animal
from oop2.cooking_capabilities import Cooking_capabilities_interface

SPEED_WINGS_FACTOR = 23.4
class Bird(Animal, Cooking_capabilities_interface):

    def __init__(self, age_param):
        Animal.__init__(self, age_param)
        self.wings_length: int = 1

    def get_max_speed(self)-> float:
        max_speed = 0

        max_speed = self.wings_length * SPEED_WINGS_FACTOR

        return max_speed

    def cook(self, duration: int) -> None:
        print("Tembel I'm a bird!!!!!")

    def bake(self, duration: int) -> None:
        pass

    def fried(self, duration: int) -> None:
        pass
