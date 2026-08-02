# MicroStrategy MCP Server

**Project Status:** Active Development

**Last Updated:** 2026-07-30

---

# 1. Vision

Build a production-quality **Python SDK** and **Model Context Protocol (MCP) Server** for MicroStrategy that enables AI assistants (ChatGPT, GitHub Copilot, Claude Desktop, VS Code, and other MCP-compatible clients) to securely interact with the MicroStrategy REST API.

The project follows a strict **SDK-first architecture**, where every capability is implemented and tested in the Python SDK before being exposed through the CLI or MCP Server.

```
               AI Assistant
(ChatGPT / Copilot / Claude / VS Code)

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

---

# 2. Development Principles

The project follows several architectural principles.

- SDK-first development
- One REST endpoint per module
- Business logic separated from REST calls
- CLI separated from SDK
- MCP layer only exposes SDK functions
- Small, independently testable commits
- Production-quality code over quick prototypes
- Modular parser architecture
- Clean console output suitable for production

---

# 3. Current Architecture

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

# 4. Coding Standards

Current project standards include:

- No REST calls inside CLI workflow
- One REST endpoint per API module
- CLI only orchestrates SDK calls
- Business logic belongs in SDK
- Parsing separated from REST communication
- Printer handles all console formatting
- SDK functions return Python objects
- Every feature must be independently testable
- Remove debugging code before committing
- Keep commits small and logically grouped

---

# 5. Current Features

## Authentication

- ✅ Login
- ⬜ Logout
- ⬜ Session Validation

---

## Session Management

- ✅ Authentication Token
- ✅ Project Context
- ✅ Changeset Context

---

## Project APIs

- ✅ List Projects
- ✅ Select Active Project

---

## Changesets

- ✅ Create Modeling Changeset
- ⬜ Close Changeset
- ⬜ Delete Changeset

---

## Folder APIs

- ✅ Browse Root Folders
- ✅ Browse Folder
- ✅ Browse ALL Root Folders
- ⬜ Folder Details

---

## Generic Search

Supported object types:

- ✅ Reports
- ✅ Metrics
- ✅ Attributes
- ✅ Facts
- ✅ Filters
- ✅ Documents
- ✅ Folders

---

## Object Details

Generic metadata extraction:

- ✅ Name
- ✅ Description
- ✅ Owner
- ✅ Object ID
- ✅ Creation Date
- ✅ Modification Date
- ✅ Version
- ✅ Folder Path

---

## Report Definition

Extract report metadata including:

- ✅ Rows
- ✅ Columns
- ✅ Metrics
- ✅ Filters
- ✅ Prompt Count
- ⬜ Page By
- ⬜ Thresholds
- ⬜ View Filters

---

## Report Execution

Current execution workflow:

- ✅ Create Report Instance
- ✅ Retrieve Prompt Definitions
- ✅ Prompt Detection
- ✅ Generate Prompt Payload
- ✅ Submit Prompt Answers
- ✅ Retrieve Report Data
- ✅ Delete Report Instance

---

## Grid Parsing

Current parser capabilities:

- ✅ Row Attributes
- ✅ Column Attributes
- ✅ Metrics
- ✅ Grid Metadata

Future:

- ⬜ Headers
- ⬜ Data Matrix
- ⬜ Totals
- ⬜ Subtotals
- ⬜ Cell Formatting

---

# 6. Implemented REST APIs

| REST API | Status |
|----------|--------|
| Login | ✅ |
| List Projects | ✅ |
| Create Changeset | ✅ |
| Browse Root Folders | ✅ |
| Browse Folder | ✅ |
| Search Objects | ✅ |
| Object Details | ✅ |
| Report Definition | ✅ |
| Create Report Instance | ✅ |
| Retrieve Report Prompts | ✅ |
| Submit Prompt Answers | ✅ |
| Retrieve Report Data | ✅ |
| Delete Report Instance | ✅ |

---

# 7. Development Roadmap

## Phase 1 — Foundation & Metadata SDK

### Completed

- ✅ Project Structure
- ✅ Configuration
- ✅ REST Client
- ✅ Authentication
- ✅ Project APIs
- ✅ Folder APIs
- ✅ Generic Search
- ✅ Object Details
- ✅ Report Definition
- ✅ Report Execution
- ✅ Prompt Handling
- ✅ Grid Metadata Parsing

Remaining:

- Session Validation
- Logout
- Better Error Handling
- Retry Logic

---

## Phase 2 — Report SDK

Upcoming work:

### Grid Parser

- Header Parser
- Metric Parser
- Attribute Parser
- Data Matrix Parser

### Result Export

- JSON
- CSV
- Excel
- PDF (where supported)

### Advanced Reports

- Prompted Reports
- View Filters
- Report Caching
- Pagination

---

## Phase 3 — Modeling SDK

- Create Attributes
- Create Facts
- Create Metrics
- Create Hierarchies
- Create Transformations
- Create Relationships
- Validate Schema
- Trigger Schema Update

---

## Phase 4 — Content Development SDK

- Reports
- Dossiers
- Cubes
- Filters
- Prompts
- Documents
- Users
- Security

---

## Phase 5 — MCP Server

Expose SDK functions as MCP tools.

Examples:

- login
- list_projects
- search_objects
- browse_folder
- execute_report
- create_metric
- create_attribute

---

## Phase 6 — AI Assistant

Natural language requests:

> Create a Revenue metric.

> Execute Regional Sales Report.

> Export the report to Excel.

> Create Customer Attribute.

> Build a report showing Revenue by Region.

---

# 8. Current Workflow

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

Browse Root Folder
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

Report Definition
   │
   ▼

Execute Report
   │
   ▼

Retrieve Prompts
   │
   ▼

Generate Prompt Payload
   │
   ▼

Submit Answers
   │
   ▼

Retrieve Report Data
   │
   ▼

Delete Report Instance
```

---

# 9. Deferred Features

The following items are intentionally postponed.

- Recursive Project Explorer
- Metadata Inventory Generator
- Full Project Crawl
- Bulk Object Export
- Object Dependency Analyzer

---

# 10. Recent Milestones

Completed during the latest development cycle:

- Report Definition API
- Changeset API
- Report Execution Workflow
- Prompt Handling
- Grid Metadata Parser
- Cleaner CLI Output
- Removal of Debug Logging
- Production-ready Console Formatting

---

# 11. Future SDK Structure

```
api/
services/
models/
parsers/
utils/
tests/
server.py
```

---

# 12. Planned Documentation

The following documentation will be added under `docs/`.

- Architecture Guide
- SDK Developer Guide
- MCP Integration Guide
- REST API Reference
- Sequence Diagrams
- CLI User Guide
- Example Workflows
- Contribution Guide

---

# 13. Progress Summary

| Area | Status |
|------|--------|
| Foundation | ✅ Nearly Complete |
| Metadata SDK | ✅ Nearly Complete |
| Report SDK | 🚧 In Progress |
| Modeling SDK | Planned |
| Content SDK | Planned |
| MCP Server | Planned |
| AI Assistant | Planned |

---

# 14. Notes

The Python SDK remains the primary deliverable.

The CLI is used only for interactive testing and demonstrations.

The MCP Server will remain a thin wrapper over SDK functionality.

Every new capability should:

- Be implemented in the SDK
- Be independently tested
- Be documented
- Be committed separately
- Only then be exposed through the MCP Server

This approach keeps the project maintainable, testable, and suitable for production-scale development.