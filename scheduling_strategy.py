from abc import ABC, abstractmethod

class SchedulingStrategy(ABC):

    @abstractmethod
    def run(self, ready_queue):
        pass
