from process import Process
from process_state import ProcessState 


class ProcessManager:
    def __init__(self):
        self.next_pid = 1
        self.processes = []
        # print("Process Manager is ready")


    def create_process(self, burst_time):
        process = Process(self.next_pid, burst_time)
        print(f"Process {process.pid} created with state {process.state.name}")

        self.next_pid += 1
        return process

    def make_ready(self, process, scheduler):
        process.state =  ProcessState.READY #every "ready" changed to ProcessState.READY
        scheduler.add_process(process)
        print(f"Process {process.pid} moved to READY state")

    def make_waiting(self, process, scheduler):
        process.state =  ProcessState.WAITING 
        scheduler.remove_process(process)
        print(f"Process {process.pid} moved to WAITING state")

    def wake_process(self, process, scheduler):
        if process.state ==  ProcessState.WAITING:
            process.state =  ProcessState.READY
            scheduler.add_process(process)
            print(f"Process {process.pid} moved from WAITING to READY")
        else:
            print(f"Process {process.pid} is not in WAITING state")

    def terminate_process(self, process, scheduler):
        process.state =  ProcessState.TERMINATED
        scheduler.remove_process(process)
        print(f"Process {process.pid} terminated")


