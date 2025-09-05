"""
Cliente chatbot para interactuar con el servidor MCP-Schedulizer
Envia comandos JSON-RPC a http://localhost:8000/
"""

import json
import requests
from rich import print

SERVER_URL = "http://localhost:8000"

def enviar_rpc(method, params=None):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params or {},
        "id": 1
    }
    response = requests.post(SERVER_URL, json=payload)
    return response.json()

def menu():
    print("[bold cyan]Chatbot Anfitrión - MCP Schedulizer[/bold cyan]")
    print("Comandos disponibles:")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Generar horario")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            duracion = int(input("Duración (minutos): "))
            deadline = input("Fecha límite (YYYY-MM-DDTHH:MM): ")
            prioridad = input("Prioridad (alta/media/baja): ")
            categoria = input("Categoría: ")

            resultado = enviar_rpc("add_task", {
                "nombre": nombre,
                "duracion": duracion,
                "deadline": deadline,
                "prioridad": prioridad,
                "categoria": categoria
            })
            print("[green]Respuesta:[/green]", resultado)

        elif opcion == "2":
            resultado = enviar_rpc("list_tasks")
            print("[yellow]Tareas actuales:[/yellow]")
            for t in resultado["result"]["tareas"]:
                print("-", t["nombre"], "|", t["duracion"], "min | deadline:", t["deadline"])

        elif opcion == "3":
            inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            disponibilidad = int(input("Minutos disponibles por día: "))

            resultado = enviar_rpc("generate_schedule", {
                "fecha_inicio": inicio + "T08:00",
                "disponibilidad": disponibilidad
            })
            print("[magenta]Agenda generada:[/magenta]")
            for bloque in resultado["result"]["agenda"]:
                print(bloque["fecha"], bloque["hora_inicio"], "-", bloque["hora_fin"], "->", bloque["tarea"])

        elif opcion == "4":
            nombre = input("Nombre exacto de la tarea a eliminar: ")
            resultado = enviar_rpc("remove_task", {"nombre": nombre})
            print("[red]Respuesta:[/red]", resultado)

        elif opcion == "5":
            print("[bold red]Saliendo...[/bold red]")
            break
        else:
            print("[red]Opción inválida[/red]")

if __name__ == "__main__":
    main()