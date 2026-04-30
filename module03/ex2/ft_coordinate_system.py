from math import sqrt
from sys import argv


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    """Create a 3D position tuple."""
    return (x, y, z)


def calculate_distance(
    pos1: tuple[int | float, int | float, int | float],
    pos2: tuple[int | float, int | float, int | float],
) -> float:
    """Calculate Euclidean distance between two 3D positions."""
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinate(coord_str: str) -> tuple[int, int, int]:
    """Parse a coordinate string in 'x,y,z' format into a tuple."""
    parts: list[str] = coord_str.split(",")
    x: int = int(parts[0])
    y: int = int(parts[1])
    z: int = int(parts[2])
    return (x, y, z)


def demonstrate_unpacking(pos: tuple[int, int, int]) -> None:
    """Demonstrate tuple unpacking with a 3D position."""
    x, y, z = pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    """Entry point for Position Tracker."""
    print("=== Game Coordinate System ===")

    origin: tuple[int, int, int] = create_position(0, 0, 0)

    pos1: tuple[int, int, int] = create_position(10, 20, 5)
    print(f"Position created: {pos1}")
    dist1: float = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {round(dist1, 2)}")

    print()
    coord_str: str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        pos2: tuple[int, int, int] = parse_coordinate(coord_str)
        print(f"Parsed position: {pos2}")
        dist2: float = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {round(dist2, 2)}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print()
    invalid_str: str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_str}"')
    try:
        parse_coordinate(invalid_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print()
    print("Unpacking demonstration:")
    if "pos2" in dir():
        demonstrate_unpacking(pos2)

    _ = argv


if __name__ == "__main__":
    main()
