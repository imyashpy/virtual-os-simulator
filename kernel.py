
from fcfs_strategy import FCFSSchedulingStrategy
from process_manager import ProcessManager
from scheduler import Scheduler

class Kernel:
    def __init__(self):
        strategy = FCFSSchedulingStrategy()
        self.scheduler = Scheduler(strategy)
        self.process_manager = ProcessManager() #composition, instead of inheritence!


