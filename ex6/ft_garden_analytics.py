class Plant:
    class Stats:
        def __init__(self):
            self.growc = 0
            self.agec = 0
            self.showc = 0

        def printt(self):
            print(
                f"Stats: {self.growc} grow, {self.agec} age, {self.showc} "
                f"show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.stats = Plant.Stats()

    @staticmethod
    def year_cheker(days):
        return days > 365

    @classmethod
    def unknownp(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self):
        self.height += 8.0
        self.stats.growc += 1

    def older(self):
        self.age += 1
        self.stats.agec += 1

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.stats.showc += 1

    def show_stats(self):
        self.stats.printt()


class flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloom = False

    def bloomed(self):
        self.bloom = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")

        if self.bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = 0

    def provide_shade(self):
        self.shade += 1
        line = (
            f"Tree {self.name} now produces a shade of {self.height:.1f}cm "
            f"long and {self.trunk_diameter:.1f}cm wide."
        )
        print(line)

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    def show_stats(self):
        super().show_stats()
        print(f"{self.shade} shade")


class seed(flower):
    def __init__(self, name, height, age, color, seeds):
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def grow(self):
        self.height += 30.0
        self.stats.growc += 1

    def show(self):
        super().show()
        print(f"Seeds: {self.seeds}")


def display(plant):
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.year_cheker(30)}")
    print(f"Is 400 days more than a year? -> {Plant.year_cheker(400)}")
    print("\n=== Flower")
    rose = flower("Rose", 15.0, 10, "red")
    rose.show()
    display(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloomed()
    rose.show()
    display(rose)
    print("\n=== Tree")
    oak = tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display(oak)
    print("[asking the oak to produce shade]")
    oak.provide_shade()
    display(oak)
    print("\n=== Seed")
    sunflower = seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age = 65
    sunflower.stats.agec = 1
    sunflower.bloomed()
    sunflower.seeds = 42
    sunflower.show()
    display(sunflower)
    print("=== Anonymous ===")
    unknown = Plant.unknownp()
    unknown.show()
    display(unknown)
