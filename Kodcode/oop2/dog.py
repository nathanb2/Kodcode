from oop2.animal import Animal

SPEED_STEP_FACTOR = 3


class Dog(Animal):

    def __init__(self, age_param: int, step_by_min_param: int):
        Animal.__init__(self, age_param)
        self.step_by_minute = step_by_min_param

    def get_max_speed(self) -> float:
        max_speed = 0

        max_speed = self.step_by_minute * SPEED_STEP_FACTOR

        return max_speed

    def present_my_self(self) -> None:
        print("__________ Hello I'm an animal, my name is", self.name,
              ", I'm", self.age, "years old")
