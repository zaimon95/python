from sys import argv


def display_command_info(args: list[str]) -> None:
    """Display command-line argument information."""
    print("=== Command Quest ===")
    program_name: str = args[0]

    if len(args) == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {len(args)}")
        return

    print(f"Program name: {program_name}")
    print(f"Arguments received: {len(args) - 1}")

    for i, arg in enumerate(args[1:], start=1):
        print(f"Argument {i}: {arg}")

    print(f"Total arguments: {len(args)}")


def main() -> None:
    """Entry point for Command Quest."""
    display_command_info(argv)


if __name__ == "__main__":
    main()
