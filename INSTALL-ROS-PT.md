Este arquivo README fornece instruções passo a passo sobre como instalar o ROS (Robot Operating System) em um sistema operacional Ubuntu 20.04.

#### Passo 1: Configurando os repositórios

Abra o terminal e execute os seguintes comandos para configurar os repositórios do ROS:

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

#### Passo 2: Instalando o Curl (caso ainda não esteja instalado)

Se o comando `curl` ainda não estiver instalado no seu sistema, execute o seguinte comando:

```bash
sudo apt install curl -y
```

#### Passo 3: Adicionando a chave de autenticação

Execute o seguinte comando para adicionar a chave de autenticação:

```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

#### Passo 4: Atualizando os pacotes

Execute o comando a seguir para atualizar a lista de pacotes disponíveis:

```bash
sudo apt update -y
```

#### Passo 5: Instalando o ROS

Para instalar a versão completa do ROS Noetic, execute o seguinte comando:

```bash
sudo apt install ros-noetic-desktop-full -y
```

#### Passo 6: Configurando o ambiente do ROS

Configure o ambiente do ROS executando os seguintes comandos:

```bash
source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

#### Passo 7: Instalando dependências adicionais

Instale as dependências adicionais do ROS executando os seguintes comandos:

```bash
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential -y
sudo apt install python3-rosdep -y
```

#### Passo 8: Inicializando o rosdep

Execute os seguintes comandos para inicializar e atualizar o rosdep:

```bash
sudo rosdep init
rosdep update
```
