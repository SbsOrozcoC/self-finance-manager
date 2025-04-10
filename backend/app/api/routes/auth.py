from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, UserResponse
from app.services import user as user_service
from app.core.security import create_access_token
from app.db.database import get_db  # conexión a la base de datos

router = APIRouter(prefix="/auth", tags=["Autenticación"])

# ========================
# Registro de nuevo usuario
# ========================
@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Registra un nuevo usuario en la base de datos.
    """
    db_user = user_service.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
    
    db_email = user_service.get_user_by_email(db, user.email)
    if db_email:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    return user_service.create_user(db, user)

# ========================
# Login y obtención de token JWT
# ========================
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Autentica al usuario y genera un token de acceso (JWT).
    """
    user = user_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")

    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
