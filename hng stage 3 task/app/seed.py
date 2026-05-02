import json
from sqlalchemy.orm import Session
from app.models import Profile
from app.database import SessionLocal
from uuid6 import uuid7
from datetime import datetime

# Path to your JSON file
data_file = "profiles.json"  # Place the file in the project root

def seed():
    with open(data_file, "r") as f:
        profiles = json.load(f)
    db: Session = SessionLocal()
    for p in profiles:
        # Check for existing by name
        exists = db.query(Profile).filter_by(name=p["name"]).first()
        if exists:
            continue
        db.add(Profile(
            id=uuid7(),
            name=p["name"],
            gender=p["gender"],
            gender_probability=p["gender_probability"],
            age=p["age"],
            age_group=p["age_group"],
            country_id=p["country_id"],
            country_name=p["country_name"],
            country_probability=p["country_probability"],
            created_at=datetime.fromisoformat(p["created_at"])
        ))
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()
