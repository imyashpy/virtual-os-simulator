# VOS (Virtual Operating System Simulator) — Overview

## What is VOS?
- A Python program simulating OS concepts (processes, files, users)
- Pure simulation — NOT a real OS
- Purpose:
  - Practice advanced OOP
  - Model real-world systems
  - Create portfolio-level project

## OOP Goals
- Encapsulation → each object manages its own state
- Composition → Kernel owns managers; managers own Processes
- Lifecycle modeling → NEW → READY → RUNNING → WAITING → TERMINATED
- Responsibility boundaries → separation of concerns
- State machines & guard logic → only valid transitions allowed

## Mental Diagram (simplified)
- Kernel
- └── ProcessManager
- ├── Process(pid=1, state=RUNNING)
- ├── Process(pid=2, state=WAITING)
- └── Process(pid=3, state=TERMINATED)


- Kernel = coordinator  
- ProcessManager = manager/factory/police  
- Process = self-contained object with its own state & actions
