from typing import Optional, Dict
import re

COUNTRY_MAP = {
    "nigeria": "NG",
    "angola": "AO",
    "kenya": "KE",
    # Add more as needed
}

AGE_GROUPS = ["child", "teenager", "adult", "senior"]

# Rule-based parser for /api/profiles/search
# Returns dict of filters or None if cannot parse

def parse_natural_language_query(q: str) -> Optional[Dict]:
    q = q.lower().strip()
    filters = {}
    # Gender
    if "male" in q and "female" in q:
        filters["gender"] = None  # Both
    elif "male" in q:
        filters["gender"] = "male"
    elif "female" in q:
        filters["gender"] = "female"
    # Age group
    for group in AGE_GROUPS:
        if group in q:
            filters["age_group"] = group
    # Young
    if "young" in q:
        filters["min_age"] = 16
        filters["max_age"] = 24
    # Above/below
    m = re.search(r"above (\d+)", q)
    if m:
        filters["min_age"] = int(m.group(1))
    m = re.search(r"below (\d+)", q)
    if m:
        filters["max_age"] = int(m.group(1))
    # Between
    m = re.search(r"between (\d+) and (\d+)", q)
    if m:
        filters["min_age"] = int(m.group(1))
        filters["max_age"] = int(m.group(2))
    # Country
    for cname, cid in COUNTRY_MAP.items():
        if cname in q:
            filters["country_id"] = cid
    # From country
    m = re.search(r"from ([a-z ]+)", q)
    if m:
        cname = m.group(1).strip()
        if cname in COUNTRY_MAP:
            filters["country_id"] = COUNTRY_MAP[cname]
    # If no filters found, return None
    if not filters:
        return None
    return filters
