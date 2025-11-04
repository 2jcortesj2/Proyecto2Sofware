# 🧬 BioLab LIS - Sistema de Información de Laboratorio

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Django](https://img.shields.io/badge/Django-5.2.7-green)
![Vue.js](https://img.shields.io/badge/Vue.js-3.x-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![License](https://img.shields.io/badge/license-MIT-purple)

**BioLab LIS** es un sistema de información de laboratorio clínico diseñado para la gestión integral de pacientes, laboratoristas y resultados de análisis de perfil lipídico. Desarrollado con Django (backend) y Vue.js (frontend).

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [API Endpoints](#-api-endpoints)
- [Scripts Disponibles](#-scripts-disponibles)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## ✨ Características

### 👥 Gestión de Pacientes
- ✅ Registro completo de pacientes con datos demográficos
- ✅ Código de ingreso único
- ✅ Información de EPS/Seguro médico
- ✅ Búsqueda y filtrado en tiempo real
- ✅ Edición y eliminación de registros

### 🔬 Gestión de Laboratoristas
- ✅ Registro de personal de laboratorio
- ✅ Información profesional (título, especialidad)
- ✅ Datos de contacto completos
- ✅ Sistema de búsqueda avanzado

### 📊 Gestión de Resultados
- ✅ Registro de perfil lipídico completo:
  - Colesterol Total
  - Colesterol HDL
  - Colesterol LDL
  - Triglicéridos
- ✅ Indicadores visuales de rangos normales/elevados
- ✅ Modal de detalles con información completa del paciente
- ✅ Observaciones médicas
- ✅ Vinculación automática paciente-laboratorista
- ✅ Historial de análisis

### 🎨 Interfaz de Usuario
- ✅ Diseño moderno y responsivo
- ✅ Navegación por pestañas
- ✅ Sistema de alertas animadas
- ✅ Badges de estado con colores
- ✅ Búsqueda en tiempo real
- ✅ Formularios validados

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **Django 5.2.7** - Framework web de Python
- **Django REST Framework** - Para APIs RESTful
- **MySQL** - Base de datos relacional
- **django-cors-headers** - Manejo de CORS

### Frontend
- **Vue.js 3** - Framework JavaScript progresivo
- **Vue Router** - Enrutamiento SPA
- **Axios** - Cliente HTTP
- **Vite** - Build tool y dev server

### Herramientas de Desarrollo
- **Python 3.x**
- **Node.js & npm**
- **XAMPP** - Servidor MySQL local

---

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.8+** - [Descargar Python](https://www.python.org/downloads/)
- **Node.js 16+** y npm - [Descargar Node.js](https://nodejs.org/)
- **MySQL** - A través de [XAMPP](https://www.apachefriends.org/) o instalación independiente
- **Git** (opcional) - Para clonar el repositorio

### Verificar instalaciones:

```bash
python --version
node --version
npm --version
mysql --version
```

---

## 🚀 Instalación

### 1️⃣ Clonar o Descargar el Proyecto

```bash
# Si usas Git
git clone <url-del-repositorio>
cd Proyecto2Sofware

# O simplemente descomprime el ZIP descargado
```

### 2️⃣ Crear Entorno Virtual de Python

```bash
# Crear entorno virtual en la raíz del proyecto
python -m venv env

# Activar entorno virtual
# En Windows:
env\Scripts\activate

# En Linux/Mac:
source env/bin/activate
```

### 3️⃣ Instalar Dependencias del Backend

```bash
cd backend
pip install django
pip install mysqlclient
pip install django-cors-headers
```

### 4️⃣ Instalar Dependencias del Frontend

```bash
cd ../frontend
npm install
```

---

## ⚙️ Configuración

### 1️⃣ Configurar Base de Datos MySQL

#### Iniciar XAMPP:
- Abre XAMPP Control Panel
- Inicia **Apache** y **MySQL**

#### Crear Base de Datos:
```sql
-- Abrir phpMyAdmin (http://localhost/phpmyadmin)
-- Ejecutar:
CREATE DATABASE clinical_data CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 2️⃣ Configurar Django

El archivo `backend/MedicalAPI/settings.py` ya está configurado con:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '',  # Cambiar si tu MySQL tiene contraseña
        'NAME': 'clinical_data',
    }
}
```

**⚠️ Importante:** Si tu MySQL tiene contraseña, actualiza el campo `PASSWORD`.

### 3️⃣ Ejecutar Migraciones

```bash
cd backend

# Crear migraciones
python manage.py makemigrations api_paciente
python manage.py makemigrations api_laboratorista
python manage.py makemigrations api_resultado

# Aplicar migraciones
python manage.py migrate
```

### 4️⃣ Crear Superusuario (Opcional)

```bash
python manage.py createsuperuser
# Seguir las instrucciones para crear usuario admin
```

### 5️⃣ Cargar Datos de Ejemplo (Opcional)

```bash
# En phpMyAdmin, importar el archivo:
datos_ejemplo.sql
```

---

## 🎯 Uso

### Opción 1: Inicio Manual (Dos Consolas)

#### Consola 1 - Backend:
```bash
cd backend
env\Scripts\activate  # Desde la raíz
python manage.py runserver
```
**Backend corriendo en:** http://127.0.0.1:8000

#### Consola 2 - Frontend:
```bash
cd frontend
npm run dev
```
**Frontend corriendo en:** http://localhost:5173

---

### Opción 2: Inicio Automático (Recomendado)

Usa el script `start_biolab.bat` en la raíz del proyecto:

```bash
# Simplemente doble clic en:
start_biolab.bat
```

Esto abrirá automáticamente dos ventanas con el backend y frontend.

**Para detener:**
```bash
# Doble clic en:
stop_biolab.bat
```

---

### 🌐 Acceder al Sistema

Una vez iniciados ambos servidores:

- **Aplicación Principal:** http://localhost:5173
- **Admin Django:** http://127.0.0.1:8000/admin
- **API Backend:** http://127.0.0.1:8000/api

---

## 📁 Estructura del Proyecto

```
Proyecto2Sofware/
│
├── backend/                    # Backend Django
│   ├── MedicalAPI/            # Configuración del proyecto
│   │   ├── settings.py        # Configuración general
│   │   ├── urls.py            # URLs principales
│   │   └── wsgi.py
│   │
│   ├── api_paciente/          # App de Pacientes
│   │   ├── models.py          # Modelo Paciente
│   │   ├── views.py           # API Views
│   │   ├── urls.py            # URLs de la API
│   │   └── admin.py
│   │
│   ├── api_laboratorista/     # App de Laboratoristas
│   │   ├── models.py          # Modelo Laboratorista
│   │   ├── views.py           # API Views
│   │   ├── urls.py            # URLs de la API
│   │   └── admin.py
│   │
│   ├── api_resultado/         # App de Resultados
│   │   ├── models.py          # Modelo ResultadoPerfilLipidico
│   │   ├── views.py           # API Views
│   │   ├── urls.py            # URLs de la API
│   │   └── admin.py
│   │
│   └── manage.py              # CLI de Django
│
├── frontend/                   # Frontend Vue.js
│   ├── src/
│   │   ├── assets/
│   │   │   └── main.css       # Estilos globales
│   │   ├── components/        # Componentes Vue
│   │   ├── router/
│   │   │   └── index.js       # Configuración de rutas
│   │   ├── services/
│   │   │   └── api.js         # Servicio API con Axios
│   │   ├── views/
│   │   │   ├── PacientesView.vue
│   │   │   ├── LaboratoristasView.vue
│   │   │   └── ResultadosView.vue
│   │   ├── App.vue            # Componente raíz
│   │   └── main.js            # Punto de entrada
│   │
│   ├── package.json           # Dependencias Node
│   └── vite.config.js         # Configuración Vite
│
├── env/                        # Entorno virtual Python
├── datos_ejemplo.sql          # Script de datos de prueba
├── start_biolab.bat           # Script de inicio (Windows)
├── stop_biolab.bat            # Script de detención (Windows)
└── README.md                  # Este archivo
```

---

## 🔌 API Endpoints

### Base URL: `http://127.0.0.1:8000/api`

### 👥 Pacientes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/pacientes/` | Listar todos los pacientes |
| GET | `/pacientes/<paciente_id>/` | Obtener un paciente específico |
| POST | `/pacientes/` | Crear nuevo paciente |
| PUT | `/pacientes/<paciente_id>/` | Actualizar paciente |
| DELETE | `/pacientes/<paciente_id>/` | Eliminar paciente |

#### Ejemplo POST - Crear Paciente:
```json
{
  "paciente_id": "P011",
  "codigo_ingreso": "ING-00166",
  "nombre": "Juan",
  "apellidos": "Pérez García",
  "direccion": "Calle 123 #45-67",
  "telefono": "3001234567",
  "insurance": "Sura EPS",
  "fecha_registro": "2024-11-03"
}
```

---

### 🔬 Laboratoristas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/laboratoristas/` | Listar todos los laboratoristas |
| GET | `/laboratoristas/<id>/` | Obtener un laboratorista específico |
| POST | `/laboratoristas/` | Crear nuevo laboratorista |
| PUT | `/laboratoristas/<id>/` | Actualizar laboratorista |
| DELETE | `/laboratoristas/<id>/` | Eliminar laboratorista |

#### Ejemplo POST - Crear Laboratorista:
```json
{
  "codigo_interno": "LAB006",
  "nombre": "Dr. Carlos Mendoza",
  "titulo": "Bacteriólogo",
  "telefono": "3001234567",
  "email": "carlos.mendoza@biolab.com",
  "especialidad": "Química Clínica"
}
```

---

### 📊 Resultados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/resultados/` | Listar todos los resultados |
| GET | `/resultados/<id>/` | Obtener un resultado específico |
| POST | `/resultados/` | Crear nuevo resultado |
| PUT | `/resultados/<id>/` | Actualizar resultado |
| DELETE | `/resultados/<id>/` | Eliminar resultado |

#### Ejemplo POST - Crear Resultado:
```json
{
  "paciente_id": "P001",
  "laboratorista_id": 1,
  "colesterol_total": 185.5,
  "colesterol_hdl": 52.0,
  "colesterol_ldl": 115.0,
  "trigliceridos": 130.0,
  "fecha_analisis": "2024-11-03",
  "observaciones": "Valores dentro del rango normal."
}
```

---

## 📜 Scripts Disponibles

### Backend (Django)

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Abrir shell de Django
python manage.py shell
```

### Frontend (Vue.js)

```bash
# Iniciar servidor de desarrollo
npm run dev

# Compilar para producción
npm run build

# Preview de producción
npm run preview
```

### Scripts de Inicio Automático

```bash
# Iniciar todo el sistema (Windows)
start_biolab.bat

# Detener todo el sistema (Windows)
stop_biolab.bat

# Diagnóstico de estructura
diagnostico.bat
```

---

## 📸 Capturas de Pantalla

### Dashboard Principal
![Dashboard](docs/images/dashboard.png)

### Gestión de Pacientes
![Pacientes](docs/images/pacientes.png)

### Resultados de Análisis
![Resultados](docs/images/resultados.png)

---

## 🐛 Solución de Problemas

### Error: "No module named 'corsheaders'"
```bash
# Solución:
pip install django-cors-headers
```

### Error: "Access denied for user 'root'@'localhost'"
```bash
# Solución:
# Verificar que MySQL está corriendo en XAMPP
# Actualizar PASSWORD en settings.py si tu MySQL tiene contraseña
```

### Error: "Port 8000 is already in use"
```bash
# Solución:
# Cambiar el puerto:
python manage.py runserver 8080
```

### Error: "ENOENT: no such file or directory"
```bash
# Solución:
cd frontend
npm install
```

### Frontend no se conecta al Backend
```bash
# Verificar:
# 1. Backend está corriendo en http://127.0.0.1:8000
# 2. CORS está configurado correctamente en settings.py
# 3. Axios apunta a la URL correcta en api.js
```

### Error de Migraciones
```bash
# Solución:
# Borrar archivos de migraciones (excepto __init__.py)
# Volver a crear:
python manage.py makemigrations
python manage.py migrate
```

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 👨‍💻 Autores

- **Juan José Cortés** - *Desarrollo inicial* - [Tu GitHub](https://github.com/2jcortesj2)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 📞 Soporte

Si tienes preguntas o necesitas ayuda:

- 📧 Email: jjose.cortes@udea.edu.com
---

## 🙏 Agradecimientos

- Django Documentation
- Vue.js Documentation
- Comunidad de Stack Overflow
- Profe Angelower

---

## 📈 Roadmap

### Versión 1.1 (Próxima)
- [ ] Exportación de resultados a PDF
- [ ] Envío de resultados por email
- [ ] Gráficos de tendencias de resultados
- [ ] Autenticación de usuarios

### Versión 1.2
- [ ] Múltiples tipos de análisis
- [ ] Sistema de citas
- [ ] Notificaciones push
- [ ] Dashboard con estadísticas

### Versión 2.0
- [ ] App móvil
- [ ] Integración con equipos de laboratorio
- [ ] IA para análisis predictivo
- [ ] Multi-tenancy

---

**Desarrollado con ❤️ usando Django y Vue.js**

---

## 🎓 Información Académica

Este proyecto fue desarrollado como parte del curso de Ingeniería de Software en la Universidad de Antioquía.

**Fecha:** Noviembre 2024  
**Versión:** 1.0.0