# Parra's Dev ToDo App

## Descripción

Aplicación web Django que resuelve el problema de la pizarra de pendientes para Parra's Dev. Esta aplicación permite gestionar una lista completa de tareas (ToDo) con diferentes vistas y funcionalidades CRUD.

## Características

### Listas Específicas Requeridas
- ✅ Lista de todos los pendientes (solo IDs)
- ✅ Lista de todos los pendientes (IDs y Titles)
- ✅ Lista de todos los pendientes sin resolver (ID y Title)
- ✅ Lista de todos los pendientes resueltos (ID y Title)
- ✅ Lista de todos los pendientes (IDs y userID)
- ✅ Lista de todos los pendientes resueltos (ID y userID)
- ✅ Lista de todos los pendientes sin resolver (ID y userID)

### Funcionalidades CRUD
- ✅ Crear nuevas tareas
- ✅ Leer/Ver tareas existentes
- ✅ Actualizar tareas
- ✅ Eliminar tareas
- ✅ Marcar tareas como completadas/pendientes

### Características Adicionales
- ✅ Sistema de autenticación de usuarios
- ✅ Interfaz web moderna y responsiva
- ✅ Panel de administración Django
- ✅ Validación de formularios
- ✅ Mensajes de feedback al usuario

## Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- pip

### Pasos de Instalación

1. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Realizar migraciones:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Crear superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

4. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

5. **Acceder a la aplicación:**
   - Aplicación principal: http://127.0.0.1:8000/
   - Panel de administración: http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
examen2/
├── todo/                    # Aplicación principal
│   ├── templates/todo/      # Plantillas HTML
│   ├── migrations/          # Migraciones de base de datos
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas
│   ├── forms.py            # Formularios
│   ├── urls.py             # URLs de la aplicación
│   ├── admin.py            # Configuración del admin
│   └── tests.py            # Pruebas unitarias
├── static/css/             # Archivos CSS
├── settings.py             # Configuración de Django
├── urls.py                 # URLs principales
├── manage.py               # Utilidad de administración
└── requirements.txt        # Dependencias del proyecto
```

## Uso de la Aplicación

### Para Usuarios
1. **Registro/Login**: Crear cuenta o iniciar sesión
2. **Gestionar Tareas**: Crear, editar, eliminar tareas personales
3. **Ver Listas**: Acceder a diferentes vistas de los pendientes
4. **Marcar Completadas**: Cambiar el estado de las tareas

### Para Administradores
1. **Panel Admin**: Acceso completo a todos los datos
2. **Gestión de Usuarios**: Crear y administrar cuentas
3. **Supervisión**: Ver todas las tareas del sistema

## URLs Disponibles

### Autenticación
- `/` - Página principal
- `/login/` - Iniciar sesión
- `/register/` - Registrar nueva cuenta
- `/logout/` - Cerrar sesión

### Listas Específicas
- `/todos/ids-only/` - Solo IDs
- `/todos/ids-titles/` - IDs y Títulos
- `/todos/pending/id-title/` - Pendientes (ID y Título)
- `/todos/completed/id-title/` - Completados (ID y Título)
- `/todos/ids-userids/` - IDs y UserIDs
- `/todos/completed/id-userid/` - Completados (ID y UserID)
- `/todos/pending/id-userid/` - Pendientes (ID y UserID)

### CRUD Operations
- `/todos/` - Lista de tareas del usuario
- `/todos/create/` - Crear nueva tarea
- `/todos/<id>/` - Ver detalle de tarea
- `/todos/<id>/update/` - Editar tarea
- `/todos/<id>/delete/` - Eliminar tarea
- `/todos/<id>/toggle/` - Cambiar estado completado/pendiente

## Tecnologías Utilizadas
- **Backend**: Django 4.2.11
- **Frontend**: HTML5, CSS3, Bootstrap 5.1.3
- **Base de Datos**: SQLite (por defecto)
- **JavaScript**: Vanilla JS para interactividad
- **Iconos**: Font Awesome 6.0.0

## Desarrollo

### Ejecutar Tests
```bash
python manage.py test
```

### Crear Migraciones
```bash
python manage.py makemigrations todo
```

### Aplicar Migraciones
```bash
python manage.py migrate
```

## Calidad del Código

El código fuente ha sido desarrollado siguiendo las mejores prácticas de Django:
- Estructura MVC (Model-View-Controller)
- Separación de responsabilidades
- Validación de datos
- Seguridad CSRF
- Código limpio y bien documentado

## Soporte

Para cualquier duda o problema, contactar con el equipo de desarrollo de Parra's Dev.

---

**© 2025 Parra's Dev. Todos los derechos reservados.**
