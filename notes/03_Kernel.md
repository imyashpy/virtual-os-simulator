# Kernel — Detailed Design

## What is the Kernel?
- The Kernel is the **central coordinator** of VOS
- It connects all managers and components:
  - **ProcessManager** → owns processes
  - **Scheduler** → decides which process runs
  - **FileSystem** → manages files and directories
  - **CLI** → user interface to interact with the system
- Think of Kernel as the **brain of the virtual OS**

---

## Core Responsibilities
1. Initialize and hold references to all managers (ProcessManager, Scheduler, FileSystem)
2. Receive commands from CLI and delegate to the correct manager or object
3. Handle the **main loop**: scheduling, process execution, and system updates
4. Ensure rules and state transitions are enforced across components

---

## Core Data Attributes

| Attribute          | Type        | Purpose |
|-------------------|------------|---------|
| `process_manager`  | ProcessManager | Manages all processes |
| `scheduler`        | Scheduler      | Decides which process to run |
| `filesystem`       | FileSystem     | Holds virtual files and directories |
| `users`            | dict           | User accounts in the system (optional) |
| `running`          | bool           | Kernel loop state: is VOS running? |

---

## Core Methods / Actions

### 🔹 `start_system()`
- Initializes all components
- Starts main loop

### 🔹 `shutdown_system()`
- Terminates all running processes
- Cleans up resources
- Stops main loop

### 🔹 `execute_command(command_str)`
- Receives user command from CLI
- Parses command and delegates:
  - Process / Scheduler → process actions
  - FileSystem → file/directory actions
- Returns output / error messages

### 🔹 `main_loop()`
- Continuously schedules processes using Scheduler
- Handles state transitions
- Checks for terminated processes and cleans up
- Updates system state

---

## Rules / Invariants
- Kernel **never directly modifies process internals** → uses ProcessManager & Scheduler
- Kernel **never directly modifies filesystem internals** → uses FileSystem methods
- CLI commands always go through Kernel → ensures control and validation
- System can only run if `running=True`

---

## OOP Lessons
- **Composition:** Kernel contains all managers (ProcessManager, Scheduler, FileSystem)
- **Encapsulation:** Kernel provides a single interface to the system (CLI → Kernel → objects)
- **Separation of concerns:** Each manager handles its own domain
- **Responsibility inversion:** Kernel delegates tasks instead of doing everything itself

---

## Mini Diagram

CLI / User
|
v
Kernel
├── ProcessManager → manages Process objects
├── Scheduler → decides RUNNING process
└── FileSystem → manages files & directories


---

## Example Flow (Day-to-Day Usage)

1. User types command → `execute_command("ps")`
2. Kernel parses command → calls `ProcessManager.list_processes()`
3. Scheduler picks next process → RUNNING
4. Process executes → may read/write files via FileSystem
5. Loop continues until user exits → `shutdown_system()`

---

✅ Summary:
> Kernel = brain of VOS  
> Delegates responsibilities to ProcessManager, Scheduler, FileSystem  
> Provides a single interface (CLI) to interact with the system  
> Keeps the system organized, safe, and modular
