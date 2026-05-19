from fastapi import APIRouter, Query, HTTPException, Response
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc
from app.database import SessionLocal
from app.models import Profile
from app.schemas import ProfileOut, ProfilesResponse, ErrorResponse
from app.utils import parse_natural_language_query
from typing import Optional

router = APIRouter()

SORTABLE_FIELDS = {"age", "created_at", "gender_probability"}
ORDER_MAP = {"asc": asc, "desc": desc}

# Helper to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/profiles", response_model=ProfilesResponse)
def get_profiles(
    response: Response,
    gender: Optional[str] = None,
    age_group: Optional[str] = None,
    country_id: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    min_gender_probability: Optional[float] = None,
    min_country_probability: Optional[float] = None,
    sort_by: Optional[str] = Query("created_at"),
    order: Optional[str] = Query("desc"),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    db: Session = next(get_db())
):
    # Validate sort_by and order
    if sort_by not in SORTABLE_FIELDS or order not in ORDER_MAP:
        response.status_code = 422
        return {"status": "error", "message": "Invalid query parameters"}
    filters = []
    if gender:
        filters.append(Profile.gender == gender)
    if age_group:
        filters.append(Profile.age_group == age_group)
    if country_id:
        filters.append(Profile.country_id == country_id)
    if min_age is not None:
        filters.append(Profile.age >= min_age)
    if max_age is not None:
        filters.append(Profile.age <= max_age)
    if min_gender_probability is not None:
        filters.append(Profile.gender_probability >= min_gender_probability)
    if min_country_probability is not None:
        filters.append(Profile.country_probability >= min_country_probability)
    q = db.query(Profile).filter(and_(*filters))
    total = q.count()
    q = q.order_by(ORDER_MAP[order](getattr(Profile, sort_by)))
    q = q.offset((page - 1) * limit).limit(limit)
    data = q.all()
    return {
        "status": "success",
        "page": page,
        "limit": limit,
        "total": total,
        "data": data
    }

@router.get("/profiles/search", response_model=ProfilesResponse, responses={422: {"model": ErrorResponse}})
def search_profiles(
    response: Response,
    q: str = Query(...),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=50),
    db: Session = next(get_db())
):
    filters = parse_natural_language_query(q)
    if not filters:
        response.status_code = 422
        return {"status": "error", "message": "Unable to interpret query"}
    db_filters = []
    if filters.get("gender"):
        db_filters.append(Profile.gender == filters["gender"])
    if filters.get("age_group"):
        db_filters.append(Profile.age_group == filters["age_group"])
    if filters.get("country_id"):
        db_filters.append(Profile.country_id == filters["country_id"])
    if filters.get("min_age"):
        db_filters.append(Profile.age >= filters["min_age"])
    if filters.get("max_age"):
        db_filters.append(Profile.age <= filters["max_age"])
    qset = db.query(Profile).filter(and_(*db_filters))
    total = qset.count()
    qset = qset.order_by(desc(Profile.created_at)).offset((page - 1) * limit).limit(limit)
    data = qset.all()
    return {
        "status": "success",
        "page": page,
        "limit": limit,
        "total": total,
        "data": data
    }
