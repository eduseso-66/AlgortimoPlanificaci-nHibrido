<h1 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=30&pause=1000&color=F72929&center=true&vCenter=true&width=800&height=70&lines=Algoritmo+Planificador+de+Procesos+H%C3%ADbrido;RT+%2B+Fair-Share+%2B+UNIX+%2B+RR;Kernel+Jer%C3%A1rquico+Simulado">
</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/OS-Linux%20%2F%20Windows-white?style=for-the-badge&logo=linux" />
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" />
</div>

<br>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXF4Znd4Znd4Znd4Znd4Znd4Znd4Znd4Znd4Znd4Znd4Znd4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKSjPqcKInwLcmk/giphy.gif" width="400">
</p>

# PROYECTO
Este repositorio implementa un **Planificador de Procesos Híbrido de última generación**. No es solo un algoritmo aislado; es un Kernel jerárquico que integra cuatro lógicas de planificación que conviven en sistemas operativos modernos.

> [!IMPORTANT]
> **Proyecto Escolar:** Creado para simular la gestión de recursos de CPU. Incluye documentación detallada en formato `.docx` dentro del repositorio.



# 🧠 Arquitectura del Algoritmo
El sistema unifica los siguientes paradigmas en una estructura de datos modular de 4 capas:

| Capa | Algoritmo | Propósito |
| :--- | :--- | :--- |
| **Capa 0** | **Hard Real-Time (RT)** | Prioridad absoluta para procesos críticos (Sensores, Emergencias). |
| **Capa 1** | **Fair-Share** | Distribución equitativa por grupos de usuarios. |
| **Capa 2** | **UNIX Feedback** | Uso de valores *Nice* y penalizaciones dinámicas. |
| **Capa 3** | **Round Robin (RR)** | Gestión de ráfagas de tiempo (Quantums) para interactividad. |



# 🛠️ Tecnologías Utilizadas
<div align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" />
  <img src="https://img.shields.io/badge/Shell_Script-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" />
</div>


### Diagrama de Flujo de Datos

```mermaid
flowchart TB
    subgraph Entrada["📝 Entrada de Usuario"]
        A[Procesos Personalizados<br/>o Escenarios Demo]
    end

    subgraph Kernel["⚙️ Kernel - Orquestador Híbrido"]
        B[Cola de Procesos RT<br/>priority < 10]
        C[Grupos de Usuarios<br/>Fair-Share]
        D[Scheduler UNIX<br/>Prioridad Dinámica]
    end

    subgraph Schedulers["🔧 Schedulers Especializados"]
        E[RealTimeScheduler<br/>get_next]
        F[FairShareScheduler<br/>select_user_group]
        G[UnixScheduler<br/>sort_by_unix_priority]
    end

    subgraph Ejecucion["▶️ Ejecución"]
        H[Dispatcher<br/>context_switch]
        I[CPU Simulation<br/>tick]
    end

    subgraph Salida["📊 Salida"]
        J[Métricas Finales<br/>Waiting / Turnaround]
    end

    A -->|add_process| B
    A -->|add_process| C
    
    B -->|RT primero| E
    C -->|Usuario con menor vruntime| F
    F -->|Procesos del usuario| D
    D -->|Ordenar por prioridad UNIX| G
    
    E -->|next_p| H
    G -->|chosen| H
    
    H -->|Ejecutar| I
    I -->|tick| I
    I -->|Terminado| J
    I -->|Pendientes| B
    I -->|Pendientes| C
```

### Diagrama de Clases

```mermaid
classDiagram
    class Process {
        +str pid
        +str name
        +str status
        +int burst_time
        +int remaining_time
        +int priority
        +str user_id
        +float vruntime
        +int nice
        +int completion_time
        +update_vruntime(delta, weight)
    }

    class Kernel {
        +list rt_queue
        +dict user_groups
        +Process running_process
        +int clock
        +add_process(process)
        +select_next_process()
        +tick()
    }

    class Dispatcher {
        +Kernel kernel
        +int total_execution_time
        +context_switch(new_process)
        +run_step()
    }

    class RealTimeScheduler {
        +get_next(queue)$
    }

    class FairShareScheduler {
        +select_user_group(user_groups)$
    }

    class UnixScheduler {
        +adjust_priority(process)$
        +sort_by_unix_priority(process_list)$
    }

    class Metrics {
        +calculate_metrics(process_list)$
    }

    Kernel --> Process : manages
    Dispatcher --> Kernel : controls
    Kernel --> RealTimeScheduler : uses
    Kernel --> FairShareScheduler : uses
    Kernel --> UnixScheduler : uses
    Metrics --> Process : analyzes
```




# 🚀 Metodo de instalacion y uso

## Prerrequisitos
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### 1. Clonar el repositorio
```
git clone https://github.com/eduseso-66/AlgortimoPlanificaci-nHibrido.git
cd AlgoritmoPlanificaci-nHibrido
```
### 2. Instalar las dependencias necesarias
```
pip install -r requirements.txt
```
### 3. Iniciar el simulador
```
python main.py
```
# Recomendacion
Es de crucial importancia mencionar que, para evitar problemas recomendamos crear un entorno virtual en Python para evitar fallas (si se presentan).
```
python -m venv env
```
Una vez creado el entorno virtual debe activarse usando los siguientes comandos.
En Windows:
```
env\Scripts\activate
```
En MacOS/Linux:
```
source env/bin/activate
```
Para desactivar el entorno virtual se usa el siguiente comando:
```
deactivate
```
## Integrantes y participantes de la creación de este proyecto
<h2 align = "center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=30&pause=1000&color=27F7E3&center=true&vCenter=true&width=800&height=80&lines=Jos&eacute+Eduardo+Perez+Cordova;Alexander+Martines+Aguilar">
</h2>

## 👨‍💻 Autores

**eduseso-66**

- GitHub: [@eduseso-66](https://github.com/eduseso-66)
- Repositorio: [AlgortimoPlanificaci-nHibrido](https://github.com/eduseso-66/AlgortimoPlanificaci-nHibrido.git)



## 🙏 Agradecimientos

- Inspirado en los algoritmos de planificación de Linux (CFS) y UNIX
- Documentación de [SimPy](https://simpy.readthedocs.io/) para simulación de eventos
- Comunidad de Python por las herramientas y librerías



<p align="center">
  <b>⭐ ¡Si este proyecto te fue útil, dale una estrella! ⭐</b>
</p>


![animation](https://media.tenor.com/USfkXRl1-a0AAAAj/ratzombien.gif)














