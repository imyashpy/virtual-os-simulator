# Process — Detailed Design

## What is a Process?
- Represents a running or runnable program in VOS
- Stateful object with identity, owner, resources
- Conceptually: Process = data + rules + lifecycle

## Core Attributes
- `pid`: unique process ID, integer
- `name`: string, human-readable
- `owner`: user object (or string)
- `state`: NEW, READY, RUNNING, WAITING, TERMINATED
- Optional:
  - `priority`: integer, scheduling priority
  - `memory_allocated`: integer (fake memory units)
  - `cpu_time`: integer (tracking CPU usage)
  - `open_files`: list of file handles

## Actions / Methods
- `start()`: NEW → READY / READY → RUNNING
- `run()`: execute process
- `wait()`: RUNNING → WAITING
- `wake()`: WAITING → READY
- `kill()`: terminate process immediately
- `terminate()`: normal exit
- `info()`: inspect process details

## Rules / Invariants
- TERMINATED is final
- PID is unique
- Process cannot run if not READY
- Process does not self-register globally — ProcessManager handles it

## OOP Lessons
- Encapsulation → state protected by methods
- Lifecycle modeling → enforce valid transitions
- Responsibility boundaries → single responsibility principle
- State machine thinking → only valid state transitions allowed
