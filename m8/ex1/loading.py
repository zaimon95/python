import sys
import importlib


DEPENDENCIES = ["pandas", "numpy", "matplotlib"]


def check_dependencies() -> bool:
    """Check required packages."""
    print("Checking dependencies:")
    all_ok = True

    for package in DEPENDENCIES:
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version})")
        except ImportError:
            print(f"[MISSING] {package}")
            all_ok = False

    return all_ok


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    try:
        if not check_dependencies():
            print("\nInstall dependencies:")
            print("pip install -r requirements.txt")
            print("or")
            print("poetry install")
            sys.exit(1)

        import numpy as np
        import pandas as pd
        import matplotlib.pyplot as plt

        print("\nAnalyzing Matrix data...")

        data = np.random.normal(50, 15, 1000)

        df = pd.DataFrame({"signal_strength": data})

        print(f"Processing {len(df)} data points...")

        plt.hist(df["signal_strength"], bins=30)
        plt.title("Matrix Signal Analysis")
        plt.xlabel("Signal Strength")
        plt.ylabel("Frequency")

        plt.savefig("matrix_analysis.png")

        print("Generating visualization...")
        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    except ImportError:
        print("ERROR")


if __name__ == "__main__":
    main()
