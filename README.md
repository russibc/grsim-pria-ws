# grsim-pria

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
catkin_init_workspace
```
## Passo 4: Instalação e configuração do GrSim

Tutorial disponível [aqui](https://github.com/RoboCup-SSL/grSim/blob/master/INSTALL.md).

## Passo 5: Clonar repositórios dentro da pasta `src` do diretório `test_ssl`

```bash
git clone git@github.com:Los-UruBots-del-Norte/vision_comm.git
git clone ggit@github.com:Los-UruBots-del-Norte/grsim_ros_bridge_msgs.git
git clone git@github.com:Los-UruBots-del-Norte/grsim_ros_bridge.git
git clone git@github.com:KRSSG/krssg_ssl_msgs.git
```
Ao final se deve ter cinco diretórios dentro de `/test_ssl/src`: o `grSim` e os quatro repositórios clonados acima.
