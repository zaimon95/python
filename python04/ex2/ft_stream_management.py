from sys import stdout, stderr


def run_communication_system() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {archivist_id}: {status_report}",
          file=stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=stderr)
    print("[STANDARD] Data transmission complete", file=stdout)

    print("\nThree-channel communication test successful.")


def main() -> None:
    run_communication_system()


if __name__ == "__main__":
    main()
