from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.services.auth_utils import get_current_user

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)


@router.get("/users", response_model=list[UserResponse])
def get_all_users(
    skip: int = 0,
    limit: int = 10,
    search: str = "",
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Lista de usuarios para administradores, con paginación y filtro por nombre o email.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Solo administradores pueden acceder a esta ruta")

    query = db.query(User)

    if search:
        query = query.filter(
            (User.username.ilike(f"%{search}%")) |
            (User.email.ilike(f"%{search}%"))
        )

    users = query.offset(skip).limit(limit).all()
    return users


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Permite a un administrador actualizar datos de un usuario específico.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Acceso restringido solo a administradores")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user_data.email:
        user.email = user_data.email
    if user_data.is_active is not None:
        user.is_active = user_data.is_active
    if user_data.role:
        user.role = user_data.role

    db.commit()
    db.refresh(user)

    return user


@router.delete("/users/{user_id}", status_code=204)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Permite a un administrador eliminar un usuario del sistema.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Acceso restringido solo a administradores")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return


@router.patch("/users/{user_id}/status", response_model=UserResponse)
def toggle_user_status(
    user_id: int,
    is_active: bool,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Cambia el estado de activación (activo/inactivo) de un usuario.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Solo administradores pueden realizar esta acción")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    user.is_active = is_active
    db.commit()
    db.refresh(user)

    return user


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Retorna los datos de un usuario específico. Solo para administradores.
    """
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Acceso restringido solo a administradores")

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user
