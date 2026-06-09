from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="ISS",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-05-01T12:00:00"
    )

    print("Valid station created:", station)

    print("\n" + "=" * 40)

    try:
        SpaceStation(
            station_id="BAD",
            name="Bad Station",
            crew_size=50,  # ❌ erreur
            power_level=150.0,  # ❌ erreur
            oxygen_level=50.0,
            last_maintenance="2024-05-01T12:00:00"
        )
    except ValidationError as e:
        print(f"Expected validation error: {e}")


if __name__ == "__main__":
    main()
