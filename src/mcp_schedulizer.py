from flask import Flask, request, jsonify
import json
from datetime import datetime, timedelta
import os
import csv

app = Flask(__name__)
TASKS_FILE = "tasks_db.json"
EXPORT_FILE = "agenda_exportada.csv"

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
    return {"tareas": load_tasks()}

def remove_task(params):
    id_tarea = params.get("id")
    tasks = load_tasks()
    if 0 <= id_tarea < len(tasks):
        eliminado = tasks.pop(id_tarea)
        save_tasks(tasks)
        return {"status": f"tarea '{eliminado['nombre']}' eliminada", "tareas_totales": len(tasks)}
    else:
        return {"status": "ID inválido"}

def prioridad_valor(p):
    return {"alta": 1, "media": 2, "baja": 3}.get(p.lower(), 4)

def generate_schedule(params):
    tasks = load_tasks()
    tasks.sort(key=lambda t: (datetime.fromisoformat(t["deadline"]), prioridad_valor(t["prioridad"])))
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

def export_schedule(_params=None):
    result = generate_schedule({
        "fecha_inicio": datetime.today().strftime("%Y-%m-%dT08:00"),
        "disponibilidad": 240
    })
    with open(EXPORT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["fecha", "hora_inicio", "hora_fin", "tarea"])
        writer.writeheader()
        for row in result["agenda"]:
            writer.writerow(row)
    return {"status": "Agenda exportada correctamente."}

@app.route("/", methods=["POST"])
def handle_rpc():
    req = request.get_json()
    method = req.get("method")
    params = req.get("params", {})

    if method == "add_task":
        result = add_task(params)
    elif method == "list_tasks":
        result = list_tasks(params)
    elif method == "generate_schedule":
        result = generate_schedule(params)
    elif method == "remove_task":
        result = remove_task(params)
    elif method == "export_schedule":
        result = export_schedule()
    else:
        return jsonify({"error": "Método no soportado"}), 400

    return jsonify({
        "jsonrpc": "2.0",
        "result": result,
        "id": req.get("id")
    })

if __name__ == "__main__":
    app.run(port=8000)