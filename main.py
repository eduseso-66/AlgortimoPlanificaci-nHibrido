"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ██████╗ ███████╗████████╗██████╗  ██████╗     ██████╗ ███████╗ ██████╗    ║
║     ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝██╔═══██╗   ║
║     ██████╔╝█████╗     ██║   ██████╔╝██║   ██║    ██████╔╝█████╗  ██║   ██║   ║
║     ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║    ██╔══██╗██╔══╝  ██║   ██║   ║
║     ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝    ██║  ██║███████╗╚██████╔╝   ║
║     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝    ║
║                                                                              ║
║           S I S T E M A   D E   P L A N I F I C A C I Ó N   H Í B R I D A  ║
║                                                                              ║
║                    RT (Tiempo Real) + Fair-Share + UNIX Tradicional        ║
║                                                                              ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
from src.models.process import Process
from src.core.kernel import Kernel
from src.core.dispatcher import Dispatcher
from src.schedulers.real_time import RealTimeScheduler
from src.schedulers.fair_share import FairShareScheduler
from src.schedulers.unix_tradicional import UnixScheduler




BANNER = """╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║     ██████╗ ███████╗████████╗██████╗  ██████╗     ██████╗ ███████╗ ██████╗    ║
║     ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗    ██╔══██╗██╔════╝██╔═══██╗   ║
║     ██████╔╝█████╗     ██║   ██████╔╝██║   ██║    ██████╔╝█████╗  ██║   ██║   ║
║     ██╔══██╗██╔══╝     ██║   ██╔══██╗██║   ██║    ██╔══██╗██╔══╝  ██║   ██║   ║
║     ██║  ██║███████╗   ██║   ██║  ██║╚██████╔╝    ██║  ██║███████╗╚██████╔╝   ║
║     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚═╝  ╚═╝╚══════╝ ╚═════╝    ║
║                                                                               ║
║           S I S T E M A   D E   P L A N I F I C A C I Ó N   H Í B R I D A     ║
║                                                                               ║
║                    RT (Tiempo Real) + Fair-Share + UNIX Tradicional           ║
║                                                                               ║
╚════════════════════════════════════════════════════════════════════════════╝"""



