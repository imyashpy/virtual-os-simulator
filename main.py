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

#better way
while kernel.scheduler.ready_queue:
    kernel.scheduler.run_next()
