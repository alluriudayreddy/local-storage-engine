Local Storage Engine

Description

Local Storage Engine is a modular Python CLI application for managing product/inventory records with persistent local JSON storage.

The system supports creating, viewing, updating, deleting, and searching records through a terminal interface.


Features

* Add new records
* View all records
* Update records by ID
* Delete records with confirmation
* Search by ID
* Search by Name
* Automatic JSON save/load
* Input validation
* Structured modular codebase

Record Fields

* ID
* Name
* Price
* Quantity
* Category
* Brand
* Status
* Created Time

Tech Stack

* Python
* JSON
* File Handling
* CLI

Project Structure

local-storage-engine/
│
├── src/
│   ├── main.py
│   ├── engine.py
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

1. Load records from storage.json
2. Show CLI menu
3. Perform CRUD/Search actions
4. Save updated data automatically

Sample Record

{
  "id": 1,
  "name": "Phone",
  "price": 25000,
  "quantity": 5,
  "category": "Electronics",
  "brand": "Samsung",
  "status": "Active",
  "created_at": "2026-04-23 10:15:00"
}

Learning Outcomes

* Python modular architecture
* CRUD systems
* JSON persistence
* Validation logic
* Search logic
* CLI design
* Real-world data modeling

Run

python3 src/main.py
