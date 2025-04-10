from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    # Nombre de usuario único
    username = Column(String, unique=True, index=True, nullable=False)

    # Email único para recuperación o notificaciones
    email = Column(String, unique=True, index=True, nullable=False)

    # Contraseña cifrada, no en texto plano
    hashed_password = Column(String, nullable=False)

    # Estado del usuario (activo o desactivado)
    is_active = Column(Boolean, default=True)

    # Rol del usuario (admin, user, etc.) - se puede extender
    role = Column(String, default="user")
