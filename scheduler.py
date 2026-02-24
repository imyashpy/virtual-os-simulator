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












