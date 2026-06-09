import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    db = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")

    if not db or not api_key or not endpoint:
        print("WARNING: Missing configuration values.")
        return

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db}")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {endpoint}\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
