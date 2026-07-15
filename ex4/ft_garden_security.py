class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def printt(self):
        print(
            f"Plant created: {self.name}: "
            f"{self.height:.1f}cm, {self.age} days old\n"
        )

    def age_up(self, value):
        if value < 0:
            print(
                f"{self.name}: Error, age can't be negative\n"
                "Age update rejected"
            )
        else:
            self.age = value
            print(f"Age updated: {self.age} days")

    def height_up(self, value):
        if value < 0:
            print(
                f"{self.name}: Error, height can't be negative\n"
                "Height update rejected"
            )
        else:
            self.height = value
            print(f"Height updated: {self.height}cm")


def ft_garden_security():
    plant1 = Plant("Rose", 10, 15.0)

    print("=== Garden Security System ===")
    plant1.printt()

    plant1.height_up(25)
    plant1.age_up(30)

    print()

    plant1.height_up(-5)
    plant1.age_up(-10)

    print(
        f"\nCurrent state: {plant1.name}: "
        f"{plant1.height:.1f}cm, {plant1.age} days old"
    )


if __name__ == "__main__":
    ft_garden_security()
