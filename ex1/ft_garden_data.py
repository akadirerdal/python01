#!/usr/bin/env python3
class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def printt(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 30, 25)
    plant2 = Plant("Sunflower", 45, 80)
    plant3 = Plant("Cactus", 120, 15)
    print("=== Garden Plant Registry ===")
    plant1.printt()
    plant2.printt()
    plant3.printt()
