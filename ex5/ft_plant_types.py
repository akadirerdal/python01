class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def printt(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def printt(self):
        super().printt()
        print(f" Color: {self.color}")

    def bloom(self, value):
        if value == 0:
            print(
                f" {self.name} has not bloomed yet\n"
                f"[asking the {self.name} to bloom]"
            )
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, td):
        super().__init__(name, height, age)
        self.td = td

    def printt(self):
        super().printt()
        print(f" Trunk diameter: {self.td}cm")

    def produce_shade(self, value):
        if value == 0:
            print(f"[asking the {self.name} to produce shade]")
        else:
            print(
                f"Tree {self.name} now produces a shade of "
                f"{self.height}cm long and {self.td}cm wide."
            )


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height,
        age,
        harvest_time,
        nutritional_value,
    ):
        super().__init__(name, height, age)
        self.harvest_time = harvest_time
        self.nutritional_value = nutritional_value

    def printt(self):
        super().printt()
        print(
            f" Harvest season: {self.harvest_time}\n"
            f" Nutritional value: {self.nutritional_value}"
        )

    def grow(self):
        if self.age < 30:
            print(
                f"[make {self.name} grow and age "
                f"for {30 - self.age} days]"
            )


def ft_plant_types():
    flower = Flower("Rose", 15.0, 10, "Red")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    vegetable1 = Vegetable("Tomato", 5.0, 10, "April", 0)

    print("=== Garden Plant Types ===")

    print("=== Flower")
    flower.printt()
    flower.bloom(0)
    flower.printt()
    flower.bloom(1)

    print("\n=== Tree")
    tree1.printt()
    tree1.produce_shade(0)
    tree1.produce_shade(1)

    print("\n=== Vegetable")
    vegetable1.printt()
    vegetable1.grow()

    vegetable1 = Vegetable("Tomato", 47.0, 30, "April", 20)
    vegetable1.printt()


if __name__ == "__main__":
    ft_plant_types()
