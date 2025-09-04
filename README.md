## Estructura

Proyecto-1-Redes/

│
├── mcp_schedulizer/                 ← 📂 Carpeta raíz del proyecto (opcional)
│   ├── mcp_schedulizer.py        ← 🧠 Servidor Flask + JSON-RPC
│   ├── cliente_chatbot.py          ← 🤖 Cliente chatbot anfitrión (menú CLI)
│   ├── tasks_db.json                 ← 💾 Base de datos de tareas (JSON)
│   └── README.md                  ← 📄 Documentación en inglés (instrucciones + ejemplos)
│

¿Qué hace este servidor?

* Expone un endpoint JSON-RPC en `http://localhost:8000/`
* Soporta 3 métodos:
  * `add_task(...)`: agrega tareas a `tasks_db.json`
  * `list_tasks()`: retorna todas las tareas guardadas
  * `generate_schedule(...)`: crea una agenda ficticia desde una fecha de inicio
* Usa Flask puro, sin SDK externo.

## ¿Cómo correrlo?

1. Instala Flask:

<pre class="overflow-visible!" data-start="665" data-end="694"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install flask
</span></span></code></div></div></pre>

2. Ejecuta el servidor:

<pre class="overflow-visible!" data-start="721" data-end="758"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python mcp_schedulizer.py
</span></span></code></div></div></pre>




## Opción 1: Agregar tareas

Ingresa estas tareas **una por una** (repite opción 1 tres veces):

---

### Tarea 1

<pre class="overflow-visible!" data-start="306" data-end="462"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Nombre de la tarea:</span><span></span><span>Revisión</span><span></span><span>informe</span><span>
</span><span>Duración</span><span></span><span>(minutos):</span><span></span><span>45</span><span>
</span><span>Fecha</span><span></span><span>límite</span><span></span><span>(YYYY-MM-DDTHH:MM):</span><span></span><span>2025-09</span><span>-06T18:00</span><span>
</span><span>Prioridad:</span><span></span><span>alta</span><span>
</span><span>Categoría:</span><span></span><span>universidad</span><span>
</span></span></code></div></div></pre>

---

### Tarea 2

<pre class="overflow-visible!" data-start="485" data-end="633"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Nombre de la tarea:</span><span></span><span>Lavar</span><span></span><span>ropa</span><span>
</span><span>Duración</span><span></span><span>(minutos):</span><span></span><span>30</span><span>
</span><span>Fecha</span><span></span><span>límite</span><span></span><span>(YYYY-MM-DDTHH:MM):</span><span></span><span>2025-09</span><span>-08T20:00</span><span>
</span><span>Prioridad:</span><span></span><span>media</span><span>
</span><span>Categoría:</span><span></span><span>personal</span><span>
</span></span></code></div></div></pre>

---

### Tarea 3

<pre class="overflow-visible!" data-start="656" data-end="811"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Nombre de la tarea:</span><span></span><span>Estudiar</span><span></span><span>Redes</span><span>
</span><span>Duración</span><span></span><span>(minutos):</span><span></span><span>120</span><span>
</span><span>Fecha</span><span></span><span>límite</span><span></span><span>(YYYY-MM-DDTHH:MM):</span><span></span><span>2025-09</span><span>-10T23:59</span><span>
</span><span>Prioridad:</span><span></span><span>alta</span><span>
</span><span>Categoría:</span><span></span><span>universidad</span><span>
</span></span></code></div></div></pre>

---

## Opción 2: Listar tareas

Luego de agregar las tareas, selecciona la opción 2:

<pre class="overflow-visible!" data-start="902" data-end="940"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Selecciona una opción (</span><span>1</span><span>-</span><span>4</span><span>): </span><span>2</span><span>
</span></span></code></div></div></pre>

📋 Deberías ver algo como:

<pre class="overflow-visible!" data-start="970" data-end="1158"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Tareas actuales:</span><span>
</span><span>-</span><span></span><span>Revisión</span><span></span><span>informe</span><span></span><span>|</span><span></span><span>45</span><span></span><span>min</span><span></span><span>|</span><span></span><span>deadline:</span><span></span><span>2025-09</span><span>-06T18:00</span><span>
</span><span>-</span><span></span><span>Lavar</span><span></span><span>ropa</span><span></span><span>|</span><span></span><span>30</span><span></span><span>min</span><span></span><span>|</span><span></span><span>deadline:</span><span></span><span>2025-09</span><span>-08T20:00</span><span>
</span><span>-</span><span></span><span>Estudiar</span><span></span><span>Redes</span><span></span><span>|</span><span></span><span>120</span><span></span><span>min</span><span></span><span>|</span><span></span><span>deadline:</span><span></span><span>2025-09</span><span>-10T23:59</span><span>
</span></span></code></div></div></pre>

---

## Opción 3: Generar horario

Selecciona:

<pre class="overflow-visible!" data-start="1210" data-end="1248"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Selecciona una opción (</span><span>1</span><span>-</span><span>4</span><span>): </span><span>3</span><span>
</span></span></code></div></div></pre>

Y luego responde:

<pre class="overflow-visible!" data-start="1269" data-end="1350"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Fecha de inicio (YYYY-MM-</span><span>DD</span><span>): </span><span>2025</span><span>-</span><span>09</span><span>-</span><span>05</span><span>
Minutos disponibles por día: </span><span>240</span><span>
</span></span></code></div></div></pre>

🕒 Resultado esperado (simulado):

<pre class="overflow-visible!" data-start="1387" data-end="1538"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Agenda generada:</span><span>
</span><span>2025-09-05 </span><span>08</span><span>:00</span><span></span><span>-</span><span></span><span>08</span><span>:45</span><span></span><span>-></span><span></span><span>Revisión</span><span></span><span>informe</span><span>
</span><span>2025-09-06 </span><span>08</span><span>:00</span><span></span><span>-</span><span></span><span>08</span><span>:30</span><span></span><span>-></span><span></span><span>Lavar</span><span></span><span>ropa</span><span>
</span><span>2025-09-07 </span><span>08</span><span>:00</span><span></span><span>-</span><span></span><span>10</span><span>:00</span><span></span><span>-></span><span></span><span>Estudiar</span><span></span><span>Redes</span><span>
</span></span></code></div></div></pre>

## Opción 4: Salir

Simplemente:

<pre class="overflow-visible!" data-start="1581" data-end="1619"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Selecciona una opción (</span><span>1</span><span>-</span><span>4</span><span>): </span><span>4</span><span>
</span></span></code></div></div></pre>

Y verás:

<pre class="overflow-visible!" data-start="1631" data-end="1650"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>Saliendo...</span></span></code></div></div></pre>
