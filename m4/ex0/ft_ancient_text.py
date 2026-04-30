def recover_ancient_text(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {filename}")

    file = open(filename, "r")
    print("Connection established...")
    print("\nRECOVERED DATA:")
    content = file.read()
    print(content)
    file.close()
    print("Data recovery complete. Storage unit disconnected.")


def main() -> None:
    try:
        recover_ancient_text("ancient_fragment.txt")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()
