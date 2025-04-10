from pydantic import BaseModel, EmailStr
from typing import Optional

# ========================
# Esquema base común
# ========================
class UserBase(BaseModel):
    username: str
    email: EmailStr

# ========================
# Esquema para crear usuarios (registro)
# ========================
class UserCreate(UserBase):
    password: str  # El usuario debe enviar una contraseña

# ========================
# Esquema de respuesta (lo que enviamos de vuelta)
# ========================
class UserResponse(UserBase):
    id: int
    is_active: bool
    role: str

    class Config:
        orm_mode = True  # Permite que FastAPI trabaje con modelos ORM directamente

# ========================
# Esquema para login
# ========================
class UserLogin(BaseModel):
    username: str
    password: str
