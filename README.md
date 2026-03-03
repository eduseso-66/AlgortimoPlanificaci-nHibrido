# 📁 Algoritmo de Planificación de Procesos : RT + Fair-Share + UNIX

Este proyecto implementa un Planificador de Procesos Híbrido de última generación. 
No es solo un algoritmo aislado; es un Kernel jerárquico que integra cuatro lógicas de planificación que conviven en sistemas operativos modernos como Linux y Windows.

## PROYECTO ESCOLAR ⚠️
Proyecto escolar creado con la finalidad de simular algoritmos de planificación de proceso, se adjuntara un archivo docx incluyendo la documentación completa de la creación de este proyecto. El proyecto fue construido solo en python, pero se espera una futura implementacion en lenguaje C.
Evidentemente este proyecto incluye algunos fallos que serán corregidos en un futuro, así como también se aceptan sugerencias de mejora a este pequeño proyecto escolar.



# 🚀 Características Principales

El algoritmo unifica los siguientes paradigmas en una sola estructura de datos modular:

    Capa 0: Hard Real-Time (RT) - Prioridad absoluta para procesos críticos (Sensores, Emergencias).

    Capa 1: Fair-Share Scheduling - Distribución equitativa de CPU basada en grupos de usuarios, evitando la monopolización de recursos.

    Capa 2: UNIX Traditional (Feedback) - Uso de valores Nice y penalizaciones dinámicas para procesos intensivos en CPU.

    Capa 3: Round Robin (RR) - Gestión de ráfagas de tiempo (Quantums) para interactividad.

# 💻 Instalación y Uso

## Clonar el repositorio
```bash
git clone https://github.com/eduseso-66/AlgortimoPlanificaci-nHibrido.git
cd Algoritmo-Planificaci-nHibrido
```
## Instalar dependencias necesarias
```bash
pip install -r requirements.txt
```
## Ejecutar el simulador
```bash
python main.py
```
### 🛠️ Próximos Pasos (Roadmap)

    [ ] Implementar gestión de estados de Bloqueo (I/O Wait).

    [ ] Añadir visualización de Diagramas de Gantt en tiempo real.

    [x] Migración a C: Traducción de la lógica de punteros y estructuras a nivel de Kernel real.

### 👥 Integrantes y participantes de la creación de este proyecto
Alexander Martines Aguilar
José Eduardo Pérez Córdova






