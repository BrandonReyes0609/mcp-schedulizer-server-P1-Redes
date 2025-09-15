# 🤖 Proyecto 1 Redes (Schedulizer Server)

Este documento describe el funcionamiento del agente anfitrión desarrollado para el **Proyecto 1 - Uso de un protocolo existente (CC3067)**, el cual utiliza un **LLM (Claude)** para interpretar instrucciones en lenguaje natural y ejecutar herramientas a través de un **servidor MCP local** compatible con el protocolo oficial.

Realizado por:
Brandon Reyes Moraes 22992

---

## Herramientas disponibles

### **Servidor Local MCP (`mcp_schedulizer.py`)**

 **Temática:** **Gestión de tareas y generación de horarios (Schedulizer)**

 **Funciones principales:**

* Agregar tareas con duración, prioridad y deadline
* Listar tareas (`list_tasks`)
* Generar agenda optimizada (`generate_schedule`)
* Guardar tareas localmente en `tasks_db.json`

 **Objetivo:** Ser el núcleo del proyecto, simulando un asistente que organiza tu semana a partir de tus tareas. Se puede extender para priorizar materias, trabajo, descanso, etc.

---

### **Servidor Remoto MCP (Google Cloud Run)**

 **Temática:** **Servicios educativos complementarios y bienestar**

 **Funciones implementadas:**

* `suggest_breaks`: sugiere descansos entre tareas en una agenda
* `daily_quote`: devuelve una frase motivacional del día

 **Objetivo:** Extender el asistente con funciones que apoyan el bienestar del estudiante o trabajador, reforzando la productividad con motivación y pausas saludables. Sirve como ejemplo de servidor hospedado en la nube.

---

## 💬 Ejemplo de conversación

### Server online

* Ejemplos para el servidor remoto en Google Cloud (FastAPI)

```
¿Puedes sugerirme descansos si estudio 4 horas?
```

```
Dame una frase motivacional
```

```
Agrega tarea de estudiar redes...
```

```
Escribe en archivo notas.txt
```

* Suggest_breaks — Sugerencias tipo Pomodoro

```
Si planeo estudiar 3 horas, ¿cuántos descansos debería tomar?
```

```
Voy a trabajar durante 5 horas seguidas, ¿puedes sugerirme pausas?
```

```
¿Puedes darme una rutina tipo Pomodoro para estudiar 2.5 horas?
```

```
Dame una lista de descansos si planeo hacer 4 horas de estudio
```

```
Quiero organizar mi jornada de 6 horas con pausas cada 45 minutos
```

```
Sugiere bloques de trabajo y descanso para una sesión de 3 horas
```

* daily_quote — Frases motivacionales

```
Dame una frase motivacional para empezar mi día
```

```
¿Tienes alguna frase positiva que me inspire hoy?
```

```
Quiero una cita inspiradora por favor
```

```
Motívame con una frase para estudiar
```

```
¿Puedes darme una frase que me ayude a concentrarme?
```

```
¿Puedes darme una frase que me ayude a concentrarme?
```

* **¿Cómo verificar que se está usando el servidor remoto?**

Deberías ver en consola algo como:

```
🔗 Claude API usada para interpretar instrucciones del usuario...
🔧 Ejecutando 'suggest_breaks' con: {'hours': 4}
🌐 Usando servidor remoto en Google Cloud (endpoint /suggest_breaks)
📬 Respuesta: { ... }
```

ó

```
🔧 Ejecutando 'daily_quote' con: {}
🌐 Usando servidor remoto en Google Cloud (endpoint /daily_quote)
```

### server local

* Ejemplos de entrada para tareas (add_task)

```
Agrega una tarea de estudiar para final de redes, 90 minutos, deadline 2025-09-30
```

```
Agrega una tarea de estudiar para el examen de redes, 90 minutos, deadline 2025-09-30, prioridad alta, categoría universidad
```

```
Crea una nueva tarea llamada “Leer capítulo 5 de inteligencia artificial”, duración 60 minutos, deadline 2025-10-01, prioridad media, categoría estudio
```

```
Agrega tarea para repasar algoritmos, duración 45 minutos, deadline 2025-09-25, prioridad baja, categoría universidad
```

```
Añade tarea de redactar el reporte de laboratorio de redes, que dure 120 minutos, con fecha límite 2025-10-02, categoría universidad, prioridad alta
```

```
Registra una tarea para repasar seguridad informática por 30 minutos antes del 28 de septiembre, categoría trabajo, prioridad media
```

* Ejemplo para listar tareas (list_tasks)

```
Muéstrame todas mis tareas
```

```
¿Cuáles tareas tengo pendientes?
```

```
Quiero ver mi lista de tareas
```

**¿Cómo verificar que se está usando el servidor remoto?**

Deberías ver en consola algo como:

```
🔗 Claude API usada para interpretar instrucciones del usuario...
🔧 Ejecutando 'suggest_breaks' con: {'hours': 4}
🌐 Usando servidor remoto en Google Cloud (endpoint /suggest_breaks)
📬 Respuesta: { ... }
```

