import time

class Dispatcher:
    def __init__(self, kernel):
        self.kernel = kernel
        self.total_execution_time = 0

    def context_switch(self, new_process):
        """Simula el guardado de registros y carga del nuevo proceso"""
        if self.kernel.running_process:
            prev = self.kernel.running_process
            if prev.remaining_time > 0:
                print(f"[DISPATCHER] Pausando: {prev.name} (Contexto Guardado)")
                prev.status = "READY"
                self.kernel.add_process(prev)
        
        self.kernel.running_process = new_process
        if new_process:
            new_process.status = "RUNNING"
            print(f"[DISPATCHER] Cargando: {new_process.name} (PID: {new_process.pid})")

    def run_step(self):
        next_p = self.kernel.select_next_process()
        
        if next_p:
            self.context_switch(next_p)
        
        if self.kernel.running_process:
            p = self.kernel.running_process
            print(f"  ==> CPU Ejecutando: {p.name} | Restante: {p.remaining_time}s")
            
            self.kernel.tick() 
            self.total_execution_time += 1
            
            if p.remaining_time <= 0:
                print(f"[DISPATCHER] Finalizado: {p.name}")
                p.status = "TERMINATED"
                self.kernel.running_process = None
        else:
            print("  ==> CPU IDLE (Inactiva)")
            self.total_execution_time += 1