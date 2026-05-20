#!/usr/bin/env python3
class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def printt(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

    def development(self):
        self.height = self.height + 0.8

    def day(self):
        self.age = self.age + 1


if __name__ == "__main__":
    plant1 = Plant("Rose", 30, 25)
    tmp_height = plant1.height
    print("=== Garden Plant Registry ===")
    plant1.printt()
    i = 1
    while i <= 7:
        print(f"=== Day {i} === ")
        plant1.development()
        plant1.day()
        plant1.printt()
        i = i + 1
    print(f"Growth this week: {plant1.height - tmp_height:.1f}cm")
