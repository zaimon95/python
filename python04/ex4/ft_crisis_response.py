def crisis_handler(filename: str) -> None:
    is_routine = filename == "standard_archive.txt"

    if is_routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as vault:
            content = vault.read().strip()
            print(f"SUCCESS: Archive recovered - \"{content}\"")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly detected - {e}")
        print("STATUS: Crisis contained, system stabilized")


def run_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    crisis_handler("lost_archive.txt")
    print()
    crisis_handler("classified_vault.txt")
    print()
    crisis_handler("standard_archive.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


def main() -> None:
    run_crisis_response()


if __name__ == "__main__":
    main()
