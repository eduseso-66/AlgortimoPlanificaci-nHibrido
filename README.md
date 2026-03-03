# 📁 Hybrid scheduling algorithm : RT + Fair-Share + UNIX

Este proyecto implementa un Planificador de Procesos Híbrido de última generación. 
No es solo un algoritmo aislado; es un Kernel jerárquico que integra cuatro lógicas de planificación que conviven en sistemas operativos modernos como Linux y Windows.

# 🚀 Características Principales

El algoritmo unifica los siguientes paradigmas en una sola estructura de datos modular:

    Capa 0: Hard Real-Time (RT) - Prioridad absoluta para procesos críticos (Sensores, Emergencias).

    Capa 1: Fair-Share Scheduling - Distribución equitativa de CPU basada en grupos de usuarios, evitando la monopolización de recursos.

    Capa 2: UNIX Traditional (Feedback) - Uso de valores Nice y penalizaciones dinámicas para procesos intensivos en CPU.

    Capa 3: Round Robin (RR) - Gestión de ráfagas de tiempo (Quantums) para interactividad.




