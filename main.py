from kernel import Kernel

kernel = Kernel()

p1 = kernel.process_manager.create_process(3)
p2 = kernel.process_manager.create_process(2)
p3 = kernel.process_manager.create_process(1)


kernel.process_manager.make_ready(p1, kernel.scheduler)
kernel.process_manager.make_ready(p2, kernel.scheduler)
kernel.process_manager.make_ready(p3, kernel.scheduler)

# kernel.scheduler.run_next()
# kernel.scheduler.run_next()
# kernel.scheduler.run_next()
# kernel.scheduler.run_next()
while kernel.scheduler.ready_queue:
    kernel.scheduler.run_next()


# 🚀 Day 16 — Implemented Time Slicing (Round Robin Simulation)
#
# Today I upgraded my scheduler from non-preemptive to a simulated preemptive model.
#
# I implemented:
#
# • Time slicing (1 unit per run)
# • RUNNING → READY transition if work remains
# • RUNNING → TERMINATED when work completes
# • FIFO rotation using a queue
#
# Seeing the execution rotate like:
#
# P1 → P2 → P3 → P1 → P2 → P1
#
# made the concept of Round Robin finally click.
#
# The system now behaves closer to a real OS scheduler.
#
# Small steps. Deep foundations.

#OperatingSystems #RoundRobin #KernelDevelopment #Scheduler #SystemsThinking