class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def show(self):
        super().show()
        print(f"Clor: {self.color}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season,
                 nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    Flower1 = Flower("Rose", 15.0, 10, "red")
    Flower1.show()
    print("Rose has not bloomed yet")
    print("[asking the rose to bloom]")
    Flower1.show()
    print("Rose is blooming beautifully!")
    print("\n=== Tree")
    Tree1 = Tree("Oak", 200.0, 365, 5.0)
    Tree1.show()
    print("[asking the oak to produce shade]")
    line = (
        f"Tree Oak now produces a shade of {Tree1.height:.1f}cm long and "
        f"{Tree1.trunk_diameter:.1f}cm wide."
    )
    print(line)
    print("\n=== Vegetable")
    Vegetable1 = Vegetable("Tomato", 5.0, 10, "April", 0)
    Vegetable1.show()
    print("[make tomato grow and age for 20 days]")
    Vegetable1 = Vegetable("Tomato", 47.0, 30, "April", 20)
    Vegetable1.show()
