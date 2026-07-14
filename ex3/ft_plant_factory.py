class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def printt(self):
        print(f"Created: {self.name}: {self.height:.1f}cm, {self.age} days old")

def ft_plant_factory():
    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    i = 0
    while i < len(plants):
        plants[i].printt()
        i += 1

if __name__ == "__main__":
    ft_plant_factory()
