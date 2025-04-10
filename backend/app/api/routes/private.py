from fastapi import APIRouter, Depends
from app.services.auth_utils import get_current_user
from app.schemas.user import UserResponse
from app.services.auth_utils import require_admin

router = APIRouter(prefix="/private", tags=["Privado"])

@router.get("/me", response_model=UserResponse)
def read_logged_user(current_user: UserResponse = Depends(get_current_user)):
    """
    Retorna los datos del usuario actual autenticado.
    """
    return current_user

@router.get("/admin-only")
def admin_route(current_admin: UserResponse = Depends(require_admin)):
    """
    Ruta privada exclusiva para administradores.
    """
    return {"message": f"Hola {current_admin.username}, tienes acceso como administrador."}