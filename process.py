from process_state import ProcessState

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.state = ProcessState.NEW 
        self.remaining_time = burst_time



