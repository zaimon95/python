#!/usr/bin/env python3

def check_temperature(temp_str) -> str:
    print(f"Testing temperature: {temp_str}")
    try:
        temp_str = (int(temp_str))
        if (temp_str >= 0 and temp_str <= 40):
            print(f"Temperature {temp_str}°C is perfect for plants!\n")
            return (temp_str)
        elif (temp_str < 0):
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)\n")
        elif (temp_str > 40):
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)\n")
    except ValueError:
        print(f"Error: {temp_str} is not a valid number\n")
    return temp_str


def test_temperature_input() -> None:
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
