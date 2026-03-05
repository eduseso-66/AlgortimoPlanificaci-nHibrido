# 📁 Algoritmo de Planificación de Procesos : RT + Fair-Share + UNIX

En este repositorio se aplican 3 diferentes tipos de algoritmos de planificacion, además se incluye un simulador en terminal para probar cada uno de ellos, además se implemento un algoritmo hibrido que implementa todos juntos simuladon procesos y funcionalidades como paginación.
Este proyecto implementa un Planificador de Procesos Híbrido de última generación. 
No es solo un algoritmo aislado; es un Kernel jerárquico que integra cuatro lógicas de planificación que conviven en sistemas operativos modernos como Linux y Windows.



## PROYECTO ESCOLAR 
Proyecto escolar creado con la finalidad de simular algoritmos de planificación de proceso, se adjuntara un archivo docx incluyendo la documentación completa de la creación de este proyecto. El proyecto fue construido solo en python, pero se espera una futura implementacion en lenguaje C.
Evidentemente este proyecto incluye algunos fallos que serán corregidos en un futuro, así como también se aceptan sugerencias de mejora a este pequeño proyecto escolar.



#  Características del algoritmo

El algoritmo unifica los siguientes paradigmas en una sola estructura de datos modular:

    Capa 0: Hard Real-Time (RT) - Prioridad absoluta para procesos críticos (Sensores, Emergencias).

    Capa 1: Fair-Share Scheduling - Distribución equitativa de CPU basada en grupos de usuarios, evitando la monopolización de recursos.

    Capa 2: UNIX Traditional (Feedback) - Uso de valores Nice y penalizaciones dinámicas para procesos intensivos en CPU.

    Capa 3: Round Robin (RR) - Gestión de ráfagas de tiempo (Quantums) para interactividad.

# Como usarlo e instalarlo

## Clonar el repositorio
```bash
git clone https://github.com/eduseso-66/AlgortimoPlanificaci-nHibrido.git
cd AlgoritmoPlanificaci-nHibrido
```
## Instalar dependencias necesarias
```bash
pip install -r requirements.txt
```
## Ejecutar el simulador
```bash
python main.py
```
    
### IMPORTANTE
Es de crucial importancia mencionar que, para evitar problemas se recomienda crear un entorno virtual en Python para evitar fallas (si se presentan).
```bash
python -m venv env

```
Una vez creado, el entorno virtual debe activarse vía alguno de los siguientes comandos.

En Windows:
```bash
env\Scripts\activate
```
En Linux/MacOS
```bash
source env/bin/activate
```
Para desactivar el entorno virtual se usa el comando:
deactivate


### 👥 Integrantes y participantes de la creación de este proyecto
Alexander Martines Aguilar y
José Eduardo Pérez Córdova


![animation](https://media.tenor.com/USfkXRl1-a0AAAAi/ratzombien.gif)











