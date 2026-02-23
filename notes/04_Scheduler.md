# Scheduler — Detailed Design

## What is a Scheduler?
- The Scheduler decides **which process gets CPU time and when**.
- In VOS:
  - It chooses the next **READY process** to run.
  - Ensures fair and organized execution.
- Think of it as a **traffic controller for processes**:
  READY → RUNNING → WAITING → READY → RUNNING …

---

## Why do we need a Scheduler?
- Multiple processes exist in the system.
- Only one process can “run” at a time (simplified VOS).
- Ensures **fairness**, prevents starvation.
- Teaches:
  - OOP design (separation of concerns)
  - Queue management
  - State transitions

---

## Core Responsibilities
1. Keep track of **READY processes**.
2. Decide which process should run next.
3. Handle **priorities** (optional).
4. Switch process states: READY ↔ RUNNING.
5. Work with **ProcessManager** (does NOT create or kill processes).

---

## Core Data Attributes

| Attribute           | Type       | Purpose |
|--------------------|------------|---------|
| `ready_queue`       | list       | Holds processes that are READY to run |
| `current_process`   | Process    | The process currently RUNNING |
| `strategy`          | string     | Scheduling strategy (`FIFO`, `RoundRobin`, `Priority`) |

---

## Core Actions / Methods

### 🔹 `add_process(process)`
- Add a READY process to the `ready_queue`.

### 🔹 `remove_process(process)`
- Remove a process from the queue (if TERMINATED or WAITING).

### 🔹 `get_next_process()`
- Returns the next process to run based on the scheduling strategy.

### 🔹 `schedule()`
- Performs the scheduling:
  - Current RUNNING → READY (if preempted)
  - Next READY → RUNNING
- Handles **round-robin or priority-based logic**.

---

## Rules / Invariants
- Only READY processes are scheduled.
- TERMINATED or WAITING processes are skipped.
- Scheduler **does not kill or create processes**.
- Scheduler only tells processes to `run()` or `pause()`.

---

## Optional Enhancements
- Support **multiple strategies** via polymorphism:
  - FIFO (first-in, first-out)
  - Round-robin
  - Priority-based
- Track **CPU time used** per process.
- Simulate **preemption** (force current process to yield CPU).

---

## OOP Lessons
- **Separation of concerns** → ProcessManager manages processes, Scheduler decides execution.
- **Polymorphism** → multiple scheduling strategies can be implemented.
- **Queue management** → ready processes stored and managed efficiently.
- **State transitions** → only valid transitions are allowed (READY ↔ RUNNING ↔ WAITING).

---

## Mini Diagram

ProcessManager → all processes
|
v
Scheduler → selects next process to RUN
|
v
Process(pid=X) → RUNNING
Process(pid=Y) → WAITING
Process(pid=Z) → READY


---

✅ Summary:

> Scheduler = “traffic controller” deciding **which process runs next”**  
> ProcessManager = “owns all processes”  
> Process = “performs its job when scheduler says RUN”
