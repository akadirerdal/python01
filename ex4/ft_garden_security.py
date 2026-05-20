class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._age = age
        self._height = height

    def show(self):
        print(
            f"Plant created: {self.name}: {self._height:.1f}cm, {self._age} "
            f"days old"
        )

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")
            return self._height

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}:  Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"age update: {self._age} days")
            return self._age

    def total(self):
        print(
            f"Current state: {self.name}: {self._height:.1f}cm, {self._age} "
            f"days old"
        )


if __name__ == "__main__":
    plant1 = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    plant1.show()
    print("\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")
    plant1.set_height(-25)
    plant1.set_age(-30)
    print("\n")
    plant1.total()
