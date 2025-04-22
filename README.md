# 📊 Self Finance Manager

**Sistema de autogestión financiera personal** para llevar el control de ingresos, egresos, reportes y estadísticas.  
Desarrollado con **FastAPI (Backend)** y **Vue (Frontend)**.

---

## 🛠️ Tecnologías principales

- 🐍 Python 3.11
- ⚡ FastAPI
- 🎨 Vue.js 3 + TypeScript
    - Vue Router
    - Axios con JWT
    - Estilos externos con CSS modularizado
- 🐘 PostgreSQL
- 🐳 Docker + Docker Compose
- 🔒 OAuth2.0 con JWT (autenticación)

---

## 🚀 Estructura general

self-finance-manager/ 
├── backend/ 
│ ├── app/ 
│ │ ├── api/ # Rutas del API 
│ │ ├── core/ # Configuraciones generales (conexiones, seguridad, etc.) 
│ │ ├── models/ # Modelos de la base de datos 
│ │ ├── schemas/ # Esquemas Pydantic para validaciones 
│ │ └── services/ # Lógica de negocio 
│ ├── main.py # Punto de entrada de la aplicación 
│ ├── Dockerfile 
│ └── requirements.txt 
├── frontend/ # Proyecto en Vue3
├── docker-compose.yml 
├── .env 
├── .gitignore 
└── README.md

---

## 🧩 Módulos principales del sistema

- **Usuarios, roles y autenticación**
- **Ingresos y egresos mensuales**
- **Egresos fijos y control de presupuestos**
- **Reportes exportables (Excel + PDF)**
- **Dashboard con gráficas**
- **Envío automático de reportes por email**

---

## ✅ Requisitos para ejecutar localmente

### 🧰 Pre-requisitos:

- [x] Docker Desktop (v4+)
- [x] WSL2 (en Windows)
- [x] Git

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/SbsOrozcoC/self-finance-manager.git
cd self-finance-manager
```

2. Crear el archivo .env en la raíz del proyecto con el siguiente contenido:

```bash
POSTGRES_USER=finance_user
POSTGRES_PASSWORD=securepassword123
POSTGRES_DB=finance_db
```

3. Ejecutar el proyecto:

```bash
docker compose up --build
```

Una vez terminado, accede al backend en:
👉 http://localhost:8000

La documentación Swagger estará disponible en:
👉 http://localhost:8000/docs

4. Ingresar al contenedor con la base de datos

```bash
docker exec -it self-finance-manager-db-1 psql -U finance_user -d finance_db
```

## 🔐 Funcionalidades principales (por fases)

- ✅ Gestión de usuarios con roles y permisos

- ✅ Autenticación con OAuth2.0 + JWT

- 🧾 Registro de ingresos, egresos y egresos fijos

- 📈 Dashboard con gráficas mensuales

- 📤 Exportación de reportes (Excel, PDF)

- 📧 Envío automático de reportes al correo


## 🧱 Fases del desarrollo

- Fase 1: Sistema de autenticación y gestión de usuarios

- Fase 2: Ingreso y egresos mensuales

- Fase 3: Dashboard con estadísticas

- Fase 4: Reportes exportables y envío por correo

- Fase 5: Integración del frontend en Vue


✅ Cambios recientes (última sesión)
🎨 Se desarrolló e integró el módulo de Login desde Vue, con validación contra FastAPI

🧑‍💻 Se aplicaron estilos y centrado responsivo al formulario

🔒 Se configuró CORS en FastAPI para aceptar peticiones desde el frontend

📦 Se activó localStorage para almacenar el token JWT tras el login

🔐 Se protegió la ruta /dashboard para que solo usuarios autenticados accedan

⚙️ Se implementó estructura de frontend desacoplada del backend vía Docker o npm run serve


## 👨‍💻 Autor
Proyecto creado por @SbsOrozcoC Sebastian Orozco Cano como herramienta de control financiero personal.