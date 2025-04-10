from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routes import auth
from app.api.routes import private

# ========================
# Crear todas las tablas en la base de datos
# ========================
# Esto es solo para desarrollo. En producción usa migraciones con Alembic.
Base.metadata.create_all(bind=engine)

# ========================
# Instancia de la aplicación FastAPI
# ========================
app = FastAPI(
    title="Self Finance Manager API",
    description="API de gestión financiera personal",
    version="1.0.0"
)

# ========================
# Incluir rutas del sistema
# ========================
app.include_router(auth.router)
app.include_router(private.router)