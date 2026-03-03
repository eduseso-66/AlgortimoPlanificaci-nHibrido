from src.schedulers.real_time import RealTimeScheduler
from src.schedulers.fair_share import FairShareScheduler
from src.schedulers.unix_tradicional import UnixScheduler
from collections import deque

class Kernel:
    def __init__(self):
        self.rt_queue = []
        self.user_groups = {} 
        self.running_process = None
        self.clock = 0

    def add_process(self, process):
        if process.priority < 10:
            self.rt_queue.append(process)
        else:
            if process.user_id not in self.user_groups:
                self.user_groups[process.user_id] = deque()
            self.user_groups[process.user_id].append(process)

    def select_next_process(self):
        next_p = RealTimeScheduler.get_next(self.rt_queue)
        if next_p: return next_p

        target_user = FairShareScheduler.select_user_group(self.user_groups)
        
        if target_user:
            user_queue = list(self.user_groups[target_user])
            sorted_tasks = UnixScheduler.sort_by_unix_priority(user_queue)
            
            chosen = sorted_tasks[0]
            self.user_groups[target_user].remove(chosen)
            return chosen
            
        return None

    def tick(self):
        self.clock += 1
        if self.running_process:
            self.running_process.remaining_time -= 1
            self.running_process.update_vruntime(1, len(self.user_groups))