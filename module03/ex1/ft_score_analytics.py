from sys import argv


def parse_scores(raw_args: list[str]) -> list[int]:
    """Parse and validate score arguments into a list of integers."""
    scores: list[int] = []
    for arg in raw_args:
        try:
            scores.append(int(arg))
        except ValueError as e:
            print(f"Warning: skipping invalid score '{arg}': {e}")
    return scores


def analyze_scores(scores: list[int]) -> None:
    """Calculate and display analytics for a list of scores."""
    print("=== Player Score Analytics ===")

    if not scores:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return

    total: int = sum(scores)
    average: float = total / len(scores)
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")


def main() -> None:
    """Entry point for Score Cruncher."""
    scores: list[int] = parse_scores(argv[1:])
    analyze_scores(scores)


if __name__ == "__main__":
    main()
