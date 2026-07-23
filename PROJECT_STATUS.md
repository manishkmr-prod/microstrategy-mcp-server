# MicroStrategy MCP Server

**Project Status:** Active Development

*Last Updated: 2026-07-23*

------------------------------------------------------------------------

# 1. Vision

Build a production-quality **Python SDK** and **Model Context Protocol
(MCP) Server** for MicroStrategy that enables AI assistants (ChatGPT,
GitHub Copilot, Claude Desktop, VS Code, etc.) to securely interact with
the MicroStrategy REST API.

The project follows an **SDK-first** approach:

    AI Assistant
          │
          ▼
    MCP Server
          │
          ▼
    Python SDK
          │
          ▼
    MicroStrategy REST API
          │
          ▼
    MicroStrategy Platform

------------------------------------------------------------------------

# 2. Development Principles

-   SDK-first architecture
-   One REST endpoint per module
-   Business logic separated from REST calls
-   CLI separated from SDK
-   MCP layer only exposes SDK functions
-   Small, testable commits
-   Incremental development

------------------------------------------------------------------------

# 3. Current Architecture

``` text
Strategy MCP/

api/
    authentication.py
    folders.py
    projects.py
    search.py

utils/
    menu.py
    object_types.py

tests/

config.py
mstr_client.py
main.py
server.py

README.md
CHANGELOG.md
PROJECT_STATUS.md
```

------------------------------------------------------------------------

# 4. Coding Standards

-   No REST calls inside `main.py`
-   One REST endpoint per API module
-   `main.py` only orchestrates
-   Menu logic belongs in `utils/menu.py`
-   Reusable SDK functions before MCP tools
-   Every new feature should be independently testable

------------------------------------------------------------------------

# 5. Current Features

Completed:

-   Login
-   Session handling
-   Environment configuration
-   Project selection
-   Root folder browsing
-   Folder browsing
-   Browse ALL root folders
-   Generic object search
-   ObjectType enumeration
-   Menu abstraction

------------------------------------------------------------------------

# 6. Implemented REST APIs

  API                   Status
  --------------------- --------
  Login                 ✅
  List Projects         ✅
  Browse Root Folders   ✅
  Browse Folder         ✅
  Search Objects        ✅
  Object Details        ⬜

------------------------------------------------------------------------

# 7. Development Roadmap

## Phase 1 -- Foundation & Metadata SDK

### Milestone 1 -- Project Foundation

-   ✅ Project structure
-   ✅ Git
-   ✅ Virtual environment
-   ✅ Configuration
-   ✅ .env Likelihood: **100%**

### Milestone 2 -- REST Client

-   ✅ GET
-   ✅ POST
-   ⬜ PUT
-   ⬜ PATCH
-   ⬜ DELETE
-   Error handling Likelihood: **100%**

### Milestone 3 -- Authentication

-   ✅ Login
-   ⬜ Logout
-   ⬜ Session validation Likelihood: **100%**

### Milestone 4 -- Project APIs

-   ✅ List Projects
-   ⬜ Project Details Likelihood: **100%**

### Milestone 5 -- Folder APIs

-   ✅ Root folders
-   ✅ Browse folder
-   ✅ Browse ALL root folders
-   ⬜ Folder details Likelihood: **100%**

### Milestone 6 -- Generic Search

-   ✅ Reports
-   ✅ Metrics
-   ✅ Attributes
-   ✅ Facts
-   ✅ Filters
-   ✅ Documents
-   ✅ Folders
-   ✅ Generic search Likelihood: **100%**

### Milestone 7 -- Object Details

#### Generic Object Details

-   Name
-   ID
-   Type
-   Description
-   Owner
-   Dates
-   Version
-   Path

Likelihood: **95--100%**

#### Report Details

-   Template
-   Metrics
-   Attributes
-   Filters
-   Prompts Likelihood: **95%**

#### Metric Details

-   Formula
-   Dimensionality Likelihood: **85--95%**

#### Attribute Details

-   Forms
-   Lookup
-   Relationships Likelihood: **85--95%**

#### Filter Details

-   Qualification
-   Expression Likelihood: **85--95%**

#### Cube Details

Likelihood: **85--90%**

#### Dossier Details

Likelihood: **75--85%**

------------------------------------------------------------------------

## Phase 2 -- Report SDK

### Milestone 8 -- Report Metadata

-   Report definition
-   Template
-   Metrics
-   Attributes
-   Filters
-   Prompts

### Milestone 9 -- Report Execution

-   Execute report
-   Handle prompts
-   Retrieve results

### Milestone 10 -- Export

-   JSON
-   CSV
-   Excel
-   PDF (where supported)

Likelihood: **95--100%**

------------------------------------------------------------------------

## Phase 3 -- Modeling SDK

### Milestone 11

-   Create Attributes
-   Create Facts
-   Create Metrics
-   Create Hierarchies

### Milestone 12

-   Relationships
-   Logical tables

### Milestone 13

-   Validate Schema
-   Trigger Schema Update

Likelihood: **70--90%**

------------------------------------------------------------------------

## Phase 4 -- Content Development SDK

-   Reports
-   Dossiers
-   Cubes
-   Filters
-   Prompts
-   Users
-   Security

Likelihood: **80--90%**

------------------------------------------------------------------------

## Phase 5 -- MCP Server

Expose SDK functions as MCP tools:

-   login
-   list_projects
-   browse_folder
-   search_objects
-   get_object_details
-   execute_report
-   export_results
-   create_report
-   create_metric
-   create_attribute

Likelihood: **100%**

------------------------------------------------------------------------

## Phase 6 -- AI Assistant

Natural language requests such as:

-   Create Revenue metric
-   Build Customer attribute
-   Execute Sales report
-   Export report to Excel

Likelihood: **90--95%**

------------------------------------------------------------------------

# 8. Current Workflow

    Login
       ↓
    Projects
       ↓
    Select Project
       ↓
    Browse Root Folder
       ↓
    Browse Folder
       ↓
    Search Objects
       ↓
    (Object Details - Next)

------------------------------------------------------------------------

# 9. Deferred Features

-   Recursive project explorer
-   Metadata inventory
-   Full project crawler

------------------------------------------------------------------------

# 10. Git History

-   Refactor Menu class
-   Browse ALL Root Folders

------------------------------------------------------------------------

# 11. Future SDK Structure

``` text
api/
services/
models/
utils/
server.py
```

------------------------------------------------------------------------

# 12. Future Documentation

Planned for `docs/`:

-   Architecture diagram
-   Sequence diagram
-   CLI screenshots
-   Demo GIF
-   MCP tool reference
-   API reference

------------------------------------------------------------------------

# 13. Success Tracking

  Phase                   Status        Likelihood
  ----------------------- ------------- ------------
  Foundation & Metadata   In Progress   95--100%
  Report SDK              Planned       95--100%
  Modeling SDK            Planned       70--90%
  Content SDK             Planned       80--90%
  MCP Server              Planned       100%
  AI Assistant            Planned       90--95%

------------------------------------------------------------------------

# 14. Notes

The SDK is the primary deliverable.

The MCP server should remain a thin layer that exposes SDK functionality
to AI assistants.

Every new capability should first be implemented, tested, and documented
in the SDK before being exposed as an MCP tool.