class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background colors
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    
    # Light variants
    LIGHT_RED = '\033[91m'
    LIGHT_GREEN = '\033[92m'
    LIGHT_YELLOW = '\033[93m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_MAGENTA = '\033[95m'
    LIGHT_CYAN = '\033[96m'


class Style:
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_banner():
        Style.clear_screen()
        print(Colors.CYAN + BANNER + Colors.RESET)
        print(Colors.YELLOW + "  Presiona ENTER para continuar..." + Colors.RESET)
        input()
        Style.clear_screen()
    
    @staticmethod
    def print_header(title):
        width = 70
        print(f"\n{Colors.BOLD}{Colors.BLUE}{'═' * width}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BLUE}  {title}{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.BLUE}{'═' * width}{Colors.RESET}\n")
    
    @staticmethod
    def print_subheader(title):
        print(f"\n{Colors.BOLD}{Colors.CYAN}▶ {title}{Colors.RESET}")
        print(f"{Colors.CYAN}{'─' * 50}{Colors.RESET}")
    
    @staticmethod
    def print_success(message):
        print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")
    
    @staticmethod
    def print_error(message):
        print(f"{Colors.RED}✗ {message}{Colors.RESET}")
    
    @staticmethod
    def print_warning(message):
        print(f"{Colors.YELLOW}⚠ {message}{Colors.RESET}")
    
    @staticmethod
    def print_info(message):
        print(f"{Colors.CYAN}ℹ {message}{Colors.RESET}")
    
    @staticmethod
    def print_process_status(process, status_color=None):
        #determina color baasado en el tipo de proceso
        if process.priority < 10:  
            type_color = Colors.RED
            type_label = "🔴 RT"
        elif process.user_id == "User_A":
            type_color = Colors.BLUE
            type_label = "🔵 USER_A"
        else:
            type_color = Colors.GREEN
            type_label = "🟢 USER_B"
        
        if status_color:
            status_str = f"{status_color}{process.status}{Colors.RESET}"
        elif process.status == "RUNNING":
            status_str = f"{Colors.LIGHT_GREEN}{Colors.BOLD}{process.status}{Colors.RESET}"
        elif process.status == "READY":
            status_str = f"{Colors.YELLOW}{process.status}{Colors.RESET}"
        elif process.status == "TERMINATED":
            status_str = f"{Colors.DIM}{process.status}{Colors.RESET}"
        else:
            status_str = process.status
        
        print(f"  {type_label} │ {type_color}{process.name:<20}{Colors.RESET} │ "
              f"PID: {process.pid:<6} │ {status_str} │ "
              f"Burst: {process.burst_time}s │ Rest: {process.remaining_time}s")
    
    @staticmethod
    def print_menu(options, title="MENÚ PRINCIPAL"):
      
        Style.print_header(title)
        
        for i, (key, description) in enumerate(options.items(), 1):
            if key == "0":
                print(f"  {Colors.RED}[0]{Colors.RESET}  {description}")
            else:
                print(f"  {Colors.CYAN}[{i}]{Colors.RESET}  {description}")
        
        print()
    
    @staticmethod
    def print_progress_bar(current, total, prefix='Progress', length=40):
  
        percent = current / total
        filled = int(length * percent)
        bar = '█' * filled + '░' * (length - filled)
        
        color = Colors.GREEN if percent == 1 else Colors.CYAN
        print(f"\r{color}{prefix}: |{bar}| {int(percent * 100)}%{Colors.RESET}", end='')
        if percent == 1:
            print()


# ═════════════════════════════════════════════════════════════════════════════
# Demos xd
# ═════════════════════════════════════════════════════════════════════════════

def create_demo_scenario(scenario_id):
   
    kernel = Kernel()
    dispatcher = Dispatcher(kernel)
    processes = []
    
    if scenario_id == 1:
        p1 = Process(name="Render_Video", burst_time=5, user_id="User_A")
        p2 = Process(name="Compilar_C", burst_time=4, user_id="User_B")
        p3 = Process(name="Navegador", burst_time=3, user_id="User_A")
        
        processes = [p1, p2, p3]
        scenario_name = "Básico: RT + Fair-Share"
        
    elif scenario_id == 2:
        p1 = Process(name="Navegador", burst_time=4, user_id="User_A")
        p2 = Process(name="Minado_BTC", burst_time=6, user_id="User_B")
        p3 = Process(name="Compilacion", burst_time=6, user_id="User_B")
        
        processes = [p1, p2, p3]
        scenario_name = "Stress Test: Fair-Share vs Monopolio"
        
    elif scenario_id == 3:
        p1 = Process(name="Editor_Texto", burst_time=5, user_id="User_A")
        p2 = Process(name="Descarga", burst_time=8, user_id="User_B")
        p3 = Process(name=" Antivirus", burst_time=4, user_id="User_A")
        p4 = Process(name="Musica", burst_time=3, user_id="User_B")
        
        processes = [p1, p2, p3, p4]
        scenario_name = "Prioridad Tiempo Real"
        
    elif scenario_id == 4:
        p1 = Process(name="Servidor_WEB", burst_time=6, user_id="User_A")
        p2 = Process(name="Backup", burst_time=5, user_id="User_B")
        p3 = Process(name="DB_Query", burst_time=3, user_id="User_A")
        p4 = Process(name="Log_Analyzer", burst_time=4, user_id="User_B")
        p5 = Process(name="Cache_Clean", burst_time=2, user_id="User_A")
        
        processes = [p1, p2, p3, p4, p5]
        scenario_name = "Carga Mixta"
    
    for p in processes:
        kernel.add_process(p)
    
    return kernel, dispatcher, processes, scenario_name


# ═════════════════════════════════════════════════════════════════════════════
# proceso personalizado xd
# ═════════════════════════════════════════════════════════════════════════════

def create_custom_processes():
    Style.print_subheader("Crear Procesos Personalizados")
    
    processes = []
    process_id = 1
    
    print(f"{Colors.CYAN}Ingresa los datos de cada proceso.{Colors.RESET}")
    print(f"{Colors.YELLOW}Presiona ENTER en nombre vacío para terminar.{Colors.RESET}\n")
    
    while True:
        name = input(f"  Proceso #{process_id} - Nombre: ").strip()
        
        if not name:
            if process_id > 1:
                break
            else:
                Style.print_warning("Debes crear al menos un proceso.")
                continue
        
        while True:
            try:
                burst = int(input(f"  Tiempo de ráfaga (CPU Burst) para '{name}': "))
                if burst <= 0:
                    Style.print_error("El tiempo debe ser mayor a 0.")
                    continue
                break
            except ValueError:
                Style.print_error("Por favor ingresa un número válido.")
        
        print(f"\n  {Colors.CYAN}Tipos de proceso:{Colors.RESET}")
        print(f"    {Colors.RED}[1]{Colors.RESET} Tiempo Real (Crítico) - Prioridad máxima")
        print(f"    {Colors.BLUE}[2]{Colors.RESET} Usuario A - Grupo de usuario")
        print(f"    {Colors.GREEN}[3]{Colors.RESET} Usuario B - Grupo de usuario")
        
        while True:
            try:
                tipo = input("  Selecciona tipo [1-3]: ").strip()
                if tipo not in ['1', '2', '3']:
                    Style.print_error("Opción inválida. Selecciona 1, 2 o 3.")
                    continue
                break
            except ValueError:
                pass
        
        if tipo == '1':
            while True:
                try:
                    priority = int(input("  Prioridad RT (0-9, 0=máx): "))
                    if priority < 0 or priority > 9:
                        Style.print_error("La prioridad debe estar entre 0 y 9.")
                        continue
                    break
                except ValueError:
                    Style.print_error("Por favor ingresa un número válido.")
            
            p = Process(name=name, burst_time=burst, priority=priority)
            
        elif tipo == '2':
            p = Process(name=name, burst_time=burst, priority=20, user_id="User_A")
            
        else:
            p = Process(name=name, burst_time=burst, priority=20, user_id="User_B")
        
        processes.append(p)
        
        Style.print_success(f"Proceso '{name}' creado exitosamente!")
        print()
        
        process_id += 1
    
    return processes


# ═════════════════════════════════════════════════════════════════════════════
# simulación y métricas finales xd
# ═════════════════════════════════════════════════════════════════════════════

def run_simulation(kernel, dispatcher, processes, scenario_name, auto_rt=False, rt_time=None):
    
    Style.print_subheader(f"Ejecutando: {scenario_name}")
    
    print(f"\n{Colors.BOLD}Lista de procesos inicial:{Colors.RESET}")
    print(f"  {'Tipo':<8} │ {'Nombre':<20} │ {'PID':<8} │ {'Estado':<10} │ {'Burst':<6}")
    print(f"  {'─' * 6} │ {'─' * 18} │ {'─' * 6} │ {'─' * 8} │ {'─' * 4}")
    
    for p in processes:
        Style.print_process_status(p)
    
    print(f"\n{Colors.YELLOW}▶ Presiona ENTER para comenzar la ejecución...{Colors.RESET}")
    input()
    

    t = 0
    max_time = 100  
    
    print(f"\n{Colors.BOLD}{'─' * 70}")
    print(f"  {'TIEMPO':<8} │ {'PROCESO':<20} │ {'ESTADO':<12} │ {'RESTANTE'}")
    print(f"{'─' * 70}{Colors.RESET}\n")
    
    running_process = None
    
    while t < max_time:
        pending = [p for p in processes if p.status != "TERMINATED"]
        if not pending:
            print(f"\n{Colors.LIGHT_GREEN}{Colors.BOLD}✓ ✓ ✓ TODOS LOS PROCESOS HAN TERMINADO ✓ ✓ ✓{Colors.RESET}\n")
            break
        
 
        if auto_rt and t == rt_time:
            rt_process = Process(name="SENSOR_INCENDIO", burst_time=2, priority=0)
            kernel.add_process(rt_process)
            processes.append(rt_process)
            print(f"  {Colors.RED}{Colors.BOLD} EVENTO EXTERNO: Proceso RT detectado! {Colors.RESET}")
        
        next_p = dispatcher.kernel.select_next_process()
        
        if next_p:
            if running_process and running_process.remaining_time > 0:
                running_process.status = "READY"
            
            running_process = next_p
            running_process.status = "RUNNING"
            
            print(f"  {Colors.CYAN}{t:>4}s{Colors.RESET} │ "
                  f"{Colors.YELLOW}{next_p.name:<20}{Colors.RESET} │ "
                  f"{Colors.LIGHT_GREEN}EJECUTANDO{Colors.RESET} │ "
                  f"{next_p.remaining_time}s")
        
        if running_process:
            dispatcher.kernel.tick()
            dispatcher.total_execution_time += 1
            running_process.remaining_time -= 1
            
            if running_process.remaining_time <= 0:
                running_process.status = "TERMINATED"
                running_process.completion_time = t + 1
                print(f"  {Colors.CYAN}{t+1:>4}s{Colors.RESET} │ "
                      f"{Colors.DIM}{running_process.name:<20}{Colors.RESET} │ "
                      f"{Colors.RED}TERMINADO{Colors.RESET} │ "
                      f"✓")
                running_process = None
        else:
            print(f"  {Colors.CYAN}{t:>4}s{Colors.RESET} │ "
                  f"{Colors.DIM}{'IDLE (Inactivo)':<20}{Colors.RESET} │ "
                  f"{Colors.YELLOW}ESPERANDO{Colors.RESET} │ "
                  f"-")
            dispatcher.total_execution_time += 1
        
        t += 1
        

        time.sleep(0.3)
    
    print_final_metrics(processes)


def print_final_metrics(processes):
    Style.print_subheader("Métricas Finales")
    
    total_wait = 0
    total_turnaround = 0
    rt_count = 0
    user_count = 0
    
    print(f"\n{Colors.BOLD}{'PROCESO':<18} │ {'TIPO':<10} │ {'ESPERA':<8} │ {'TURNAROUND':<10} │ {'ESTADO'}")
    print(f"{'─' * 16} │ {'─' * 8} │ {'─' * 6} │ {'─' * 8} │ {'─' * 8}")
    
    for p in processes:
        turnaround = p.completion_time - p.arrival_time
        waiting = turnaround - p.burst_time
        
        total_wait += waiting
        total_turnaround += turnaround
        
        if p.priority < 10:
            type_str = f"{Colors.RED}RT{Colors.RESET}"
            type_label = "RT"
            rt_count += 1
        else:
            type_str = f"{Colors.BLUE}{p.user_id}{Colors.RESET}"
            type_label = p.user_id
            user_count += 1
        
        status_str = f"{Colors.LIGHT_GREEN}✓{Colors.RESET}" if p.status == "TERMINATED" else f"{Colors.RED}✗{Colors.RESET}"
        
        print(f"  {Colors.WHITE}{p.name:<16}{Colors.RESET} │ "
              f"{type_str:<10} │ "
              f"{Colors.YELLOW}{waiting:>4}s{Colors.RESET}   │ "
              f"{Colors.CYAN}{turnaround:>6}s{Colors.RESET}   │ "
              f"{status_str}")
    
    n = len(processes)
    avg_wait = total_wait / n if n > 0 else 0
    avg_turnaround = total_turnaround / n if n > 0 else 0
    
    print(f"\n{Colors.BOLD}{'─' * 60}{Colors.RESET}")
    print(f"  {Colors.WHITE}Total de procesos:{Colors.RESET} {n} ({Colors.RED}RT: {rt_count}{Colors.RESET}, "
          f"{Colors.BLUE}User: {user_count}{Colors.RESET})")
    print(f"  {Colors.WHITE}Tiempo de espera promedio:{Colors.RESET} {Colors.YELLOW}{avg_wait:.2f}s{Colors.RESET}")
    print(f"  {Colors.WHITE}Tiempo de turnaround promedio:{Colors.RESET} {Colors.CYAN}{avg_turnaround:.2f}s{Colors.RESET}")
    print(f"  {Colors.WHITE}Tiempo total de CPU:{Colors.RESET} {n * 3}s (estimado)")
    print(f"{Colors.BOLD}{'─' * 60}{Colors.RESET}\n")


# ═════════════════════════════════════════════════════════════════════════════
# menu principal 
# ═════════════════════════════════════════════════════════════════════════════

def print_welcome():
    print(Colors.CYAN + BANNER + Colors.RESET)


def main_menu():
    while True:
        print_welcome()
        
        options = {
            "1": "Ejecutar escenario DEMO 1: Básico (RT + Fair-Share)",
            "2": "Ejecutar escenario DEMO 2: Stress Test (Fair-Share vs Monopolio)",
            "3": "Ejecutar escenario DEMO 3: Prioridad Tiempo Real",
            "4": "Ejecutar escenario DEMO 4: Carga Mixta",
            "5": "Crear configuración PERSONALIZADA",
            "6": "Ver información del sistema",
            "0": "Salir del programa"
        }
        
        Style.print_menu(options, "SISTEMA DE PLANIFICACIÓN HÍBRIDA")
        
        choice = input(f"{Colors.CYAN}Selecciona una opción: {Colors.RESET}").strip()
        
        if choice == "0":
            print_goodbye()
            break
        
        elif choice == "1":
            run_demo_scenario(1)
        
        elif choice == "2":
            run_demo_scenario(2)
        
        elif choice == "3":
            run_demo_scenario(3)
        
        elif choice == "4":
            run_demo_scenario(4)
        
        elif choice == "5":
            run_custom_scenario()
        
        elif choice == "6":
            show_system_info()
        
        else:
            Style.print_error("Opción inválida. Por favor selecciona 0-6.")
            time.sleep(1)


def run_demo_scenario(scenario_id):
    Style.clear_screen()
    Style.print_header(f"ESCENARIO DEMO #{scenario_id}")
    
    kernel, dispatcher, processes, scenario_name = create_demo_scenario(scenario_id)
    

    print(f"\n{Colors.CYAN}¿Deseas inyectar un proceso de Tiempo Real durante la ejecución?{Colors.RESET}")
    print(f"  {Colors.GREEN}[S]{Colors.RESET}  Sí, en el segundo 3 (simulación de sensor)")
    print(f"  {Colors.RED}[N]{Colors.RESET}  No, ejecutar normal")
    
    auto_rt = False
    rt_time = 3
    
    while True:
        resp = input(f"\n{Colors.YELLOW}Opción [S/N]: {Colors.RESET}").strip().upper()
        if resp == 'S':
            auto_rt = True
            break
        elif resp == 'N':
            auto_rt = False
            break
        else:
            Style.print_error("Opción inválida.")
    
    run_simulation(kernel, dispatcher, processes, scenario_name, auto_rt, rt_time)
    
    print(f"\n{Colors.YELLOW}Presiona ENTER para volver al menú principal...{Colors.RESET}")
    input()


def run_custom_scenario():
    Style.clear_screen()
    Style.print_header("CONFIGURACIÓN PERSONALIZADA")
    
    processes = create_custom_processes()
    
    if not processes:
        Style.print_warning("No se crearon procesos. Regresando al menú...")
        time.sleep(1)
        return
    
    kernel = Kernel()
    dispatcher = Dispatcher(kernel)
    
    for p in processes:
        kernel.add_process(p)
    
    run_simulation(kernel, dispatcher, processes, "Configuración Personalizada")
    
    print(f"\n{Colors.YELLOW}Presiona ENTER para volver al menú principal...{Colors.RESET}")
    input()


def show_system_info():
    Style.clear_screen()
    Style.print_header("INFORMACIÓN DEL SISTEMA")
    
    print(f"""
{Colors.CYAN}╔════════════════════════════════════════════════════════════════╗
║           SISTEMA DE PLANIFICACIÓN HÍBRIDA              ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  Este sistema implementa tres algoritmos de planificación:   ║
║                                                                ║
║  {Colors.RED}1. Tiempo Real (RT){Colors.CYAN}                                        ║
║     └── Prioridad máxima para procesos críticos              ║
║     └── Ejecutan inmediatamente sin espera                   ║
║     └── Ejemplo: Sensores, sistemas de emergencia             ║
║                                                                ║
║  {Colors.BLUE}2. Fair-Share (Justicia entre usuarios){Colors.CYAN}                  ║
║     └── Cada usuario recibe tiempo equitativo de CPU         ║
║     └── Previene que un usuario acapare recursos             ║
║     └── Uso: Sistemas multiusuario                           ║
║                                                                ║
║  {Colors.GREEN}3. UNIX Tradicional{Colors.CYAN}                                       ║
║     └── Prioridad dinámica basada en uso de CPU             ║
║     └── Retroalimentación: procesos largos bajan prioridad  ║
║     └── Compatible con sistemas clásicos                    ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
{Colors.RESET}
""")
    
    print(f"{Colors.YELLOW}Presiona ENTER para volver al menú principal...{Colors.RESET}")
    input()


def print_goodbye():
    Style.clear_screen()
    print(f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║     ██████╗ ██████╗ ███████╗    ██████╗ ██╗   ██╗ █████╗ ███╗   ██╗      ║
║     ██╔══██╗██╔══██╗██╔════╝   ██╔═══██╗██║   ██║██╔══██╗████╗  ██║      ║
║     ██████╔╝██████╔╝█████╗     ██║   ██║██║   ██║███████║██╔██╗ ██║      ║
║     ██╔═══╝ ██╔══██╗██╔══╝     ██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║      ║
║     ██║     ██║  ██║███████╗   ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║      ║
║     ╚═╝     ╚═╝  ╚═╝╚══════╝    ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝      ║
║                                                                          ║
║            ¡GRACIAS POR USAR EL SIMULADOR DE PLANIFICACIÓN!              ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}
    """)


# ═════════════════════════════════════════════════════════════════════════════
# punto de entrada del programa xdd
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    try:
        Style.print_banner()
        
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Programa interrumpido por el usuario.{Colors.RESET}")
        print_goodbye()
        sys.exit(0)

