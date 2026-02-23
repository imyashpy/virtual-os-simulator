# ProcessManager — Detailed Design

## What is ProcessManager?
- Creates, tracks, and manages all processes
- Kernel delegates process control here
- Responsibilities:
  - Factory → create new processes
  - Registry → track active processes
  - Police → kill, cleanup, inspect

## Core Attributes
- `process_list`: dict `{pid: Process}` — all active processes
- `next_pid`: integer, auto-incrementing PID
- Optional:
  - `max_processes`: limit total processes
  - `terminated_list`: keeps terminated processes for cleanup/logging

## Actions / Methods

### `create_process(name, owner, priority=0)`
- Create new Process object
- Assign unique PID
- Add to `process_list`
- Return Process object
- Rules:
  - Cannot create if system is “full”
  - PID must be unique

### `kill_process(pid)`
- Terminate process by PID
- Calls `process.kill()`
- Remove from `process_list`
- Optional → move to `terminated_list`
- Rules:
  - Cannot kill non-existent process
  - Must update registry

### `get_process(pid)`
- Return Process object or None
- Use case: CLI commands like `ps`, `info <pid>`

### `list_processes(state_filter=None)`
- Return all or filtered processes
- Use case: simulate `ps` command

### `cleanup_terminated()`
- Remove dead processes from memory
- Simulates OS cleanup of zombie processes

## Rules / Invariants
- PID must be unique
- ProcessManager owns all processes
- Cannot exceed `max_processes`
- Processes are manipulated via their own methods only

## OOP Lessons
- Composition → Kernel owns ProcessManager
- Ownership → Processes managed centrally
- Lifecycle enforcement → ensures proper creation → RUNNING → TERMINATED
- Extensibility → easy to add scheduler, priorities, resource limits

## Mini Diagram
- Kernel
- └── ProcessManager
- ├── Process(pid=1, state=RUNNING)
- ├── Process(pid=2, state=WAITING)
- └── Process(pid=3, state=TERMINATED)