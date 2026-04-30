#!/usr/bin/env python3

def garden_operations() -> None:
    try:
        not_int: int = int("abc")
    except ValueError:
        raise
    try:
        print(5/0)
    except ZeroDivisionError:
        raise
    try:
        open("missing.txt")
    except FileNotFoundError:
        raise
    try:
        my_dict = {'name': 'Alice', 'age': 30}
        print(my_dict['missing\\_plant'])
    except KeyError:
        raise


        print(f"Caught KeyError: 'missing\\_plant'")
def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        not_int: int = int("abc")
    except ValueError:
        print(f"Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        print(5/0)
    except ZeroDivisionError:
        print(f"Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        my_dict = {'name': 'Alice', 'age': 30}
        print(my_dict['missing\\_plant'])
    except KeyError:
        print(f"Caught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        print(5/0)
    except (ValueError, FileNotFoundError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")

if __name__ == "__main__":
    test_error_types()
