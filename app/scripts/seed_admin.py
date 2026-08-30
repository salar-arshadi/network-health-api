from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.auth.user import User
from app.models.auth.role import Role
from app.security import hash_password


ADMIN_USERNAME = "admin"

ADMIN_PASSWORD = "admin123"

ADMIN_EMAIL = "admin@zitel.local"

ADMIN_FULL_NAME = "System Administrator"


def seed_admin():

    db: Session = SessionLocal()

    try:

        user = (
            db.query(User)
            .filter(User.username == ADMIN_USERNAME)
            .first()
        )

        if user:

            print("✅ Admin user already exists.")
            return

        admin_role = (
            db.query(Role)
            .filter(Role.name == "admin")
            .first()
        )

        if not admin_role:

            print("❌ Admin role not found.")
            return

        admin = User(

            username=ADMIN_USERNAME,

            email=ADMIN_EMAIL,

            full_name=ADMIN_FULL_NAME,

            password_hash=hash_password(
                ADMIN_PASSWORD
            ),

            role_id=admin_role.id,

            is_active=True,

        )

        db.add(admin)

        db.commit()

        print("✅ Admin user created successfully.")

        print()

        print("Username :", ADMIN_USERNAME)

        print("Password :", ADMIN_PASSWORD)

    finally:

        db.close()


if __name__ == "__main__":

    seed_admin()
