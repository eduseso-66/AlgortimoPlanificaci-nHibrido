class RealTimeScheduler:
    @staticmethod
    def get_next(queue):
        if not queue:
            return None
        queue.sort(key=lambda p: (p.priority, p.arrival_time))
        return queue.pop(0)