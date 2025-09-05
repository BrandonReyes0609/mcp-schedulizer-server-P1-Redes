# 📘 MCP-Schedulizer

## 🎯 Propósito del proyecto
El proyecto **MCP-Schedulizer** consiste en el desarrollo de un **servidor MCP local** que ayuda a organizar tareas personales, académicas o laborales.  
Su función principal es **generar un horario optimizado** a partir de las tareas registradas por el usuario, tomando en cuenta:

- ⏳ Duración  
- 📅 Fecha límite (deadline)  
- 🔝 Prioridad (alta, media, baja)  
- 🏷️ Categoría  

Este servidor puede ser invocado por un **chatbot anfitrión** que actúa como cliente, ofreciendo al usuario una interfaz sencilla en consola.

---

## 📚 Temática del proyecto
El proyecto pertenece al curso **CC3067 – Redes de Computadoras (UVG)** y está enmarcado dentro del **Proyecto 1: Uso de un protocolo existente**.  
La idea central es aprender a **implementar un servidor MCP local** y un cliente que interactúe con él, aplicando conceptos de protocolos de red en la **capa de aplicación** del modelo OSI.

---

## 🌐 Protocolo utilizado
El sistema se basa en **JSON-RPC 2.0**, un protocolo estándar para **llamadas a procedimiento remoto** (RPC) utilizando JSON.

- **Cliente (chatbot)** → envía solicitudes JSON-RPC vía **HTTP POST**.  
- **Servidor (MCP-Schedulizer)** → recibe la solicitud, ejecuta el método (ej. `add_task`, `list_tasks`, `generate_schedule`) y responde con un objeto JSON siguiendo la especificación del protocolo.  

Esto significa que el proyecto **sí implementa un protocolo real**, combinando:
- **HTTP** como transporte.  
- **JSON-RPC** como protocolo de aplicación.  
- Alineado con **MCP (Model Context Protocol)** de Anthropic.  

---

## ⚙️ Funcionalidades implementadas
- **Agregar tarea** con atributos (nombre, duración, deadline, prioridad, categoría).  
- **Listar tareas** mostrando ID, nombre, duración, fecha límite y prioridad.  
- **Generar agenda** respetando orden por `deadline` y `prioridad`.  
- **Eliminar tarea** mediante su **ID**.  
- **Exportar agenda** a un archivo `agenda_exportada.csv`.  

---

## 🛠️ Instalación y ejecución

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPO>
cd mcp-schedulizer
```

### 2. Instalar dependencias
```bash
pip install flask requests rich
```

### 3. Ejecutar el servidor
```bash
python mcp_schedulizer.py
```
Esto levanta el servidor en `http://localhost:8000/`.

### 4. Ejecutar el cliente
En otra terminal:
```bash
python cliente_chatbot.py
```

---

## 💻 Ejemplo de uso
```text
Chatbot Anfitrión - MCP Schedulizer
Comandos disponibles:
1. Agregar tarea
2. Listar tareas
3. Generar horario
4. Eliminar tarea por ID
5. Exportar agenda
6. Salir

Selecciona una opción (1-6): 1
Nombre de la tarea: Estudiar Redes
Duración (minutos): 120
Fecha límite (YYYY-MM-DDTHH:MM): 2025-09-10T23:59
Prioridad (alta/media/baja): alta
Categoría: universidad
```

---

## 🧩 Arquitectura y capas OSI
- **Capa de aplicación:** JSON-RPC 2.0 + MCP (formato y reglas de los mensajes).  
- **Capa de transporte:** HTTP (POST).  
- **Capa de red:** IP (localhost en este caso).  
- **Capa de enlace y física:** dependientes del sistema operativo (loopback interface).  

---

## 📤 Exportación de agenda
Con la opción **5** del cliente, se genera un archivo `agenda_exportada.csv` con el siguiente formato:

```csv
fecha,hora_inicio,hora_fin,tarea
2025-09-05,08:00,10:00,Estudiar Redes
2025-09-06,08:00,08:45,Revisión informe
```

---

## ✨ Conclusiones
- Se implementó un **servidor MCP local no trivial** que organiza tiempo y tareas.  
- El proyecto demuestra la **aplicación de protocolos en la capa de aplicación** (JSON-RPC).  
- Se integran conceptos de **planificación automática, manejo de prioridades y deadlines**, junto con persistencia en archivos JSON.  
- La solución es **extensible**, pudiendo integrarse a otros chatbots y agentes MCP.  

---

📌 **Autores:** Brandon Reyes Morales – Universidad del Valle de Guatemala  
📌 **Curso:** CC3067 – Redes de Computadoras