# MicroStrategy MCP Server

> A production-quality Python SDK and Model Context Protocol (MCP) Server for the MicroStrategy REST API.

Build, explore, execute, and automate MicroStrategy metadata and content using a clean Python SDK, an interactive CLI, or AI assistants such as ChatGPT, GitHub Copilot, Claude Desktop, and other MCP-compatible clients.

---

## Overview

MicroStrategy provides a comprehensive REST API for interacting with metadata, reports, dossiers, cubes, and administrative objects.

This project aims to provide a modern developer experience by building:

- A reusable Python SDK
- A Model Context Protocol (MCP) Server
- A modular REST API wrapper
- A CLI for interactive exploration
- AI-ready tools for natural language driven development

Rather than calling REST endpoints directly, developers and AI assistants interact with well-structured SDK functions.

---

## Vision

```
                    AI Assistant
        (ChatGPT / Copilot / Claude)

                    │
                    ▼

           Model Context Protocol
                (MCP Server)

                    │
                    ▼

             Python SDK Layer

                    │
                    ▼

       MicroStrategy REST API

                    │
                    ▼

          MicroStrategy Platform
```

The SDK is the foundation of the project.

The MCP Server simply exposes SDK functionality as AI tools.

---

# Project Goals

The project is being developed in six major phases.

| Phase | Description | Status |
|---------|-------------|--------|
| Phase 1 | Foundation & Metadata SDK | 🚧 In Progress |
| Phase 2 | Report Execution SDK | Planned |
| Phase 3 | Metadata Modeling SDK | Planned |
| Phase 4 | Content Development SDK | Planned |
| Phase 5 | MCP Server | Planned |
| Phase 6 | AI Assistant | Planned |

---

# Current Features

## Authentication

- Login
- Session Management
- Changeset Management

---

## Project Navigation

- List Projects
- Select Active Project

---

## Folder Navigation

- Browse Root Folders
- Browse Folder Contents
- Browse Entire Project Structure

---

## Metadata Search

Search any supported object type including:

- Reports
- Metrics
- Attributes
- Facts
- Filters
- Documents
- Folders

---

## Object Details

Retrieve metadata including:

- Name
- Description
- Owner
- Object ID
- Dates
- Version
- Folder Path

---

## Report Definition

Extract report metadata including:

- Row Attributes
- Column Attributes
- Metrics
- Filters
- Prompt Count

---

## Report Execution

Current capabilities include:

- Create Report Instance
- Detect Report Prompts
- Generate Prompt Payload
- Submit Prompt Answers
- Retrieve Report Data
- Parse Grid Metadata
- Delete Report Instance

---

# Project Structure

```
Strategy MCP/

api/
│
├── authentication.py
├── changesets.py
├── folders.py
├── object_details.py
├── projects.py
├── prompt_answers.py
├── report_data.py
├── report_executor.py
├── report_instances.py
├── report_prompts.py
├── reports.py
├── search.py

cli/
│
└── workflow.py

utils/
│
├── grid_parser.py
├── header_parser.py
├── menu.py
├── metric_parser.py
├── object_types.py
├── printer.py
├── prompt_engine.py
└── report_parser.py

tests/

config.py
main.py
mstr_client.py
server.py

README.md
CHANGELOG.md
PROJECT_STATUS.md
```

---

# Design Principles

The SDK follows several important architectural principles.

## SDK First

Every REST endpoint is implemented as a reusable Python function before being exposed through the CLI or MCP Server.

---

## One Endpoint Per Module

Each REST endpoint has its own module.

Example:

```
api/
    reports.py
    search.py
    folders.py
```

This keeps responsibilities isolated and simplifies testing.

---

## Thin CLI

The CLI only orchestrates SDK calls.

Business logic never belongs inside the CLI.

---

## Thin MCP Layer

The MCP Server will never contain business logic.

It simply exposes SDK functions as AI tools.

---

## Testability

Every feature is designed to be independently testable before integration.

---

# Development Roadmap

## Phase 1

Foundation & Metadata SDK

- Authentication
- Projects
- Folders
- Search
- Object Details
- Report Definition
- Report Execution

---

## Phase 2

Report SDK

- Prompt Handling
- Grid Parsing
- Export Results
- JSON Export
- CSV Export
- Excel Export

---

## Phase 3

Modeling SDK

- Create Attributes
- Create Facts
- Create Metrics
- Create Hierarchies
- Validate Schema
- Trigger Schema Updates

---

## Phase 4

Content Development SDK

- Reports
- Dossiers
- Cubes
- Filters
- Prompts
- Users
- Security

---

## Phase 5

Model Context Protocol

Expose SDK functions as MCP tools.

Example:

```
execute_report()

create_metric()

create_attribute()

list_projects()

search_objects()
```

---

## Phase 6

AI Assistant

Example prompts:

```
Create a Revenue metric.

Build a Customer attribute.

Create a report showing Revenue by Region.

Execute the Regional Sales Report.

Export report results to Excel.
```

---

# Technology Stack

- Python
- Requests
- python-dotenv
- MicroStrategy REST API
- Model Context Protocol (MCP)
- VS Code
- Git
- GitHub

---

# Current Workflow

```
Login
   │
   ▼

Select Project
   │
   ▼

Create Changeset
   │
   ▼

Browse Folder
   │
   ▼

Search Objects
   │
   ▼

Retrieve Object Details
   │
   ▼

Execute Report
   │
   ▼

Handle Prompts
   │
   ▼

Retrieve Report Data
```

---

# Documentation

Additional project documentation can be found here:

| Document | Description |
|----------|-------------|
| PROJECT_STATUS.md | Detailed engineering progress |
| CHANGELOG.md | Version history |
| docs/ *(planned)* | Architecture, API Reference, MCP Guide |

---

# Contributing

This project follows an incremental development approach.

Each feature should:

- Implement one REST endpoint
- Include reusable SDK logic
- Be independently testable
- Be documented
- Be committed as a small logical change

---

# License

This project is currently intended for educational, research, and development purposes.

Future licensing will be determined before the first public release.

---

## Project Status

🚧 **Actively Under Development**

The SDK is currently focused on building a complete foundation for MicroStrategy automation before exposing functionality through the MCP Server.