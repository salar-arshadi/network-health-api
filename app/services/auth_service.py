from sqlalchemy.orm import Session

from app.models.auth.user import User
from app.security import (
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def authenticate_user(
        db: Session,
        username: str,
        password: str,
    ):

        user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        token = create_access_token(
            {
                "sub": user.username,
                "role": user.role.name,
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "user": user,
        }
