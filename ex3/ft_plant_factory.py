class plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(
            f"Created: {self.name}: {self.height:.1f}cm, {self.age} days old"
        )


if __name__ == "__main__":
    plants = [
        plant("Rose", 25.0, 30),
        plant("Oak", 200.0, 365),
        plant("Cactus", 5.0, 90),
        plant("Sunflower", 80.0, 45),
        plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Production ===")
    i = 0
    while i < len(plants):
        plants[i].show()
        i = i + 1
