from scheduling_strategy import SchedulingStrategy
from process_state import ProcessState


class RoundRobinStrategy(SchedulingStrategy):

    def run(self, ready_queue):
        if not ready_queue:
            #check if queue is empty!
            print("No READY process to run")
            return

        process = ready_queue.pop(0)
        process.state = ProcessState.RUNNING
        print(f"Running Process {process.pid}")

        process.remaining_time -= 1

        if process.remaining_time > 0:
            process.state = ProcessState.READY
            ready_queue.append(process)
            print(f"Process {process.pid} time slice over, moved back to READY")
        else:
            process.state = ProcessState.TERMINATED
            print(f"Process {process.pid} has TERMINATED")
