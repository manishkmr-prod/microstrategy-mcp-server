# Changelog

All notable changes to this project are documented in this file.

The format is inspired by **Keep a Changelog** and follows semantic versioning where practical during development.

---

# [Unreleased]

## Planned

### Report SDK

- Report result parser
- Header parser
- Metric parser
- Data matrix parser
- CSV export
- Excel export

### Modeling SDK

- Attribute creation
- Metric creation
- Fact creation
- Hierarchy creation
- Schema validation
- Schema update

### MCP Server

- Expose SDK functions as MCP tools
- Tool registration
- Natural language workflows

---

# [0.5.0] - 2026-07-30

## Added

### Report Execution

- Report Instance creation
- Report execution workflow
- Automatic Report Instance cleanup
- Report data retrieval

### Prompt Handling

- Retrieve report prompts
- Interactive prompt engine
- Prompt payload generation
- Prompt answer submission

### Report Metadata

- Report Definition API
- Report definition parser
- Report printer
- Report template metadata extraction

### Changesets

- Create Modeling Changeset
- Automatic Changeset context management

### Parsing Utilities

- Grid parser
- Header parser
- Metric parser
- Report parser

### SDK Modules

Added new SDK modules:

- report_executor.py
- report_data.py
- report_instances.py
- report_prompts.py
- prompt_answers.py

### Tests

- Grid parser unit tests

## Changed

- Workflow now supports complete report execution
- Cleaner console output
- Removed debugging output
- Removed raw REST response printing
- Removed final JSON response printing
- Improved SDK orchestration
- Better separation between API, parser and CLI layers

## Fixed

- Automatic deletion of report instances
- Cleaner production-ready execution flow
- Improved prompt handling workflow

---

# [0.4.0] - 2026-07-26

## Added

### Object Details

- Generic Object Details API
- Object metadata retrieval

### Reports

- Report Definition API
- Report metadata extraction

### SDK

- Additional reusable REST API wrappers
- Improved printer utilities

## Changed

- Search workflow now supports object selection followed by metadata retrieval.
- Improved separation between CLI and SDK.

---

# [0.3.0] - 2026-07-24

## Added

### Search

- Generic object search

Supported object types:

- Reports
- Metrics
- Attributes
- Facts
- Filters
- Documents
- Folders

### Utilities

- ObjectType enumeration
- Printer improvements

## Changed

- Search is now driven by object type selection.
- Cleaner CLI navigation.

---

# [0.2.0] - 2026-07-23

## Added

### Folder Navigation

- Browse Root Folders
- Browse Folder
- Browse ALL Root Folders

### CLI

- Improved navigation menus
- Folder display helper

## Changed

- Root folder menu now supports browsing all folders or a single folder.

---

# [0.1.0] - 2026-07-23

## Initial Release

### Added

### Foundation

- Project structure
- Git repository
- Virtual environment
- Environment configuration
- Configuration loader

### SDK

- REST client
- Authentication
- Session management
- Project selection

### APIs

- Login
- List Projects
- Browse Root Folders
- Browse Folder

### Utilities

- Menu abstraction
- ObjectType enumeration

### Documentation

- README
- PROJECT_STATUS
- CHANGELOG

## Changed

- Refactored menu handling into dedicated utility modules.
- Simplified CLI orchestration by separating business logic from presentation.

---

# Development Philosophy

The project follows an SDK-first development approach.

Every new capability is implemented in the following order:

1. REST API wrapper
2. SDK function
3. Parser (if required)
4. Unit tests
5. CLI integration
6. Documentation
7. MCP tool exposure (future)

This ensures every feature is independently testable before becoming available through the MCP Server.