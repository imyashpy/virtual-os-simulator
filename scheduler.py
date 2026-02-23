# class Scheduler:
#     def __init__(self):
#         self.ready_queue = []
#         # print("Scheduler initialized")
#
#     def add_process(self, process):
#         self.ready_queue.append(process)
#         print(f"Scheduler received Process {process.pid}")
#
#
#     def run_next(self):
#         if not self.ready_queue:
#             print("No READY process to run")
#             return
#
#         process = self.ready_queue.pop(0)
#         process.state = "RUNNING"
#         print(f"Running Process {process.pid}")
#
#         process.remaining_time -= 1
#
#         if process.remaining_time > 0:
#             process.state = "READY"
#             self.ready_queue.append(process)
#             print(f"Process {process.pid} time slice over, moved back to READY")
#         else:
#             process.state = "TERMINATED"
#             print(f"Process {process.pid} has TERMINATED")
#
#     def remove_process(self, process):
#         if process in self.ready_queue:
#             self.ready_queue.remove(process)








#day 17 logic
class Scheduler:
    def __init__(self, strategy):
        self.ready_queue = []
        self.strategy = strategy

    def add_process(self, process):
        self.ready_queue.append(process)
        print(f"Scheduler received Process {process.pid}")

    def remove_process(self, process):
        if process in self.ready_queue:
            self.ready_queue.remove(process)

    def run_next(self):
        self.strategy.run(self.ready_queue)












