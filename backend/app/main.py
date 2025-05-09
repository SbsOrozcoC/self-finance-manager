from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import Base, engine
from app.api.routes import auth
from app.api.routes import private
from app.api.routes import admin

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
# Middleware de CORS
# ========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # ← Aquí se habilita tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========================
# Incluir rutas del sistema
# ========================
app.include_router(auth.router)
app.include_router(private.router)
app.include_router(admin.router)