"""
Servidor MCP-Schedulizer con manejo robusto de archivo JSON
-----------------------------------------------------------
Evita error si 'tasks_db.json' está vacío o dañado.
"""

from flask import Flask, request, jsonify
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)
TASKS_FILE = "tasks_db.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(params):
    tasks = load_tasks()
    tasks.append({
        "nombre": params.get("nombre"),
        "duracion": params.get("duracion"),
        "deadline": params.get("deadline"),
        "prioridad": params.get("prioridad"),
        "categoria": params.get("categoria")
    })
    save_tasks(tasks)
    return {"status": "tarea agregada correctamente", "tareas_totales": len(tasks)}

def list_tasks(_params):
    tasks = load_tasks()
    return {"tareas": tasks}

def remove_task(params):
    nombre = params.get("nombre")
    tasks = load_tasks()
    nuevas = [t for t in tasks if t["nombre"] != nombre]
    if len(nuevas) == len(tasks):
        return {"status": f"no se encontró tarea '{nombre}'"}
    save_tasks(nuevas)
    return {"status": f"tarea '{nombre}' eliminada", "tareas_totales": len(nuevas)}

def generate_schedule(params):
    tasks = load_tasks()
    fecha_inicio = datetime.fromisoformat(params.get("fecha_inicio"))
    disponibilidad = params.get("disponibilidad", 240)
    schedule = []
    dia = fecha_inicio
    for tarea in tasks:
        duracion = int(tarea["duracion"])
        if duracion > disponibilidad:
            continue
        block = {
            "fecha": dia.strftime("%Y-%m-%d"),
            "hora_inicio": "08:00",
            "hora_fin": (datetime.strptime("08:00", "%H:%M") + timedelta(minutes=duracion)).strftime("%H:%M"),
            "tarea": tarea["nombre"]
        }
        schedule.append(block)
        dia += timedelta(days=1)
    return {"agenda": schedule}

@app.route("/", methods=["POST"])
def handle_rpc():
    request_json = request.get_json()
    method = request_json.get("method")
    params = request_json.get("params", {})

    if method == "add_task":
        result = add_task(params)
    elif method == "list_tasks":
        result = list_tasks(params)
    elif method == "generate_schedule":
        result = generate_schedule(params)
    elif method == "remove_task":
        result = remove_task(params)
    else:
        return jsonify({"error": "Método no soportado"}), 400

    return jsonify({
        "jsonrpc": "2.0",
        "result": result,
        "id": request_json.get("id")
    })

if __name__ == "__main__":
    app.run(port=8000)