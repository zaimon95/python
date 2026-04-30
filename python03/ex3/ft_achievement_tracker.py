def get_player_achievements() -> dict[str, set[str]]:
    alice: set[str] = {
        "first_kill", "level_10", "treasure_hunter", "speed_demon"
    }
    bob: set[str] = {
        "first_kill", "level_10", "boss_slayer", "collector"
    }
    charlie: set[str] = {
        "level_10", "treasure_hunter", "boss_slayer", "speed_demon",
        "perfectionist"
    }
    return {"alice": alice, "bob": bob, "charlie": charlie}


def find_rare_achievements(
    players: dict[str, set[str]]
) -> set[str]:
    all_achievements: list[str] = [
        ach for achievements in players.values() for ach in achievements
    ]
    return {
        ach for ach in all_achievements if all_achievements.count(ach) == 1
    }


def analyze_achievements(players: dict[str, set[str]]) -> None:
    print("=== Achievement Tracker System ===")
    for name, achievements in players.items():
        print(f"Player {name} achievements: {achievements}")

    all_unique: set[str] = set()
    for achievements in players.values():
        all_unique = all_unique.union(achievements)

    sets: list[set[str]] = list(players.values())
    common_all: set[str] = sets[0].intersection(*sets[1:])

    rare: set[str] = find_rare_achievements(players)

    alice_set: set[str] = players["alice"]
    bob_set: set[str] = players["bob"]
    alice_bob_common: set[str] = alice_set.intersection(bob_set)
    alice_only: set[str] = alice_set.difference(bob_set)
    bob_only: set[str] = bob_set.difference(alice_set)

    print()
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}")
    print(f"Common to all players: {common_all}")
    print(f"Rare achievements (1 player): {rare}")
    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_only}")
    print(f"Bob unique: {bob_only}")


def main() -> None:
    players: dict[str, set[str]] = get_player_achievements()
    analyze_achievements(players)


if __name__ == "__main__":
    main()
