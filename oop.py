class Panther:
    def __init__(self, p_name, p_age, p_gender):
        self.name = p_name
        self.age = p_age
        self.gender = p_gender

    def hunt(self):
        if self.gender == "boy":
            print(f"Mr.{self.name} is hunting")
        else:
            print(f"Miss.{self.name} is hunting")

    def eat(self):
        if self.gender == "boy":
            print(f"Mr.{self.name} good boy, eatup!!")
        else:
            print(f"Miss.{self.name} good girl eatup!!")


panther_1 = Panther("jessi", 5, "boy")
panther_1.hunt()
panther_1.eat()

panther2 = Panther("penny", 6, "girl")
panther2.hunt()
panther2.eat()
