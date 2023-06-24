# Trabajo final: grsim-pria

**Estudiantes:**
Bruna C. Russi & Eduardo G. S. Barreto

## Esencial: 

```bash
sudo apt install python -y
sudo apt install python3-pip -y
sudo apt install git -y
```

## Paso 1: Instalación de ROS en Ubuntu 20.04

Tutorial en [portugués (PT-BR)](https://github.com/russibc/grsim-pria/blob/main/INSTALL-ROS-PT.md) o [español (ES)](https://github.com/russibc/grsim-pria/blob/main/INSTALL-ROS-ES.md).

## Paso 2: Crear directorio 

```bash
mkdir grsim-pria-ws
cd grsim-pria-ws
mkdir src
cd src
```
## Paso 3: Inicializar workspace
```bash
source /opt/ros/noetic/setup.bash
catkin_init_workspace
```
## Paso 4: Instalación y configuración de GrSim

Tutorial disponible [aquí](https://github.com/RoboCup-SSL/grSim/blob/master/INSTALL.md).

## Paso 5: Clonar repositorios dentro de la carpeta `src` del directorio `grsim-pria-ws`

```bash
git clone https://github.com/Los-UruBots-del-Norte/vision_comm.git
git clone https://github.com/Los-UruBots-del-Norte/grsim_ros_bridge_msgs.git
git clone https://github.com/Los-UruBots-del-Norte/grsim_ros_bridge.git
git clone https://github.com/KRSSG/krssg_ssl_msgs.git
```
Al final deberías tener cinco directorios dentro de `/grsim-pria-ws/src`: `grSim` y los cuatro repositorios clonados mencionados anteriormente.

## Paso 6: Cambiar la ruta de GrSim en el archivo `run_grsim.py`

Debes colocar la ruta completa del archivo GrSim dentro de la carpeta GrSim/bin, por ejemplo:

```bash
/home/TU_USUARIO_AQUÍ/grsim-pria-ws/src/grSim/bin/grSim
```

Usa la siguiente ruta completa generada por:
```bash
echo $PWD
```

## Paso 7: Instalar dependencias de Python en grsim_ros_bridge

Además, debes ingresar a `grsim_ros_bridge` y ejecutar

```bash
cd ssl-python-clients
pip install .
```
## Paso 8: Ejecutar GrSim y modificar parámetros a través de la interfaz gráfica de ejecución

```bash
cd /grSim/bin
./grSim
```

Game > Division B

Game > Robots Count: 5

Field > Division A > width: 4

Field > Division A > length: 4

Field > Division B > width: 4

Field > Division B > length: 4

Y finalmente, reposicionar los jugadores fuera del campo para que se vea como en la siguiente imagen:

![Board](https://github.com/russibc/grsim-pria/blob/main/board.png)

## Paso 9: Cerrar GrSim y configurar el *workspace*

Regresa al directorio `grsim-pria-ws` y ejecuta:

```bash
source /opt/ros/noetic/setup.bash
catkin_make
```
```bash
source devel/setup.bash
roscd grsim_ros_bridge
```
El comando anterior te llevará a la carpeta grsim

_ros_bridge. Regresa a la carpeta `grsim-pria-ws` y finalmente ejecuta:
```bash
roslaunch grsim_ros_bridge launch.launch
```

En otra terminal (en la carpeta `grsim-pria-ws/src`), haz lo siguiente:
```bash
source /opt/ros/noetic/setup.bash
```
```bash
catkin_create_pkg grsim-pria grsim_ros_bridge_msgs rospy roscpp geometry_msgs std_msgs
```
```bash
cd grsim-pria
mkdir scripts
cd scripts
```
En `grsim-pria/scripts`, pega el archivo `game.py` y otorga permisos:
```bash
chmod +x game.py
```

Luego regresa al directorio principal `grsim-pria-ws` y recompila: 
```bash
source /opt/ros/noetic/setup.bash
source devel/setup.bash
catkin_make
```
Para finalmente ejecutar:
```bash
rosrun grsim-pria game.py
```
**NOTA: El código solo funciona si los jugadores están posicionados dentro del cuadrante.**
