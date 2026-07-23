# MicroStrategy MCP Server

A production-quality **Model Context Protocol (MCP) Server** built in **Python** for **MicroStrategy**.

The project exposes MicroStrategy REST APIs as reusable Python SDK functions and MCP tools, enabling AI assistants such as **ChatGPT**, **GitHub Copilot**, **Claude Desktop**, and other MCP-compatible clients to interact with a MicroStrategy environment using natural language.

---

# Project Goals

The project is being developed in four phases.

## Phase 1 – Metadata Tools

- Login
- List Projects
- Browse Root Folders
- Browse Folder Contents
- Search Objects
- Get Object Details

---

## Phase 2 – Modeling Tools

- Create Schema Models
- Create Attributes
- Create Facts
- Build Relationships
- Validate Schema
- Trigger Schema Updates

---

## Phase 3 – Development Tools

- Create Reports
- Execute Reports
- Create Dossiers
- Create Cubes
- Create Filters
- Create Metrics
- Export Report Results
- User and Security Administration

---

## Phase 4 – AI Assistant

Allow users to interact with MicroStrategy using natural language.

Examples:

```
Create a Revenue metric.

Build a Customer attribute.

Create a report showing Revenue by Region.

Execute Sales Summary report.

Export report results to Excel.
```

The AI assistant interprets the request, invokes the required MCP tools, and returns the result.

---

# Architecture

```
Strategy MCP

api/
authentication.py
projects.py
folders.py
search.py

utils/
menu.py
object_types.py

tests/

config.py
mstr_client.py
main.py
server.py
```

The project follows an **SDK-first architecture**.

Each REST endpoint is implemented as a reusable Python function.

The MCP server exposes those functions as AI tools.

---

# Technology Stack

- Python 3.x
- Requests
- python-dotenv
- MicroStrategy REST API
- Model Context Protocol (MCP)
- VS Code
- Git

---

# Current Features

- Authentication
- Session Management
- Project Selection
- Browse Root Folders
- Browse Folder Contents
- Generic Object Search
- Menu Utilities
- Object Type Enumeration

---

# Future Features

- Report Execution
- Cube Management
- Dossier Management
- Metadata Modeling
- Prompt Handling
- AI-powered Metadata Development

---

# Project Status

See:

- PROJECT_STATUS.md
- CHANGELOG.md

for the latest development progress.

---

# License

This project is intended for educational and development purposes.