from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Clave secreta para firmar los tokens (puedes moverla a variables de entorno)
SECRET_KEY = "una_clave_secreta_segura_123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ========================
# Configuración para hashear contraseñas
# ========================
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que la contraseña proporcionada coincida con el hash almacenado.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Genera el hash de una contraseña en texto plano.
    """
    return pwd_context.hash(password)

# ========================
# Generación del token JWT
# ========================
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Crea un token JWT con una expiración definida.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})  # Establece la expiración
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
