# 🤖 Project 1 Networks (Schedulizer Server)

[README (ESPAÑOL) -&gt; docs\README_EJECUCION_ES.md](docs/README_EJECUCION_ES.md)

This document describes the operation of the host agent developed for **Project 1 - Use of an existing protocol (CC3067)**, which uses an **LLM (Claude)** to interpret natural language instructions and execute tools through a **local MCP server** compatible with the official protocol.

Prepared by:
Brandon Reyes Morales 22992

---

## Available Tools

### **Local MCP Server (`mcp_schedulizer.py`)**

**Theme:** **Task management and schedule generation (Schedulizer)**

**Main functions:**

- Add tasks with duration, priority, and deadline
- List tasks (`list_tasks`)
- Generate an optimized schedule (`generate_schedule`)
- Save tasks locally in `tasks_db.json`

**Goal:** To be the core of the project, simulating an assistant that organizes your week based on your tasks. It can be extended to prioritize courses, work, rest, etc.

---

### **Remote MCP Server (Google Cloud Run)**

**Theme:** **Complementary educational services and well-being**

**Implemented functions:**

- `suggest_breaks`: suggests breaks between tasks in a schedule
- `daily_quote`: returns a motivational quote of the day

**Goal:** Extend the assistant with functions that support student or worker well-being, reinforcing productivity with motivation and healthy pauses. Serves as an example of a cloud-hosted server.

---

## 💬 Conversation Example

### Online server

Examples for the remote server on Google Cloud (FastAPI):

```
Can you suggest breaks if I study for 4 hours?
```

```
Give me a motivational quote
```

```
Add a task to study networks...
```

```
Write to file notes.txt
```

*Suggest_breaks — Pomodoro-style suggestions*

```
If I plan to study 3 hours, how many breaks should I take?
```

```
I’ll work for 5 hours straight, can you suggest pauses?
```

```
Can you give me a Pomodoro-style routine for 2.5 hours of study?
```

```
Give me a list of breaks if I plan a 4-hour study session
```

```
I want to organize my 6-hour workday with breaks every 45 minutes
```

```
Suggest work and break blocks for a 3-hour session
```

*daily_quote — Motivational quotes*

```
Give me a motivational quote to start my day
```

```
Do you have a positive quote to inspire me today?
```

```
I want an inspiring quote, please
```

```
Motivate me with a quote for studying
```

```
Can you give me a quote that helps me focus?
```

**How to verify that the remote server is being used?**

You should see something like this in the console:

```
🔗 Claude API used to interpret user instructions...
🔧 Executing 'suggest_breaks' with: {'hours': 4}
🌐 Using remote server on Google Cloud (endpoint /suggest_breaks)
📬 Response: { ... }
```

or

```
🔧 Executing 'daily_quote' with: {}
🌐 Using remote server on Google Cloud (endpoint /daily_quote)
```

---

### Local server

Examples of input for tasks (add_task):

```
Add a task to study for the networks final, 90 minutes, deadline 2025-09-30
```

```
Add a task to study for the networks exam, 90 minutes, deadline 2025-09-30, high priority, category university
```

```
Create a new task called “Read chapter 5 of artificial intelligence,” duration 60 minutes, deadline 2025-10-01, medium priority, category study
```

```
Add a task to review algorithms, duration 45 minutes, deadline 2025-09-25, low priority, category university
```

```
Add a task to write the networks lab report, 120 minutes, deadline 2025-10-02, category university, high priority
```

```
Register a task to review cybersecurity for 30 minutes before September 28, category work, medium priority
```

Examples to list tasks (list_tasks):

```
Show me all my tasks
```

```
What tasks do I have pending?
```

```
I want to see my task list
```

---

### Examples for the Filesystem MCP server (STDIO)

*write_file — Write or create files*

```
Create a file called resumen.txt with the content: OSI model layers and their functions
```

```
Write in a file called tareas.txt the following: study networks, program simulator
```

```
Save in notes/monday.txt: review Claude and remote server tasks
```

```
Create a folder 'reports' and inside save a file called info.txt with the content: MCP working correctly
```

```
Write in workspace/week1.txt the following: Monday - study, Tuesday - rest, Wednesday - lab
```

*read_file — Read existing files*

```
Read the file resumen.txt
```

```
Show me the content of tareas.txt
```

```
Open and read the file called info.txt in the reports folder
```

```
I want to see what I wrote in week1.txt
```

```
Can you read the file notes/monday.txt?
```

**How to know if the Filesystem server is being used?**

When you use one of these commands, your console should display:

```
🔧 Executing 'read_file' with: {'path': 'workspace/resumen.txt'}
📁 Using filesystem STDIO server (Filesystem MCP)
📬 Response:
{
  "output": {
    "content": "OSI model layers and their functions"
  }
}
```

---

## Folder and file structure

```
mcp-schedulizer-server-P1-Redes/
├── docs/                            # General and technical documentation
│   ├── screenshots/                 # Screenshots used in reports
│   │   ├── README_LLM_ES.md        # Write-up about LLM integration
│   │   ├── README_LLM_ES copy.md   # Duplicate/backup version
│   │   └── README.md               # General screenshot instructions
│   ├── captura wireshark 1.png     # Chatbot-server communication capture
│   ├── captura_wireshark_mcp_local.png
│   ├── captura_wireshark_server_remoto.png
│   ├── INFORME.docx                # Formal project report (editable)
│   ├── INFORME.pdf                 # Report in PDF format
│   └── prueba2.pcap                # Network capture file (Wireshark)
│
├── src/                            # Main MCP server source code
│   ├── tools/                      # Tool definitions
│   │   ├── add_task.tool.json
│   │   ├── definition.json
│   │   ├── generate_schedule.tool.json
│   │   ├── get_calendar.tool.json
│   │   ├── list_tasks.tool.json
│   │   └── remove_task.tool.json
│   ├── mcp_schedulizer.py          # Local MCP server that organizes tasks
│   ├── cliente_chatbot_fs_rr.py    # Client interacting with Claude and servers (FS + Remote)
│   └── mcp_log.txt                 # Execution log
│
├── workspace/                      # Local workspace (simulated user storage)
│   ├── university/                 # Example subfolder
│   └── agenda.txt                  # File generated with schedule
│
├── venv_mcp/                       # Python virtual environment
│   └── ... (internal files) ...
│
├── .env                            # Local config environment variables
├── .gitignore                      # Git ignored files
├── env.example                     # `.env` template
├── mcp_log.txt                     # Duplicate log outside `src`
├── README_LLM_EN.md                # English LLM integration guide
├── README_mcp_oficial_servers.md   # Instructions to run official MCP servers (FS, Git, etc.)
├── README.md                       # Main project instructions
├── README(1).md                    # Duplicate/backup README
├── requirements.txt                # Project dependencies
```

---

## ✅ Prerequisites

- Python 3.12+
- Libraries: `anthropic`, `requests`, `flask`
- Valid Anthropic API Key
- MCP server running at `http://localhost:5000`

```
pip install flask
pip install requests
pip install rich
pip install anthropic

pip install anthropic python-dotenv requests mcp
pip install flask anthropic python-dotenv requests mcp
```

---

## 📌 Notes

- This agent **does not use menus**, it acts as a natural conversational LLM.
- Claude must respond with exactly valid JSON, so a cleaning system was implemented for ``json ...`` responses from the model.
