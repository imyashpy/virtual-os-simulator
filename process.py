# class Process:
#     def __init__(self, pid):
#         self.pid = pid
#         self.state = "NEW"


#day 16 adding time slice!
# class Process:
#     def __init__(self, pid, burst_time):
#         self.pid = pid
#         self.state = "NEW"
#         self.remaining_time = burst_time



#day 19
#addding enum
from process_state import ProcessState


class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.state = ProcessState.NEW #new thing!
        self.remaining_time = burst_time



