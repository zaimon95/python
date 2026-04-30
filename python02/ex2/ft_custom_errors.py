class GardenError(Exception):

    def __init__(self, message="A garden error occured.") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="There is a problem with a plant.") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="There is a problem with watering.") -> None:
        super().__init__(message)


def main():
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
