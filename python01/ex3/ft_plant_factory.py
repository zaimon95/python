#!/usr/bin/env python3


class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def __str__(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.days} days)"


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    plants = [rose, oak, cactus, sunflower, fern]
    for x in plants:
        print(x)
    print(f"\nTotal plants created {len(plants)}")
