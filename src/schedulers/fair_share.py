class FairShareScheduler:
    @staticmethod
    def select_user_group(user_groups):
        if not user_groups:
            return None
            
        #aki se calcula el consumo de cpu xd
        usage = {}
        for user, processes in user_groups.items():
            if processes:
                usage[user] = sum(p.vruntime for p in processes)
        
        if not usage:
            return None
        
        #se regresa el usuario con menor consumo de cpu xd    
        return min(usage, key=usage.get)