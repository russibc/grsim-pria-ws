Este archivo README proporciona instrucciones paso a paso sobre cómo instalar ROS (Robot Operating System) en un sistema operativo Ubuntu 20.04.

### Paso 1: Configuración de los repositorios

Abra la terminal y ejecute los siguientes comandos para configurar los repositorios de ROS:

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

### Paso 2: Instalación de Curl (si aún no está instalado)

Si el comando `curl` no está instalado en su sistema, ejecute el siguiente comando:

```bash
sudo apt install curl
```

### Paso 3: Agregar la clave de autenticación

Ejecute el siguiente comando para agregar la clave de autenticación:

```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

### Paso 4: Actualización de los paquetes

Ejecute el siguiente comando para actualizar la lista de paquetes disponibles:

```bash
sudo apt update -y
```

### Paso 5: Instalación de ROS

Para instalar la versión completa de ROS Noetic, ejecute el siguiente comando:

```bash
sudo apt install ros-noetic-desktop-full -y
```

### Paso 6: Configuración del entorno de ROS

Configure el entorno de ROS ejecutando los siguientes comandos:

```bash
source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### Paso 7: Instalación de dependencias adicionales

Instale las dependencias adicionales de ROS ejecutando los siguientes comandos:

```bash
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential -y
sudo apt install python3-rosdep -y
```

### Paso 8: Inicialización de rosdep

Ejecute los siguientes comandos para inicializar y actualizar rosdep:

```bash
sudo rosdep init
rosdep update
```
