# grsim-pria

## Essencial: 

```bash
sudo apt install python -y
sudo apt install python3-pip -y
sudo apt install git -y
```

## Passo 1: Instalação do ROS no Ubuntu 20.04

Tutorial em [português (PT-BR)](https://github.com/russibc/grsim-pria/blob/main/INSTALL-ROS-PT.md) ou [español (ES)](https://github.com/russibc/grsim-pria/blob/main/INSTALL-ROS-ES.md).

## Passo 2: Criar diretório 

```bash
mkdir test_ssl
cd test_ssl
mkdir src
cd src
```
## Passo 3: Inicializar workspace
```bash
source /opt/ros/noetic/setup.bash
catkin_init_workspace
```
## Passo 4: Instalação e configuração do GrSim

Tutorial disponível [aqui](https://github.com/RoboCup-SSL/grSim/blob/master/INSTALL.md).

## Passo 5: Clonar repositórios dentro da pasta `src` do diretório `test_ssl`

```bash
git clone https://github.com/Los-UruBots-del-Norte/vision_comm.git
git clone https://github.com/Los-UruBots-del-Norte/grsim_ros_bridge_msgs.git
git clone https://github.com/Los-UruBots-del-Norte/grsim_ros_bridge.git
git clone https://github.com/KRSSG/krssg_ssl_msgs.git
```
Ao final se deve ter cinco diretórios dentro de `/test_ssl/src`: o `grSim` e os quatro repositórios clonados acima.

## Passo 6: Mudar o caminho do GrSim no arquivo `run_grsim.py`

Deve ser colocado o caminho completo do arquivo GrSim dentro da pasta GrSim/bin, exemplo:

```bash
/home/SEU_USUARIO_AQUI/grsim-pria-ws/src/grSim/bin/grSim
```

Use o caminho completo gerado em:
```bash
echo $PWD
```

## Passo 7: Instalar dependências python no grsim_ros_bridge

Além disso se deve entrar em `grsim_ros_bridge` e executar

```bash
cd ssl-python-clients
pip install .
```
## Passo 8: Executar GrSim e Modificar parâmetros pela interface gráfica da execução

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

E, por fim, reposicionar os jogadores fora do campo de modo que se pareça como na imagem abaixo:

![Board](https://github.com/russibc/grsim-pria/blob/main/board.png)

## Passo 9: Fechar GrSim e Configurar workspace

Volte ao diretório `test_ssl` e execute:

```bash
source /opt/ros/noetic/setup.bash
catkin_make
```
```bash
source devel/setup.bash
roscd grsim_ros_bridge
```
O comando acima levará à pasta grsim_ros_bridge. Volte à pasta `test_ssl` e execute finalmente:
```bash
roslaunch grsim_ros_bridge launch.launch
```

Em outro terminal (pasta `grsim-pria-ws/src`), faça:
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
Em `grsim-pria/scripts` cole o arquivo `game.py` e forneça permissão:
```bash
chmod +x game.py
```

Em seguida retorne ao diretório principal e recompile: 
```bash
source /opt/ros/noetic/setup.bash
source devel/setup.bash
catkin_make
```
Para executar, finalmente:
```bash
rosrun grsim-pria game.py
```
