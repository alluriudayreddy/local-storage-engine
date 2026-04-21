Local Storage Engine

Description

Local Storage Engine is a modular Python CLI application for managing structured records with persistent local storage.

The system supports creating, viewing, updating, and deleting records while automatically saving data in a JSON file.

Core Features

 Create records
 View all records
 Update records by ID
 Delete records by ID
 Automatic save/load system
 Clean modular architecture

Tech Stack

Python
JSON
File Handling
CLI Interface

Project Structure

local-storage-engine/
│
├── src/
│   ├── main.py
│   ├── engine.py
│   ├── operations.py
│   ├── storage.py
│   ├── models.py
│   └── utils.py
│
├── data/
│   └── storage.json
│
├── README.md
└── .gitignore


Workflow

1. Load saved data on startup
2. Accept user input through CLI
3. Process CRUD operations
4. Persist updated data automatically

Sample Record

{
    "id": 1,
    "name": "Phone",
    "value": 25000
}

Key Learnings

Modular Python project structure
CRUD system logic
Lists and dictionaries
JSON persistence
Separation of concerns
Basic systems thinking

Run

python main.py

Future Scope

 Search functionality
 Better terminal formatting
 Input validation upgrades
 SQLite / Database migration
 Multi-category storage