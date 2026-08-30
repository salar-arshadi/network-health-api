from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth.login import LoginRequest
from app.schemas.auth.token import TokenResponse
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    result = AuthService.authenticate_user(
        db=db,
        username=request.username,
        password=request.password,
    )

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    return {
        "access_token": result["access_token"],
        "token_type": result["token_type"],
    }
