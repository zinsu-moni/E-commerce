import os
import sys
from app.models.models import User, Base
from app.db.database import SessionLocal, engine
from app.utils.utils import hash_password, verify_password


os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


Base.metadata.create_all(bind=engine)

db = SessionLocal()


admin_email = "zinsusezonsu@gmail.com"
admin_password = "12345678"

existing_admin = db.query(User).filter(User.email == admin_email).first()
if existing_admin:
    db.delete(existing_admin)
    db.commit()
    print(f"Deleted existing admin")

admin = User(
    username="zinsusezonsu@gmail.com",
    full_name="zinsu dev",
    email=admin_email,
    password=hash_password(admin_password),
    role="user",
    is_admin=0
)

db.add(admin)
db.commit()
db.refresh(admin)


is_valid = verify_password(admin_password, admin.password)
print(f"Admin created: {admin_email}")
print(f"Password verification: {'✅ PASS' if is_valid else '❌ FAIL'}")
print(f"Admin ID: {admin.id}")
print(f"is_admin flag: {admin.is_admin}")

db.close()