# READY, RUNNING, WAITING, TERMINATED
import uuid

class Process:
    def __init__(self, name, burst_time, priority=0, nice=0, user_id="root"):
        self.pid = str(uuid.uuid4())[:8]
        self.name = name
        self.status = "READY" 
        
        #atributos de ejecucion
        self.burst_time = burst_time        
        self.remaining_time = burst_time    
        self.arrival_time = 0               
        
        #atributos para tiempo real
        self.priority = priority 
        
        # atributos para Linux/Fair-Share
        self.user_id = user_id              
        self.vruntime = 0.0                 
        
        #atributos para UNIX tradicional
        self.nice = nice                    
        self.cpu_usage_history = 0  
        #atributos para métricas de rendimiento
        self.completion_time = 0  
        self.waiting_time = 0         
        
    def __repr__(self):
        return f"[PID:{self.pid} | {self.name} | User:{self.user_id} | Rem:{self.remaining_time}s]"

    def update_vruntime(self, delta_time, total_weight):
        self.vruntime += delta_time * (1.0 / (self.nice + 21))