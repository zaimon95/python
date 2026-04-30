PLAYERS_DATA: list[dict[str, int | str | bool]] = [
    {"name": "alice", "score": 2300, "active": True, "region": "north"},
    {"name": "bob", "score": 1800, "active": True, "region": "east"},
    {"name": "charlie", "score": 2150, "active": True, "region": "central"},
    {"name": "diana", "score": 2050, "active": False, "region": "north"},
    {"name": "eve", "score": 950, "active": False, "region": "east"},
    {"name": "frank", "score": 1200, "active": True, "region": "central"},
]

ACHIEVEMENTS_DATA: list[dict[str, str]] = [
    {"player": "alice", "achievement": "first_kill"},
    {"player": "alice", "achievement": "level_10"},
    {"player": "alice", "achievement": "boss_slayer"},
    {"player": "alice", "achievement": "speed_demon"},
    {"player": "alice", "achievement": "treasure_hunter"},
    {"player": "bob", "achievement": "first_kill"},
    {"player": "bob", "achievement": "level_10"},
    {"player": "bob", "achievement": "collector"},
    {"player": "charlie", "achievement": "level_10"},
    {"player": "charlie", "achievement": "boss_slayer"},
    {"player": "charlie", "achievement": "perfectionist"},
    {"player": "charlie", "achievement": "speed_demon"},
    {"player": "charlie", "achievement": "treasure_hunter"},
    {"player": "charlie", "achievement": "collector"},
    {"player": "charlie", "achievement": "first_kill"},
]


def list_comprehension_examples() -> None:
    print("=== List Comprehension Examples ===")

    high_scorers: list[str] = [
        str(p["name"]) for p in PLAYERS_DATA if int(str(p["score"])) > 2000
    ]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled: list[int] = [
        int(str(p["score"])) * 2
        for p in PLAYERS_DATA
        if int(str(p["score"])) > 2000
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = [
        str(p["name"]) for p in PLAYERS_DATA if p["active"]
    ]
    print(f"Active players: {active_players}")


def dict_comprehension_examples() -> None:
    print()
    print("=== Dict Comprehension Examples ===")

    player_scores: dict[str, int] = {
        str(p["name"]): int(str(p["score"]))
        for p in PLAYERS_DATA
        if p["active"]
    }
    print(f"Player scores: {player_scores}")

    score_categories: dict[str, int] = {
        "high": len([p for p in PLAYERS_DATA if int(str(p["score"])) >= 2000]),
        "medium": len([
            p for p in PLAYERS_DATA
            if 1000 <= int(str(p["score"])) < 2000
        ]),
        "low": len([p for p in PLAYERS_DATA if int(str(p["score"])) < 1000]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts: dict[str, int] = {
        name: len([a for a in ACHIEVEMENTS_DATA if a["player"] == name])
        for name in {a["player"] for a in ACHIEVEMENTS_DATA}
    }
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension_examples() -> None:
    print()
    print("=== Set Comprehension Examples ===")

    unique_players: set[str] = {str(p["name"]) for p in PLAYERS_DATA}
    print(f"Unique players: {unique_players}")

    unique_achievements: set[str] = {
        a["achievement"] for a in ACHIEVEMENTS_DATA
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions: set[str] = {
        str(p["region"]) for p in PLAYERS_DATA if p["active"]
    }
    print(f"Active regions: {active_regions}")


def combined_analysis() -> None:
    print()
    print("=== Combined Analysis ===")

    total_players: int = len({str(p["name"]) for p in PLAYERS_DATA})
    print(f"Total players: {total_players}")

    total_achievements: int = len(
        {a["achievement"] for a in ACHIEVEMENTS_DATA}
    )
    print(f"Total unique achievements: {total_achievements}")

    all_scores: list[int] = [int(str(p["score"])) for p in PLAYERS_DATA]
    avg_score: float = sum(all_scores) / len(all_scores)
    print(f"Average score: {avg_score}")

    achievement_counts: dict[str, int] = {
        str(p["name"]): len(
            [a for a in ACHIEVEMENTS_DATA if a["player"] == p["name"]]
        )
        for p in PLAYERS_DATA
    }
    top_name: str = max(
        achievement_counts, key=lambda k: (
            int(str(next(
                (p["score"] for p in PLAYERS_DATA if p["name"] == k), 0
            ))),
            achievement_counts[k]
        )
    )
    top_score: int = int(str(
        next(p["score"] for p in PLAYERS_DATA if p["name"] == top_name)
    ))
    top_ach: int = achievement_counts[top_name]
    print(f"Top performer: {top_name} ({top_score} "
          f"points, {top_ach} achievements)")


def main() -> None:
    print("=== Game Analytics Dashboard ===")
    print()
    list_comprehension_examples()
    dict_comprehension_examples()
    set_comprehension_examples()
    combined_analysis()


if __name__ == "__main__":
    main()