ó

```
🔧 Ejecutando 'daily_quote' con: {}
🌐 Usando servidor remoto en Google Cloud (endpoint /daily_quote)
```

### Ejemplos para el servidor Filesystem MCP (STDIO)

* write_file — Escribir o crear archivos

```
Crea un archivo llamado resumen.txt con el contenido: Capas del modelo OSI y sus funciones
```

```
Escribe en un archivo llamado tareas.txt lo siguiente: estudiar redes, programar simulador
```

```
Guarda en notas/lunes.txt: revisar tareas de Claude y servidor remoto
```

```
Crea una carpeta 'reportes' y dentro guarda un archivo llamado info.txt con el contenido: MCP funcionando correctamente
```

```
Escribe en workspace/semana1.txt lo siguiente: Lunes - estudiar, Martes - descanso, Miércoles - laboratorio
```

* read_file — Leer archivos existentes

```
Lee el archivo resumen.txt
```

```
Muéstrame el contenido de tareas.txt
```

```
Abre y lee el archivo llamado info.txt que está en la carpeta reportes
```

```
Quiero ver lo que escribí en semana1.txt
```

```
¿Puedes leer el archivo llamado notas/lunes.txt?
```

---

**🧪 ¿Cómo saber que se está usando el servidor Filesystem?**

Cuando usas uno de esos comandos, tu consola debe mostrar:

```
🔧 Ejecutando 'read_file' con: {'path': 'workspace/resumen.txt'}
📁 Usando servidor filesystem STDIO (Filesystem MCP)
📬 Respuesta:
{
  "output": {
    "content": "Capas del modelo OSI y sus funciones"
  }
}
```

---

## Ruta de las carpetas y archivos

```
mcp-schedulizer-server-P1-Redes/
├── docs/                            # Documentación general y técnica
│   ├── screenshots/                 # Capturas usadas en los informes
│   │   ├── README_LLM_ES.md        # Redacción sobre integración LLM
│   │   ├── README_LLM_ES copy.md   # Versión duplicada o de respaldo
│   │   ├── README_LLM_ES.md        # Redacción sobre LLM (versión principal)
│   │   └── README.md               # Instrucciones generales de screenshots
│   ├──
│   ├── captura wireshark 1.png     # Captura de comunicación chatbot-servidor
│   ├── captura_wireshark_mcp_local.png
│   ├── captura_wireshark_server_remoto.png
│   ├── INFORME.docx                # Informe formal del proyecto (editable)
│   ├── INFORME.pdf                 # Informe en formato PDF
│   └── prueba2.pcap                # Archivo de captura de red (Wireshark)
│
├── src/                            # Código fuente principal del servidor MCP
│   ├── tools/                      # Definiciones de herramientas (tools)
│   │   ├── add_task.tool.json          # Tool para agregar tarea
│   │   ├── definition.json             # Definición de todas las tools registradas
│   │   ├── generate_schedule.tool.json# Tool para generar horario optimizado
│   │   ├── get_calendar.tool.json     # Tool para obtener calendario actual
│   │   ├── list_tasks.tool.json       # Tool para listar tareas actuales
│   │   └── remove_task.tool.json      # Tool para eliminar tareas
│   └── mcp_schedulizer.py         # Servidor MCP local que organiza tareas
│   └── cliente_chatbot_fs_rr.py   # Cliente que interactúa con Claude y servidores (FS + Remoto)
│   └── mcp_log.txt                # Log de ejecución del servidor
│
├── workspace/                      # Espacio de trabajo local (simula almacenamiento del usuario)
│   ├── universidad/               # Subcarpeta ejemplo para organización
│   ├── agenda.txt                 # Archivo generado con el horario
│
├── venv_mcp/                       # Entorno virtual de Python
│   └── ... (archivos internos del entorno) ...
│
├── .env                            # Variables de entorno (config local)
├── .gitignore                      # Archivos a ignorar por Git
├── env.example                     # Plantilla de `.env`
├── mcp_log.txt                     # Log duplicado fuera de `src` (revisar si necesario)
├── README_LLM_EN.md                # Instrucciones en inglés sobre integración LLM
├── README_mcp_oficial_servers.md   # Instrucciones para correr servidores oficiales (FS, Git, etc.)
├── README.md                       # Instrucciones principales del proyecto
├── README(1).md                    # (duplicado o respaldo del README)
├── requirements.txt                # Lista de dependencias del proyecto

```

---

---

## ✅ Requisitos previos

- Python 3.12+
- Librerías: `anthropic`, `requests`, `flask`
- API Key válida de Anthropic
- Servidor MCP corriendo en `http://localhost:5000`

```
pip install flask
pip install requests
pip install rich
pip install anthropic

pip install anthropic python-dotenv requests mcp
pip install flask anthropic python-dotenv requests mcp
```

## ✅Ejecución

Ejecución del chat del cliente:

```
python src\cliente_chatbot_fs_rr.py
```

Ejecución del server local:

```
python src\mcp_schedulizer.py
```

## 📌 Notas
