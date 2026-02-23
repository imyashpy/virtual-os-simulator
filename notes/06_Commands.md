# CLI Commands — Design Notes

## What is the CLI?
- Simulates **user interaction with VOS** through text commands
- Commands interact with objects like **Process, ProcessManager, FileSystem, Scheduler**

---

## Example Commands and Their Mapping

| Command        | Object / Method Called            | Purpose |
|----------------|----------------------------------|---------|
| `ps`           | ProcessManager.list_processes()  | List all processes |
| `kill <pid>`   | ProcessManager.kill_process(pid) | Kill a process |
| `start <pid>`  | Process.start()                  | Make process READY |
| `run <pid>`    | Scheduler.schedule() / Process.run() | Execute process |
| `touch <file>` | FileSystem.create_file()         | Create new file |
| `cat <file>`   | File.read()                      | Read file content |
| `ls`           | Directory.list()                 | List directory contents |
| `rm <file>`    | File.delete()                    | Remove file |
| `mkdir <dir>`  | Directory.add_directory()        | Create new directory |

---

## Command Handling Logic
1. CLI parses user input
2. Identifies command and arguments
3. Maps to **method calls** on objects
4. Checks **permissions and rules**
5. Executes action, returns output

---

## Rules / Invariants
- Invalid commands → return error
- Permission checks before each action
- State validation for processes (e.g., cannot run TERMINATED process)
- All commands are **facades** over objects — no direct state manipulation

---

## OOP Lessons
- Encapsulation → CLI does not manipulate objects internally  
- Delegation → CLI calls methods of objects  
- Command design → mapping input → object actions  

---

✅ Summary:
> CLI = user-facing interface, converts text commands into **object method calls** safely

# Diagrams / Visuals — ASCII / Notes

## 1️⃣ Overall VOS Architecture

Kernel
├── ProcessManager
│ ├── Process(pid=1)
│ ├── Process(pid=2)
│ └── Process(pid=3)
├── Scheduler
│ └── ready_queue → decides RUNNING process
└── FileSystem
├── /
│ ├── home/
│ │ ├── user1/
│ │ │ └── file1.txt
│ │ └── user2/
│ │ └── notes.md
│ └── etc/
│ └── config.txt




## 2️⃣ Process Lifecycle with Queues

NEW → start() → READY (ready_queue)
READY → schedule() → RUNNING
RUNNING → wait() → WAITING (waiting_queue)
WAITING → wake() → READY (ready_queue)
RUNNING → terminate() → TERMINATED




## 3️⃣ Scheduler Queue Options

Ready Queue Options:

FIFO Queue: process run in order

Circular Queue: round-robin, rotates

Deque: flexible, add/remove front/back

Priority Queue: highest priority process first



## 4️⃣ FileSystem Tree Example

/
├── home/
│ ├── user1/
│ │ ├── file1.txt
│ │ └── file2.txt
│ └── user2/
│ └── notes.md
└── etc/
└── config.txt