def secure_read(filename: str) -> str:
    with open(filename, "r") as vault:
        return vault.read()


def secure_write(filename: str, content: str) -> None:
    with open(filename, "w") as vault:
        vault.write(content)


def run_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    # Seed the vault with initial classified content
    secure_write("classified_data.txt",
                 "Quantum encryption keys recovered\n"
                 "Archive integrity: 100%\n")

    print("\nSECURE EXTRACTION:")
    data = secure_read("classified_data.txt")
    for line in data.strip().splitlines():
        print(f"[CLASSIFIED] {line}")

    print("\nSECURE PRESERVATION:")
    secure_write("security_protocols.txt", "New security protocols v2.0\n")
    print("[CLASSIFIED] New security protocols archived")
    print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


def main() -> None:
    run_vault_security()


if __name__ == "__main__":
    main()
