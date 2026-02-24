
from scheduling_strategy import SchedulingStrategy
from process_state import ProcessState


class FCFSSchedulingStrategy(SchedulingStrategy):

    def run(self, ready_queue):
        if not ready_queue:
            print("No READY process to run")
            return

        process = ready_queue.pop(0)
        process.state = ProcessState.RUNNING 
        print(f"Running Process {process.pid} (FCFS)")

        # Run completely
        while process.remaining_time > 0:
            process.remaining_time -= 1

        process.state = ProcessState.TERMINATED
        print(f"Process {process.pid} has TERMINATED")










