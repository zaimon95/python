from sys import argv


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        try:
            parts: list[str] = arg.split(":")
            if len(parts) != 2:
                raise ValueError(f"Expected 'item:quantity' "
                                 f":format, got '{arg}'")
            name: str = parts[0]
            quantity: int = int(parts[1])
            inventory.update({name: quantity})
        except ValueError as e:
            print(f"Warning: skipping invalid entry '{arg}': {e}")
    return inventory


def categorize_items(
    inventory: dict[str, int]
) -> dict[str, dict[str, int]]:
    categories: dict[str, dict[str, int]] = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {},
    }
    for item, qty in inventory.items():
        if qty >= 10:
            categories["Abundant"][item] = qty
        elif qty >= 4:
            categories["Moderate"][item] = qty
        else:
            categories["Scarce"][item] = qty
    return categories


def display_inventory(inventory: dict[str, int]) -> None:
    print("=== Inventory System Analysis ===")
    total_items: int = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print()
    print("=== Current Inventory ===")
    sorted_inv: list[tuple[str, int]] = sorted(
        inventory.items(), key=lambda x: x[1], reverse=True
    )
    for item, qty in sorted_inv:
        pct: float = (qty / total_items) * 100
        unit_label: str = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {unit_label} ({pct:.1f}%)")

    print()
    print("=== Inventory Statistics ===")
    most: str = max(inventory, key=lambda k: inventory[k])
    least: str = min(inventory, key=lambda k: inventory[k])
    print(f"Most abundant: {most} ({inventory.get(most)} units)")
    print(f"Least abundant: {least} ({inventory.get(least)} unit)")

    print()
    print("=== Item Categories ===")
    categories: dict[str, dict[str, int]] = categorize_items(inventory)
    for cat_name, items in categories.items():
        if items:
            print(f"{cat_name}: {items}")

    print()
    print("=== Management Suggestions ===")
    restock: list[str] = [
        item for item, qty in inventory.items() if qty <= 1
    ]
    if restock:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("All items sufficiently stocked.")

    print()
    print("=== Dictionary Properties Demo ===")
    keys_str: str = ", ".join(inventory.keys())
    values_str: str = ", ".join(str(v) for v in inventory.values())
    print(f"Dictionary keys: {keys_str}")
    print(f"Dictionary values: {values_str}")
    sample_key: str = list(inventory.keys())[0]
    print(f"Sample lookup - '{sample_key}' in inventory: "
          f"{sample_key in inventory}")


def main() -> None:
    if len(argv) < 2:
        print("Usage: python3 ft_inventory_system.py "
              "item1:qty1 item2:qty2 ...")
        return
    inventory: dict[str, int] = parse_inventory(argv[1:])
    if not inventory:
        print("No valid inventory data provided.")
        return
    display_inventory(inventory)


if __name__ == "__main__":
    main()
