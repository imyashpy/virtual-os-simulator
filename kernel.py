# from scheduler import Scheduler
# from process_manager import ProcessManager
#
# class Kernel:
#     def __init__(self):
#         self.scheduler = Scheduler()
#         self.process_manager = ProcessManager()
#         # print("Kernel started")
#
#
# #
# # from scheduler import Scheduler
# # from process_manager import ProcessManager
# #
# # class Kernel:
# #     def __init__(self):
# #         self.scheduler = Scheduler()
# #         self.process_manager = ProcessManager()
# #         print("Kernel started")



#day 17
# from scheduler import Scheduler
# from process_manager import ProcessManager
# from round_robin_strategy import RoundRobinStrategy
#
# class Kernel:
#     def __init__(self):
#         strategy = RoundRobinStrategy()
#         self.scheduler = Scheduler(strategy)
#         self.process_manager = ProcessManager()



#day 18
from fcfs_strategy import FCFSSchedulingStrategy
from process_manager import ProcessManager
from scheduler import Scheduler

class Kernel:
    def __init__(self):
        strategy = FCFSSchedulingStrategy()
        self.scheduler = Scheduler(strategy)
        self.process_manager = ProcessManager()


