from time import time
from typing import Generator


PLAYERS: list[str] = ["alice", "bob", "charlie", "diana", "eve"]
EVENTS: list[str] = ["killed monster", "found treasure", "leveled up",
                     "completed quest", "defeated boss"]


def game_event_stream(
        count: int,
) -> Generator[dict[str, int | str], None, None]:
    for i in range(count):
        player: str = PLAYERS[i % len(PLAYERS)]
        event: str = EVENTS[i % len(EVENTS)]
        level: int = (i % 20) + 1
        yield {"id": i + 1, "player": player, "level": level, "event": event}


def fibonacci_generator() -> Generator[int, None, None]:
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> Generator[int, None, None]:
    candidate: int = 2
    while True:
        is_prime: bool = all(
            candidate % d != 0 for d in range(2, int(candidate ** 0.5) + 1)
        )
        if is_prime:
            yield candidate
        candidate += 1


def process_stream(count: int) -> None:
    print(f"Processing {count} game events...")
    print()

    total_events: int = 0
    high_level_count: int = 0
    treasure_count: int = 0
    level_up_count: int = 0

    start: float = time()

    stream: Generator[dict[str, int | str], None, None] = game_event_stream(
        count
    )

    for event in stream:
        total_events += 1
        level: int = int(event["level"])
        evt_type: str = str(event["event"])

        if total_events <= 3:
            print(
                f"Event {event['id']}: Player {event['player']} "
                f"(level {level}) {evt_type}"
            )
        elif total_events == 4:
            print("...")

        if level >= 10:
            high_level_count += 1
        if "treasure" in evt_type:
            treasure_count += 1
        if "leveled" in evt_type:
            level_up_count += 1

    elapsed: float = time() - start

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {elapsed:.3f} seconds")


def demonstrate_generators() -> None:
    print()
    print("=== Generator Demonstration ===")

    fib_gen: Generator[int, None, None] = fibonacci_generator()
    limit: int = 50
    print(f"Fibonacci sequence (first {limit}):", end=" ")
    for _ in range(limit - 1):
        print(next(fib_gen), end=", ")
    print(next(fib_gen))

    prime_gen: Generator[int, None, None] = prime_generator()
    primes: list[int] = [next(prime_gen) for _ in range(limit)]
    print(f"Prime numbers (first {limit}): "
          f"{', '.join(str(p) for p in primes)}")


def main() -> None:
    """Entry point for Stream Wizard."""
    print("=== Game Data Stream Processor ===")
    print()
    process_stream(1000)
    demonstrate_generators()


if __name__ == "__main__":
    main()
