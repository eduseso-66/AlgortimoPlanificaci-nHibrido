#formula simplificada de UNIX: Priority = Base + (CPU_usage / 2) + Nice
#esta formula se usa para ajustar la prioridad de los procesos xd
class UnixScheduler:
    @staticmethod
    def adjust_priority(process):
        usage_penalty = (process.burst_time - process.remaining_time) // 2
        dynamic_priority = 20 + usage_penalty + process.nice
        return dynamic_priority

    @staticmethod
    def sort_by_unix_priority(process_list):
        return sorted(process_list, key=lambda p: UnixScheduler.adjust_priority(p))