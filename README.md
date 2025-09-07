# Readme Spanish

[🔗Cick for view🔗](REAME_Spanish.md)

# 📘 MCP-Schedulizer

## 🎯 Project Purpose

The **MCP-Schedulizer** project consists of developing a **local MCP server** that helps organize personal, academic, or work tasks.Its main function is to **generate an optimized schedule** based on the tasks registered by the user, taking into account:

- ⏳ Duration
- 📅 Deadline
- 🔝 Priority (high, medium, low)
- 🏷️ Category

This server can be invoked by a **host chatbot** that acts as a client, offering the user a simple console interface.

---

## 📚 Project Theme

The project belongs to the course **CC3067 – Computer Networks (UVG)** and is part of **Project 1: Use of an existing protocol**.
The central idea is to learn how to **implement a local MCP server** and a client that interacts with it, applying networking protocol concepts at the **application layer** of the OSI model.

---

## 🌐 Protocol Used

The system is based on **JSON-RPC 2.0**, a standard protocol for **remote procedure calls (RPC)** using JSON.

- **Client (chatbot)** → sends JSON-RPC requests via **HTTP POST**.
- **Server (MCP-Schedulizer)** → receives the request, executes the method (e.g., `add_task`, `list_tasks`, `generate_schedule`) and responds with a JSON object following the protocol specification.

This means the project **implements a real protocol**, combining:

- **HTTP** as transport.
- **JSON-RPC** as application protocol.
- Aligned with **MCP (Model Context Protocol)** by Anthropic.

---

## ⚙️ Implemented Features

- **Add task** with attributes (name, duration, deadline, priority, category).
- **List tasks** showing ID, name, duration, deadline, and priority.
- **Generate schedule** respecting order by `deadline` and `priority`.
- **Delete task** by **ID**.
- **Export schedule** to a `agenda_exportada.csv` file.

---

## 🛠️ Installation and Execution

### 1. Clone the repository

```bash
git clone <REPO_URL>
cd mcp-schedulizer
```

### 2. Install dependencies

```bash
pip install flask requests rich
```

### 3. Run the server

```bash
python mcp_schedulizer.py
```

This starts the server at `http://localhost:8000/`.

### 4. Run the client

In another terminal:

```bash
python cliente_chatbot.py
```

---

## 💻 Example of Use

```text
Host Chatbot - MCP Schedulizer
Available commands:
1. Add task
2. List tasks
3. Generate schedule
4. Delete task by ID
5. Export schedule
6. Exit

Select an option (1-6): 1
Task name: Study Networks
Duration (minutes): 120
Deadline (YYYY-MM-DDTHH:MM): 2025-09-10T23:59
Priority (high/medium/low): high
Category: university
```

---

## ▶️ Execution

### 1. Run the server

```bash
python mcp_schedulizer.py
```

Runs at `http://localhost:8000`.

### 2. Run the client (host chatbot)

```bash
python cliente_chatbot.py
```

---

## Step-by-Step Tests

### Option 1: Add tasks

Run option `1` and then enter:

#### Task 1

```
Name: Report Review
Duration: 45
Deadline: 2025-09-06T18:00
Priority: high
Category: university
```

#### Task 2

```
Name: Do Laundry
Duration: 30
Deadline: 2025-09-08T20:00
Priority: medium
Category: personal
```

#### Task 3

```
Name: Study Networks
Duration: 120
Deadline: 2025-09-10T23:59
Priority: high
Category: university
```

---

### Option 2: List tasks

```
Select an option (1-5): 2
```

### Option 3: Generate schedule

```
Select an option (1-5): 3

Start date: 2025-09-05
Minutes per day: 240
```

Expected result:

```
Generated schedule:
2025-09-05 08:00 - 08:45 -> Report Review
2025-09-06 08:00 - 08:30 -> Do Laundry
2025-09-07 08:00 - 10:00 -> Study Networks
```

---

### Option 4: Delete task

```
Select an option (1-5): 4
Task ID to delete: 3
```

Expected result:

```
Response:
{'status': "task 'Do Laundry' deleted", 'remaining_tasks': 2}
```

---

### Option 5: Exit

```
Select an option (1-5): 5
```

---

## OSI Layers Architecture

- **Application layer:** JSON-RPC 2.0 + MCP (message format and rules).
- **Transport layer:** HTTP (POST).
- **Network layer:** IP (localhost in this case).
- **Data Link and Physical layer:** OS-dependent (loopback interface).

---

## Schedule Export

With the **5** option of the client, a `agenda_exportada.csv` file is generated with the following format:

```csv
date,start_time,end_time,task
2025-09-05,08:00,10:00,Study Networks
2025-09-06,08:00,08:45,Report Review
```

---

## Conclusions

- A **non-trivial local MCP server** was implemented to organize time and tasks.
- The project demonstrates the **application of protocols at the application layer** (JSON-RPC).
- Concepts of **automatic scheduling, priority management, and deadlines** were integrated, along with JSON file persistence.
- The solution is **extensible**, making it possible to integrate with other chatbots and MCP agents.

---

 **Author:** Brandon Reyes Morales – Universidad del Valle de Guatemala
 **Course:** CC3067 – Computer Networks
