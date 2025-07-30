# 🏥 Sistema Hospitalario

Sistema de gestión hospitalaria desarrollado con **Flask** siguiendo los principios de **Arquitectura Hexagonal (Clean Architecture)**. Este sistema permite gestionar citas médicas, atención de pacientes, egresos hospitalarios y la integración con sistemas externos.

## 📋 Tabla de Contenidos

- [Características](#características)
- [Arquitectura](#arquitectura)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Uso](#uso)
- [API Endpoints](#api-endpoints)
- [Desarrollo](#desarrollo)
- [Contribución](#contribución)

## ✨ Características

### 🗓️ Gestión de Citas
- Agendamiento de citas médicas
- Gestión de disponibilidad de profesionales
- Manejo de especialidades médicas
- Registro y gestión de pacientes

### 🩺 Atención Médica
- Registro de signos vitales
- Gestión de síntomas y diagnósticos
- Emisión de recetas médicas
- Historia clínica electrónica (HCE)

### 🏥 Egresos Hospitalarios
- Gestión de altas médicas
- Control de condición del paciente
- Sistema de derivaciones
- Integración con sistemas externos

## 🏗️ Arquitectura

El proyecto implementa **Arquitectura Hexagonal** con las siguientes capas:

```
┌─────────────────────────────────────────┐
│            Presentation Layer           │  ← Controllers, REST APIs
├─────────────────────────────────────────┤
│            Application Layer            │  ← Services, Ports
├─────────────────────────────────────────┤
│              Domain Layer               │  ← Entities, Business Logic
├─────────────────────────────────────────┤
│           Infrastructure Layer          │  ← Adapters, Database, External APIs
└─────────────────────────────────────────┘
```

### Principios Aplicados:
- **Inversión de Dependencias**: El dominio no depende de la infraestructura
- **Separación de Responsabilidades**: Cada capa tiene una responsabilidad específica
- **Testabilidad**: Arquitectura que facilita las pruebas unitarias
- **Mantenibilidad**: Código organizado y fácil de mantener

## 📁 Estructura del Proyecto

```
hospital_system/
├── backend/
│   ├── app.py                          # Punto de entrada de la aplicación
│   └── app/
│       ├── aplication/                 # 📋 Capa de Aplicación
│       │   ├── ports/                  # Interfaces/Contratos
│       │   │   ├── cita_schedule_port.py
│       │   │   ├── derivaciones_port.py
│       │   │   ├── disponibilidad_port.py
│       │   │   ├── egresos_port.py
│       │   │   ├── hce_port.py
│       │   │   └── prescripciones_port.py
│       │   └── services/               # Servicios de Aplicación
│       │       ├── agenda_cita_service.py
│       │       ├── brindar_atencion_service.py
│       │       └── egreso_paciente_service.py
│       ├── domain/                     # 🎯 Capa de Dominio
│       │   ├── atencion/               # Dominio: Atención Médica
│       │   │   ├── diagnostico.py
│       │   │   ├── receta.py
│       │   │   ├── signo_vital.py
│       │   │   └── sintoma.py
│       │   ├── cita/                   # Dominio: Gestión de Citas
│       │   │   ├── cita.py
│       │   │   ├── disponibilidad.py
│       │   │   ├── especialidad.py
│       │   │   └── paciente.py
│       │   └── egreso/                 # Dominio: Egresos Hospitalarios
│       │       ├── alta_medica.py
│       │       ├── condicion_paciente.py
│       │       └── derivacion.py
│       ├── infraestructure/            # 🔧 Capa de Infraestructura
│       │   ├── adapters/
│       │   │   ├── external/           # Adaptadores Externos
│       │   │   │   ├── derivaciones_adapter.py
│       │   │   │   ├── egresos_adapter.py
│       │   │   │   ├── hce_adapter.py
│       │   │   │   ├── his_adapter.py
│       │   │   │   ├── prescripciones_adapter.py
│       │   │   │   └── sgc_adapter.py
│       │   │   └── input/
│       │   │       └── rest/           # Adaptadores REST
│       │   │           ├── paciente_rest_adapter.py
│       │   │           └── profesional_rest_adapter.py
│       │   └── database/               # Base de Datos
│       │       ├── db.py
│       │       └── migrations/
│       ├── presentation/               # 🎨 Capa de Presentación
│       │   └── controllers/
│       │       ├── paciente_controller.py
│       │       └── profesional_controller.py
│       └── test/                       # 🧪 Pruebas
└── frontend/
    └── template.html                   # Frontend básico
```

## ✅ Pruebas de calidad de código (SonarLint)
![agenda_cita_sonar](docs/screenshots/agenda_cita_sonar.jpeg)

## 🛠️ Tecnologías

### Backend
- **Flask** - Framework web de Python
- **Python 3.8+** - Lenguaje de programación
- **SQLAlchemy** - ORM para base de datos
- **Flask-RESTful** - Extensión para APIs REST

### Base de Datos
- **MySQL 8.0** - Base de datos principal (desplegada con Docker)
- **Docker & Docker Compose** - Contenerización de servicios
- **Adminer** - Interfaz web para gestión de base de datos
- **SQLite** - Base de datos para testing

### Herramientas de Desarrollo
- **pytest** - Framework de testing
- **black** - Formateador de código
- **flake8** - Linter de código

## 🚀 Instalación

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Docker y Docker Compose
- Git

### Configuración de Variables de Entorno

El proyecto requiere un archivo `.env` con la siguiente estructura:

```bash
# MySQL Database
MYSQL_ROOT_PASSWORD=tu_password_root
MYSQL_DATABASE=nombre_base_datos
MYSQL_USER=usuario_db
MYSQL_PASSWORD=password_usuario
MYSQL_HOST=localhost
MYSQL_PORT=3306

# Database URI para Flask-SQLAlchemy
DATABASE_URL=mysql+pymysql://usuario_db:password_usuario@localhost:3306/nombre_base_datos

# Adminer (DB Management)
ADMINER_PORT=8080

# Flask App Configuration
SECRET_KEY=tu_clave_secreta_super_segura
JWT_SECRET_KEY=tu_clave_jwt_para_autenticacion
```

> **Nota**: Cambia todos los valores por credenciales seguras para tu entorno. Copia el archivo `.env.example` a `.env` y personaliza las variables según tus necesidades.

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd hospital_system
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

3. **Configurar variables de entorno**
   ```bash
   # Copiar el archivo de ejemplo
   cp .env.example .env
   
   # Editar .env con tus credenciales específicas
   # En Windows puedes usar: copy .env.example .env
   ```

4. **Levantar los servicios con Docker**
   ```bash
   # Iniciar MySQL y Adminer
   docker-compose up -d
   
   # Verificar que los contenedores estén ejecutándose
   docker-compose ps
   ```

5. **Configurar base de datos (cuando tengas Flask configurado)**
   ```bash
   # Ejecutar migraciones
   flask db upgrade
   ```

6. **Ejecutar la aplicación**
   ```bash
   cd backend
   python app.py
   ```

## 🎯 Uso

### Levantar todo el entorno con Docker
```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs de los servicios
docker-compose logs -f
```

### Iniciar solo la aplicación (BD ya en Docker)
```bash
python backend/app.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Gestión de Docker
```bash
# Detener servicios
docker-compose down

# Reiniciar servicios
docker-compose restart

# Ver estado de los contenedores
docker-compose ps

# Ver logs de los servicios
docker-compose logs -f mysql
docker-compose logs -f adminer

# Acceder a la base de datos directamente
docker-compose exec mysql mysql -u tu_usuario_db -p nombre_base_datos
```

### Acceso a servicios
- **API Flask**: `http://localhost:5000`
- **Adminer (Gestión BD)**: `http://localhost:8080`
- **MySQL**: `localhost:3306`

### Credenciales para Adminer
- **Sistema**: MySQL
- **Servidor**: mysql
- **Usuario**: tu_usuario_db
- **Contraseña**: tu_password_usuario
- **Base de datos**: nombre_base_datos

### Acceder a la documentación de la API
- Swagger UI: `http://localhost:5000/docs` (por configurar)
- Redoc: `http://localhost:5000/redoc` (por configurar)

## 🐳 Servicios Docker

El proyecto utiliza Docker Compose para gestionar los siguientes servicios:

### MySQL 8.0
- **Puerto**: 3306
- **Base de datos**: Configurada según tu `.env`
- **Usuario**: Configurado según tu `.env`
- **Contraseña**: Configurada según tu `.env`
- **Volumen persistente**: Los datos se mantienen entre reinicios

### Adminer
- **Puerto**: 8080
- **URL**: `http://localhost:8080`
- **Función**: Interfaz web para gestionar MySQL
- **Acceso**: Usar las credenciales de MySQL configuradas en `.env`

## 📚 API Endpoints

### 👤 Gestión de Pacientes
```
GET    /api/pacientes          # Listar pacientes
POST   /api/pacientes          # Crear paciente
GET    /api/pacientes/{id}     # Obtener paciente
PUT    /api/pacientes/{id}     # Actualizar paciente
DELETE /api/pacientes/{id}     # Eliminar paciente
```

### 👨‍⚕️ Gestión de Profesionales
```
GET    /api/profesionales      # Listar profesionales
POST   /api/profesionales      # Crear profesional
GET    /api/profesionales/{id} # Obtener profesional
PUT    /api/profesionales/{id} # Actualizar profesional
```

### 🗓️ Gestión de Citas
```
GET    /api/citas              # Listar citas
POST   /api/citas              # Agendar cita
GET    /api/citas/{id}         # Obtener cita
PUT    /api/citas/{id}         # Actualizar cita
DELETE /api/citas/{id}         # Cancelar cita
```

### 🩺 Atención Médica
```
POST   /api/atencion           # Registrar atención
GET    /api/atencion/{id}      # Obtener atención
POST   /api/signos-vitales     # Registrar signos vitales
POST   /api/recetas            # Emitir receta
```

### 🏥 Egresos
```
POST   /api/egresos            # Registrar egreso
GET    /api/egresos/{id}       # Obtener egreso
POST   /api/derivaciones       # Crear derivación
```

## 👨‍💻 Desarrollo

### Ejecutar pruebas
```bash
# Ejecutar todas las pruebas
pytest

# Ejecutar con cobertura
pytest --cov=app

# Ejecutar pruebas específicas
pytest tests/domain/test_cita.py
```

### Formatear código
```bash
# Formatear con black
black app/

# Verificar con flake8
flake8 app/
```

### Estructura de desarrollo
- Seguir principios SOLID
- Implementar tests para cada componente
- Documentar APIs con docstrings
- Usar type hints en Python

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama feature
3. Commit los cambios
4. Push a la rama
5. Abrir un Pull Request

### Convenciones de código
- Seguir PEP 8
- Usar nombres descriptivos en español para el dominio
- Documentar funciones y clases
- Escribir tests para nuevas funcionalidades

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- **Equipo de Desarrollo** - UNSA - Semestre 7 - Ingeniería de Software

## 🆘 Soporte

Si tienes alguna pregunta o problema:
1. Revisa la documentación
2. Busca en los issues existentes
3. Crea un nuevo issue con detalles del problema

---

⭐ ¡No olvides dar una estrella al proyecto si te ha sido útil!
