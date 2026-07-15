class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def days(self):
        self.age += 1

    def grow(self):
        self.height += 0.8

    def printt(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def ft_plant_growth():
    plant1 = Plant("Rose", 30, 25.0)

    print("=== Garden Plant Growth ===")
    plant1.printt()

    tmp_height = plant1.height

    i = 1
    while i <= 7:
        print(f"=== Day {i} ===")
        plant1.days()
        plant1.grow()
        plant1.printt()
        i += 1

    print(f"Growth this week: {plant1.height - tmp_height:.1f}cm")


if __name__ == "__main__":
    ft_plant_growth()
