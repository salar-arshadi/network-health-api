from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.auth.role import Role


DEFAULT_ROLES = [

    {
        "name": "admin",
        "description": "Full system administrator",
    },

    {
        "name": "operator",
        "description": "Data Center Operator",
    },

    {
        "name": "viewer",
        "description": "Read only access",
    },

]


def seed_roles():

    db: Session = SessionLocal()

    try:

        for role_data in DEFAULT_ROLES:

            role = (
                db.query(Role)
                .filter(Role.name == role_data["name"])
                .first()
            )

            if role:
                continue

            db.add(
                Role(
                    name=role_data["name"],
                    description=role_data["description"],
                )
            )

        db.commit()

        print("✅ Roles created successfully.")

    finally:

        db.close()


if __name__ == "__main__":

    seed_roles()
