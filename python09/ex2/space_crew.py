from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import List
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission(self):
        # ID commence par M
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Au moins un captain ou commander
        if not any(member.rank in [Rank.captain, Rank.commander]
           for member in self.crew):
            raise ValueError("Mission must have a Captain or Commander")

        # Missions longues → 50% expérimentés
        if self.duration_days > 365:
            experienced = [m for m in self.crew if m.years_experience >= 5]
            if len(experienced) < len(self.crew) / 2:
                raise ValueError("Long missions need 50% experienced crew")

        # Tous actifs
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main():
    print("Space Mission Validation")
    print("=" * 40)

    mission = SpaceMission(
        mission_id="M00115",
        mission_name="Mars Mission",
        destination="Mars",
        launch_date="2025-01-01T00:00:00",
        duration_days=400,
        budget_millions=500.0,
        crew=[
            {
                "member_id": "001",
                "name": "Alice",
                "rank": "commander",
                "age": 40,
                "specialization": "Pilot",
                "years_experience": 10
            },
            {
                "member_id": "002",
                "name": "Bob",
                "rank": "officer",
                "age": 35,
                "specialization": "Engineer",
                "years_experience": 6
            }
        ]
    )

    print("Valid mission:", mission)

    print("\n" + "=" * 40)

    try:
        SpaceMission(
            mission_id="X001",  # ❌ erreur
            mission_name="Fail Mission",
            destination="Moon",
            launch_date="2025-01-01T00:00:00",
            duration_days=100,
            budget_millions=100.0,
            crew=[]
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
