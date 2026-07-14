class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        self.stats = self.stats()

    def printt(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.stats.total_print += 1

    @staticmethod
    def year_checker(days):
        return days > 365
    
    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0.0, 0)
    
    def grow(self):
        self.height += 0.8
        self.stats.total_grow += 1
    
    def age(self):
        self.age += 1
        self.stats.total_age += 1

    def stats_print(self):
        self.stats.printt()

    class stats:
        def __init__(self):
            self.total_grow = 0
            self.total_height = 0
            self.total_print = 0
        
        def printt(self):
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.total_grow} grow, {self.total_age} age, {self.total_print} show")
    
    
class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    
    def printt(self):
        super().printt()
        print(f" Color: {self.color}")
    
    def Bloom(self, value):
        if value == 0:
            print(f"[asking the {self.name} to grow and bloom]")
        elif value == 1:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")

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
            return
    
    def shade(self,value):
        if value :
            print(f"{value} shade")
        else :
            return
        
class Seed(Plant):
    def __init__(self, name, height, age, color, seeds):
        super().__init__(name, height, age)
        self.color = color
        self.seeds = seeds

    def printt(self):
        super().printt()
        print(f" Color: {self.color}")

    def bloom(self, value):
        if value == 0:
            print(f"{self.name} has not bloomed yet")
            Seed.print_seeds()
            print(f"[make {self.name} grow, age and bloom]")
        else:
            print(f"{self.name} is blooming beautifully!")
            Seed.print_seeds()

    def print_seeds(self):
        print(f"Seeds: {self.seeds}")

class Anonymous(Plant):
    def printt():
        print("Unknown plant: 0.0cm, 0 days old")
        print("[statistics for Unknown plant]")
        print("Stats: 0 grow, 0 age, 1 show")

def display(plant):
    print(f"[statistics for {plant.name}]")
    plant.stats_printt()

def ft_garden_analytics():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.year_checker(30)}")
    print(f"Is 400 days more than a year? -> {Plant.year_checker(400)}\n")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    Flower.printt(rose)
    Flower.Bloom(1)
    display(rose)
    Plant.stats(rose)
    rose = Flower("Rose", 23.0, 10 , "red")
    Flower.Bloom(0)
    Flower.printt(rose)
    Flower.Bloom(10)
    display(rose)
    Flower.stats(rose)
    print("\n")
    print("=== Tree")
    tree1 = Tree("Oak", 200.0, 365, 5.0)
    Tree.printt(tree1)
    display(tree1)
    Tree.stats(tree1)
    Tree.shade(0)
    Tree.produce_shade(0)
    print(f"Tree Oak now produces a shade of {tree1.height}cm long and {tree1.td}cm wide.")
    display(tree1)
    Tree.stats(tree1)
    Tree.shade(1)
    print("=== Seed")
    seed1 = Seed("Sunflower", 80.0, 45, "yellow", 0)
    Seed.printt(seed1)
    Seed.bloom(0)
    seed1 = Seed("Sunflower", 110.0, 65, "yellow", 42)
    Seed.printt(seed1)
    Seed.bloom(1)
    display(seed1)
    Seed.stats(seed1)
    print("\n")
    print("=== Anonymous")
    Anonymous.printt()

if __name__ == "__main__":
    ft_garden_analytics()