from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# ========================
# Cargar variables de entorno desde .env
# ========================
load_dotenv()

# ========================
# Obtener datos de conexión desde .env
# ========================
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = "db"  # nombre del servicio en docker-compose
DB_PORT = "5432"

# ========================
# Crear URL de conexión
# ========================
SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ========================
# Configuración del engine de SQLAlchemy
# ========================
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ========================
# Crear sesión de base de datos
# ========================
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ========================
# Clase base para modelos ORM
# ========================
Base = declarative_base()

# ========================
# Dependencia para obtener la sesión en cada request
# ========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
