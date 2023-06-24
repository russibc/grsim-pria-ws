#! /usr/bin/env python3

import numpy as np
from math import atan2
from threading import *
import rospy
from geometry_msgs.msg import *
from gazebo_msgs.msg import *
from grsim_ros_bridge_msgs.msg import *
from krssg_ssl_msgs.msg import *
import math
import random

bola = Pose()
p_bola=(0,0)
cabecalho=0

jogador_a = {
    0: SSL_DetectionRobot(),
    1: SSL_DetectionRobot(),
    2: SSL_DetectionRobot(),
    3: SSL_DetectionRobot(),
    4: SSL_DetectionRobot()
}

jogador_b = {
    0: SSL_DetectionRobot(),
    1: SSL_DetectionRobot(),
    2: SSL_DetectionRobot(),
    3: SSL_DetectionRobot(),
    4: SSL_DetectionRobot()
}

dist = { 
    0: (0,0), 
    1: (0,0),
    2: (0,0),
    3: (0,0),
    4: (0,0)
}

dist_mod = {
    0: 0, 
    1: 0,
    2: 0,
    3: 0,
    4: 0
}
    
ang = { 
    0: 0, 
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

dist_by = { #
    0: [(0,0), (0,0), (0,0), (0,0), (0,0)], 
    1: [(0,0), (0,0), (0,0), (0,0), (0,0)],
    2: [(0,0), (0,0), (0,0), (0,0), (0,0)],
    3: [(0,0), (0,0), (0,0), (0,0), (0,0)],
    4: [(0,0), (0,0), (0,0), (0,0), (0,0)]
}

min_dist = { 
    0: 0, 
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

min_vec_dist ={ 
    0: (0,0), 
    1: (0,0),
    2: (0,0),
    3: (0,0),
    4: (0,0)
}

ang_arc = { 
    0: 0, 
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

ssl_msg = {
        0:SSL(),
        1:SSL(),
        2:SSL(),
        3:SSL(),
        4:SSL()
    }


def definir_dados(dados): 
                
    for i in range(0, len(dados.robots_blue)):
        id_robots = dados.robots_blue[i].robot_id
        if id_robots == 0:
            jogador_a[0] = dados.robots_blue[i]
        if id_robots == 1:
            jogador_a[1] = dados.robots_blue[i]
        if id_robots == 2:
            jogador_a[2] = dados.robots_blue[i]
        if id_robots == 3:
            jogador_a[3] = dados.robots_blue[i]
        if id_robots == 4:
            jogador_a[4] = dados.robots_blue[i]

    for i in range(0, len(dados.robots_yellow)):
        id_robotsy = dados.robots_yellow[i].robot_id
        if id_robotsy == 0:
            jogador_b[0] = dados.robots_yellow[i]
        if id_robotsy == 1:
            jogador_b[1] = dados.robots_yellow[i]
        if id_robotsy == 2:
            jogador_b[2] = dados.robots_yellow[i]
        if id_robotsy == 3:
            jogador_b[3] = dados.robots_yellow[i]
        if id_robotsy == 4:
            jogador_b[4] = dados.robots_yellow[i]
    
    global bola		
    bola = dados.balls

def salvar_bola():

    global p_bola

    try: 
        p_bola=((bola[0].x),(bola[0].y))
        dist_angle(p_bola[0], p_bola[1]) 
        return (p_bola)

    except: 
        pass


def verifica_area(positionX, positionY): 
    if positionX > -2000 and positionX < 0:
        if positionY > -2000 and positionY < 2000:
            return True
        else:
            return False
    else:
        return False

def campo(positionX, positionY): 
    if positionX > -2000 and positionX < 2000:
        if positionY > -2000 and positionY < 2000:
            return True
        else:
            return False
    else:
        return False

def defender_pos(positionX, positionY):
    if positionX > -2000 and positionX < 0:
        if positionY > -2000 and positionY < 2000:
            return True
        else:
            return False
    else:
        return False


def dist_angle(ball_x, ball_y): 

    for i in range (0,5):
        dist[i]= (ball_x-jogador_a[i].x,ball_y-jogador_a[i].y) 
        dist_mod[i]= math.sqrt((ball_x-jogador_a[i].x)**2+(ball_y-jogador_a[i].y)**2) 
        ang[i]= math.atan2(dist[i][1], dist[i][0]) 

def distancia_jogadores(): 

    for i in range (0,5):
        for j in range (0,5):
            dist_by[i]=math.sqrt((jogador_b[j].x-jogador_a[i].x)**2 + (jogador_b[j].y-jogador_a[i].y)**2)

def arc_jogadores(robotIndex): 

    global dist_arc_robot
    global ang_v2,ang_v1
    global ang_min

    dist_arc_robot = []
    vect_arc_robot = []
    ang_arc_robot = []

    
    ang_min = 0 

    for h in range(-950,1000,50):
        dist_arc_robot.append(math.sqrt((1900-jogador_a[robotIndex].x)**2+(h-jogador_a[robotIndex].y)**2)) #modulo distancia arco-robot
        
        vect_arc_robot.append(((1900-jogador_a[robotIndex].x),(h-jogador_a[robotIndex].y))) #vector distancia arco-robot
        
        if (1900-jogador_a[robotIndex].x) != 0: 
            ang_arc_robot.append(math.atan2((h-jogador_a[robotIndex].y),(1900-jogador_a[robotIndex].x))) #angulo arco-robot
        
        else: ang_arc_robot.append(0)

    min_dist[robotIndex]=min(dist_arc_robot)


    vector_1 = vect_arc_robot[len(vect_arc_robot)-1]
    vector_2 = vect_arc_robot[0]

    ang_v1 = (math.atan2((vector_1[0]-jogador_a[robotIndex].y),(vector_1[1]-jogador_a[robotIndex].x)))
    ang_v2 = (math.atan2((vector_2[0]-jogador_a[robotIndex].y),(vector_2[1]-jogador_a[robotIndex].x)))


    if abs((h-jogador_a[robotIndex].y)) < 0.02:
        ang_arc[robotIndex] = 0

    elif abs((1900-jogador_a[robotIndex].x)) < 0.02:
        ang_arc[robotIndex] = (math.pi)/2 

    else:
        ang_arc[robotIndex] = ang_arc_robot[dist_arc_robot.index(min(dist_arc_robot))]


def detectar(robotIndex): 

    if campo(jogador_a[robotIndex].x,jogador_a[robotIndex].y) >= 1980:
        ssl_msg[robotIndex].cmd_vel.angular.z=0.0
        ssl_msg[robotIndex].cmd_vel.linear.x=-0.8
    if campo(jogador_a[robotIndex].x,jogador_a[robotIndex].y) <= -1980:
        ssl_msg[robotIndex].cmd_vel.angular.z=0.0
        ssl_msg[robotIndex].cmd_vel.linear.x=0.8
        
    pub[robotIndex].publish(ssl_msg[robotIndex])	

def atacar(robotIndex): 
    global cabecalho	

    cabecalho = ang[robotIndex] - jogador_a[robotIndex].orientation

    if cabecalho > math.pi:
        cabecalho -= 2 * math.pi

    elif cabecalho < -math.pi:
        cabecalho += 2 * math.pi

 
    if (-0.1) <= cabecalho <= (0.1): 
        ssl_msg[robotIndex].cmd_vel.angular.z=0.0
        ssl_msg[robotIndex].cmd_vel.linear.x=0.5
  
    elif cabecalho <(-0.1):
        ssl_msg[robotIndex].cmd_vel.angular.z=-1.0
        ssl_msg[robotIndex].cmd_vel.linear.x=0.0
  
    else: 
        ssl_msg[robotIndex].cmd_vel.angular.z=1.0
        ssl_msg[robotIndex].cmd_vel.linear.x=0.0

    pub[robotIndex].publish(ssl_msg[robotIndex])
 
def pegar_bola(robotIndex):
    x_diff = p_bola[0] - jogador_a[robotIndex].x
    y_diff = p_bola[1] - jogador_a[robotIndex].y
    euclides = math.sqrt((x_diff)**2 + (y_diff)**2)
    if euclides <= 5:
        return robot_arco(robotIndex)
    else:
        return atacar(robotIndex)

def robot_arco(RobotIndex):
    x_diff = p_bola[0] - jogador_a[RobotIndex].x
    y_diff = p_bola[1] - jogador_a[RobotIndex].y
    euclides = math.sqrt((x_diff)**2 + (y_diff)**2)
    
    arco_x = 2000
    arco_y = list(range(-1000,1000,50))
    
    diff_x = arco_x - jogador_a[RobotIndex].x
    diff_y = random.choice(arco_y) - jogador_a[RobotIndex].y
    
    gama = math.atan2(diff_y, diff_x)
    err_orientation = gama - jogador_a[RobotIndex].orientation

    
    if -0.1 <= err_orientation <= 0.1 and euclides <= 5:
        return chutar(RobotIndex)
    
    else: pass
        
    
def chutar(robotIndex):
    ssl_msg[robotIndex].kicker = True
     
    pub[robotIndex].publish(ssl_msg[robotIndex])
    

def KepperMovement(robotIndex):
    global keeper

    keeper = ang[robotIndex] - jogador_a[robotIndex].orientation + math.pi

    if keeper > math.pi:
        keeper -= 2 * math.pi

    elif keeper < -math.pi:
        keeper += 2 * math.pi

    if abs(keeper) < 0.1:
        ssl_msg[robotIndex].cmd_vel.angular.z = 0.0
        ssl_msg[robotIndex].cmd_vel.linear.y = 1.2

    if keeper > 0.1:
        ssl_msg[robotIndex].cmd_vel.angular.z = -0.8
        ssl_msg[robotIndex].cmd_vel.linear.x = 0.0
    
    else:
        ssl_msg[robotIndex].cmd_vel.angular.z = 0.8
        ssl_msg[robotIndex].cmd_vel.linear.x = 0.0

def parada(robotIndex):
    ssl_msg[robotIndex].cmd_vel.angular.z = 0.0
    ssl_msg[robotIndex].cmd_vel.linear.x = 0.0
    pub[robotIndex].publish(ssl_msg[robotIndex])
    pub[robotIndex].publish(ssl_msg[robotIndex])
    
def parada(robotIndex):
    ssl_msg[robotIndex].cmd_vel.angular.z = 0.0
    ssl_msg[robotIndex].cmd_vel.linear.x = 0.0
    pub[robotIndex].publish(ssl_msg[robotIndex])


def defender(robotIndex):
    y = -500 if p_bola[1] < -500 else 500 if p_bola[1] > 500 else p_bola[1]
    diff_y = y - jogador_a[robotIndex].y
    
    if abs(diff_y) > 50:
        ssl_msg[robotIndex].cmd_vel.linear.y = 1 if diff_y > 0 else -1
    else:
        ssl_msg[robotIndex].cmd_vel.linear.y = 0
    
    pub[robotIndex].publish(ssl_msg[robotIndex])
    
def defensor_bola(robotIndex):
    y = p_bola[1]
    diff_y = y - jogador_a[robotIndex].y
    
    if abs(diff_y) > 50:
        ssl_msg[robotIndex].cmd_vel.linear.y = 1 if diff_y > 0 else -1
    else:
        ssl_msg[robotIndex].cmd_vel.linear.y = 0
    
    pub[robotIndex].publish(ssl_msg[robotIndex])
    
def manter_ang(robotIndex):
    diff_y = 0 - jogador_a[robotIndex].orientation
    
    if abs(diff_y) >= .1:
        ssl_msg[robotIndex].cmd_vel.angular.z = .1 if diff_y > 0 else -.1
    else:
        ssl_msg[robotIndex].cmd_vel.angular.z = 0
    
    pub[robotIndex].publish(ssl_msg[robotIndex])
        
mover_gol = False
def manter_linha(robotIndex):
    global mover_gol
    x = -1900
    diff_x = x - jogador_a[robotIndex].x
    
    if abs(diff_x) > 7:
        mover_gol = True
        ssl_msg[robotIndex].cmd_vel.linear.x = .2 if diff_x > 0 else -.2
    elif mover_gol:
        mover_gol = False
        ssl_msg[robotIndex].cmd_vel.linear.x = 0
    
    pub[robotIndex].publish(ssl_msg[robotIndex])

def manter_defensor(robotIndex, at_x):
    x = at_x
    diff_x = x - jogador_a[robotIndex].x
    
    if abs(diff_x) > 7:
        ssl_msg[robotIndex].cmd_vel.linear.x = .4 if diff_x > 0 else -.4
    elif mover_gol:
        ssl_msg[robotIndex].cmd_vel.linear.x = 0
        
distancia_bola_goleiro = lambda index: math.sqrt((p_bola[0]-jogador_a[index].x)**2 + (p_bola[1]-jogador_a[index].y)**2)

def move(id, pos : tuple, goal : tuple) -> None:
        KP_linear = 0.08
        KP_ang = 2.0
        delta = goal[2] - pos[2]
        if abs(delta) > np.pi:
            delta = (np.pi - delta) -1

        ssl_msg[id].cmd_vel.angular.z = KP_ang * delta

        d_x = goal[0] - pos[0]
        d_y = goal[1] - pos[1]
        theta2 = atan2(d_y, d_x)
        angulo = theta2 - pos[2]
        dist = np.linalg.norm((d_x, d_y))
        vel = KP_linear * dist
        if vel >1.0:
            vel = 1.0
        v_x = np.cos(angulo) * vel
        v_y = np.sin(angulo) * vel
        ssl_msg[id].cmd_vel.linear.x=v_x
        ssl_msg[id].cmd_vel.linear.y=v_y
        pub[id].publish(ssl_msg[id])

        return

def ataque_jog_azul(id : int):
    if p_bola[1]>=0:
        move(id,(jogador_a[id].x,jogador_a[id].y,0),(p_bola[0],p_bola[1],0))
        if jogador_a[id].x - p_bola[0]<10 and jogador_a[id].y - p_bola[1]<10: 
            ssl_msg[id].kicker=True
            pub[id].publish(ssl_msg[id])
            ssl_msg[id].kicker=False
            pub[id].publish(ssl_msg[id])
            

def goleiro(robotIndex):
    manter_ang(robotIndex)
    manter_linha(robotIndex)
    
    
    if verifica_area(p_bola[0], p_bola[1]):
        defender(robotIndex)
        
        if distancia_bola_goleiro(robotIndex) < 400:
            chutar(robotIndex)
        
def def_area_1(posX, posY): 
    if posX > -1800 and posX < 100:
        if posY > 500 and posY < 1900:
            return True
        else:
            return False
    else:
        return False

def def_area_2(posX, posY): 
    if posX > -1800 and posX < 150:
        if posY < -500 and posY > -1900:
            return True
        else:
            return False
    else:
        return False
    
def def_area_3(posX, posY): 
    if posX > -1000 and posX < 100:
        if posY > -1000 and posY < 1000:
            return True
        else:
            return False
    else:
        return False
    
    
    
def defensor_tras_1(jogIndex, at_x, at_y):
    
    x = at_x
    y = at_y
    
    diferenca_x = x - jogador_a[jogIndex].x
    diferenca_y = y - jogador_a[jogIndex].y
        
    
    if abs(diferenca_x) > 7:
        ssl_msg[jogIndex].cmd_vel.linear.x = .2 if diferenca_x > 0 else -.2
    elif mover_gol:
        ssl_msg[jogIndex].cmd_vel.linear.x = 0
    

    if abs(diferenca_y) > 7:
        ssl_msg[jogIndex].cmd_vel.linear.y = .2 if diferenca_y > 0 else -.2
    elif mover_gol:
        ssl_msg[jogIndex].cmd_vel.linear.y = 0
    
def defensor_1(jogIndex):
    manter_ang(jogIndex)
    manter_defensor(jogIndex, -900)
    
    if def_area_1(p_bola[0], p_bola[1]):
        defensor_bola(jogIndex)
        
        if distancia_bola_goleiro(jogIndex) < 400:
            chutar(jogIndex)
    else:
        defensor_tras_1(jogIndex, -900, 1000)

def defensor_2(jogIndex):
    manter_ang(jogIndex)
    manter_defensor(jogIndex, -900)
    
    if def_area_2(p_bola[0], p_bola[1]):
        defensor_bola(jogIndex)
        
        if distancia_bola_goleiro(jogIndex) < 400:
            chutar(jogIndex)
    
    else: defensor_tras_1(jogIndex, -900, -1000)
    
def defensor_3(robotIndex):
    manter_ang(robotIndex)
    manter_defensor(robotIndex, -450)
    
    if def_area_3(p_bola[0], p_bola[1]):
        defensor_bola(robotIndex)
        
        if distancia_bola_goleiro(robotIndex) < 400:
            chutar(robotIndex)
    
    else: defensor_tras_1(robotIndex, -450, 0)
    


def goal(jogIndex): 
    
    global or_jog_1, or_jog_2
    
    if (dist_mod[jogIndex] < 150): 
        arc_jogadores(jogIndex)

        or_jog_1 = ang_v1 - jogador_a[jogIndex].orientation
        or_jog_2 = ang_v2 - jogador_a[jogIndex].orientation

        if or_jog_1 > math.pi:
            or_jog_1 -= 2 * math.pi

        elif or_jog_1 < -math.pi:
            or_jog_1 += 2 * math.pi

        if or_jog_2 > math.pi:
            or_jog_2 -= 2 * math.pi

        elif or_jog_2 < -math.pi:
            or_jog_2 += 2 * math.pi

        ssl_msg[jogIndex].cmd_vel.angular.z=-0.2
        if -or_jog_1 <= jogador_a[jogIndex].orientation <= or_jog_2: 
            ssl_msg[jogIndex].cmd_vel.angular.z=0.0
            ssl_msg[jogIndex].cmd_vel.linear.x=0.8

        elif abs(jogador_a[jogIndex].orientation) <or_jog_1:
            ssl_msg[jogIndex].cmd_vel.angular.z=-0.2
            ssl_msg[jogIndex].cmd_vel.linear.x=0.0

        elif (jogador_a[jogIndex].orientation) >or_jog_2:
            ssl_msg[jogIndex].cmd_vel.angular.z=0.0
            ssl_msg[jogIndex].cmd_vel.linear.x=0.0

        pub[jogIndex].publish(ssl_msg[jogIndex])

    else:
        pass
 
if __name__=="__main__":
    rospy.init_node("test_ssl", anonymous=False)
    
    sub = rospy.Subscriber("/vision", SSL_DetectionFrame, definir_dados)
    pub = {}
    num_jogadores = 5

    for i in range(num_jogadores):
        topic = '/robot_blue_{}/cmd'.format(i)
        pub[i] = rospy.Publisher(topic, SSL, queue_size=10)

    r = rospy.Rate(50)

    while not rospy.is_shutdown():
        salvar_bola()
        
        goleiro(1)
        defensor_1(0)
        defensor_2(2)
        defensor_3(3)
        ataque_jog_azul(4)
        
        for i in range(5):
            detectar(i)