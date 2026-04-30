def create_archive(filename: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {filename}")

    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]

    file = open(filename, "w")
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")
    for i, entry in enumerate(entries, start=1):
        line = f"[ENTRY {i:03d}] {entry}\n"
        file.write(line)
        print(line, end="")
    file.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


def main() -> None:
    create_archive("new_discovery.txt")


if __name__ == "__main__":
    main()
