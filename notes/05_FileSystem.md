# FileSystem — Detailed Design

## What is the FileSystem in VOS?
- Simulates **virtual files and directories** in the system
- Provides basic operations: create, read, write, delete, move
- Handles **permissions**: who can access what

---

## Core Concepts

### 1️⃣ Files
- Attributes:
  - `name`: string
  - `content`: string or bytes
  - `owner`: user object / string
  - `permissions`: read/write/execute (e.g., 'rwx', simplified)
  - `size`: integer (optional, for simulation)
- Actions / Methods:
  - `read()` → return content if permission allows
  - `write(data)` → append or replace content if allowed
  - `delete()` → remove file

### 2️⃣ Directories
- Attributes:
  - `name`: string
  - `owner`: user
  - `permissions`: access control
  - `children`: dict `{name: File/Directory}`
- Actions / Methods:
  - `add_file(file)` → add new file
  - `add_directory(dir)` → add subdirectory
  - `delete(name)` → remove child
  - `list()` → list children

---

## Permissions Model
- Each file/directory has an **owner**
- Simplified permissions:
  - `r` → read
  - `w` → write
  - `x` → execute (optional for directories)
- Permission checks happen **before each action**
- Violations should raise **PermissionError** (simulated)

---

## Rules / Invariants
- Names must be unique within a directory
- Directories cannot contain themselves (no cycles)
- Root directory `/` always exists
- Operations only allowed if permissions permit
- FileSystem can be accessed via **FileManager** (optional manager class)

---

## OOP Lessons
- **Composition:** Directory contains files and subdirectories
- **Encapsulation:** Permissions + content managed internally
- **Hierarchy modeling:** tree-like structure
- **Method responsibility:** each object controls its own actions

---

## Mini Diagram

/
├── home/
│ ├── user1/
│ │ ├── file1.txt
│ │ └── file2.txt
│ └── user2/
│ └── notes.md
└── etc/
└── config.txt



---

✅ Summary:
> FileSystem = tree of directories and files with permissions, managed by objects.


