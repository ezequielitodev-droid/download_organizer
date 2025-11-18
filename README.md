# Files Organizer

Un organizador de archivos que clasifica y mueve archivos automáticamente según su tipo, creando backups antes de modificar cualquier archivo. Ideal para mantener tus carpetas de descargas ordenadas.

## 📂 Estructura del proyecto

```bash
FILES_ORGANIZER/
│
├─ data/
│ ├─ logs/ # Archivos de registro de cada acción
│ └─ temps/ # Archivos temporales durante el proceso
│
├─ FILES_ORGANIZER/
│ ├─ init.py
│ ├─ core.py
│ ├─ logging_config.py
│ ├─ organizer.py
│ └─ utils.py
│
├─ tests/ # Pruebas unitarias
├─ .env # Variables de entorno
├─ main.py # Archivo principal
├─ requirements.txt # Librerías necesarias
└─ README.md
```

## ⚙️ Requisitos

Tener en el computador Python 3.12.10, para arriba.

Se aconseja encarecidamente crear un entorno virtual:

- Sobre la carpeta del proyecto, hacer:
```bash
python -m venv venv
```
- Luego activarlo:
```bash
.\venv\Scripts\Activate.ps1   # Windows PowerShell
# o
source venv/bin/activate       # Linux/Mac
```



- Instalar dependencias:
```bash
pip install -r requirements.txt
```
## 📝 Configuración

Crear un archivo .env con las variables necesarias:

```bash
Crear variables de entorno con las direcciones importantes de tu computador, con los path que puedas querer usar

Ejemplo:
FOLDER_TO_ORGANIZE=C:/Users/Ezequielito/Downloads
BACKUP_PATH=D:/Backup


Abajo de adjunta las variables de entorno para controlar con los loggins:

Se deben completar con las tus rutas correspondientes de donde estan los respectivos archivos .log

SAFE_MOVE_FILE_LOG = 
SAFE_COPY_FILE_LOG = 
BACKUP_FOLDER_LOG = 
SCAN_FILE_LOG = 
CLASSIFY_FILE_LOG = 
DECIDE_DESTINATION_LOG = 
RUN_ORGANIZER_LOG = 


por ejemplo:

RUN_ORGANIZER_LOG = C:/Users/Ezequielito/files_organizer/data/logs/run_organizer.log

```

## ▶️ Uso

Ejecutar el organizador:

```bash
python main.py
```

O crear un ejecutable con PyInstaller:

```bash
pyinstaller --onefile --add-data ".env;." main.py
```

## 📋 Funcionalidades

- Clasifica archivos por extensión en diferentes carpetas.

- Crea backup de la carpeta antes de mover archivos.

- Genera logs de cada acción realizada.

- Evita sobrescribir archivos existentes.

## 💻 Estructura del código

- core.py → Función principal que inicia el organizador.

- organizer.py → Funciones para mover y clasificar archivos.

- utils.py → Funciones auxiliares (manejo de paths, validaciones, etc.).

- logging_config.py → Configuración de logs.

## 📝 Notas

- No se incluyen archivos de pruebas ni venv en el ejecutable.

- Las variables de entorno se usan para modularidad y privacidad.