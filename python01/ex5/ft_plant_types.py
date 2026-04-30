#!/usr/bin/env python3


class Plant:

    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):

    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} is blooming beatifully!")

    def print_flower(self) -> None:
        print(f"{rose.name} ({type(rose).__name__}):", end=" ")
        print(f"{rose.height}cm, {rose.age} days, {rose.color} color")
        self.bloom()
        print()


class Tree(Plant):

    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade: int = (self.height * self.trunk_diameter) // 1000
        print(f"{self.name} provides {shade} square meters of shade")

    def print_tree(self) -> None:
        print(f"{self.name} ({type(self).__name__}):", end=" ")
        print(f"{self.height}cm, {self.age} days,", end=" ")
        print(f"{self.trunk_diameter}cm diameter")
        self.produce_shade()
        print()


class Vegetable(Plant):

    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_veg(self) -> None:
        print(f"{self.name} ({type(self).__name__}):", end=" ")
        print(f"{self.height}cm, {self.age} days,", end=" ")
        print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")
        print()


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.print_flower()
    oak = Tree("Oak", 500, 1825, 50)
    oak.print_tree()
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    tomato.print_veg()
