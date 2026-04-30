#!/usr/bin/env python3


def ft_count_harvest_recursive(day: int | None = None) -> None:
    if day == None:
        ft_count_harvest_recursive(int(input("Days until harvest: ")))
        if day == None:
            print("Harvest time!")
        return
    if day <= -1:
        print(f"harvested {-day} days ago")
        exit(0)
    if day > 1:
        ft_count_harvest_recursive(day - 1)
    print(f"Day {day}")
