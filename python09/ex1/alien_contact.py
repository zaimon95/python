from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_rules(self):
        # ID doit commencer par AC
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        # Physical → doit être vérifié
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact must be verified")

        # Telepathic → ≥ 3 témoins
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        # Signal fort → message obligatoire
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals require a message")

        return self


def main():
    print("Alien Contact Validation")
    print("=" * 40)

    contact = AlienContact(
        contact_id="AC_001",
        timestamp="2024-05-01T10:00:00",
        location="Area 51",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=30,
        witness_count=5,
        message_received="Hello humans"
    )

    print("Valid contact:", contact)

    print("\n" + "=" * 40)

    try:
        AlienContact(
            contact_id="BAD001",  # ❌ erreur
            timestamp="2024-05-01T10:00:00",
            location="Mars",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=0  # ❌ erreur
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()
