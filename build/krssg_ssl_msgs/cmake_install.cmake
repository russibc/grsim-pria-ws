# Install script for directory: /home/bru/grsim-pria-ws/src/krssg_ssl_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/bru/grsim-pria-ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/krssg_ssl_msgs/msg" TYPE FILE FILES
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/gr_Commands.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/gr_Packet.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/gr_Replacement.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/gr_RobotReplacement.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/gr_Robot_Command.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/gr_BallReplacement.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/SSL_DetectionFrame.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/SSL_DetectionRobot.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/SSL_DetectionBall.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/BeliefState.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/TacticPacket.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/SSL_Refbox.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/sslDebug_Line.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/sslDebug_Circle.msg"
    "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/msg/sslDebug_Data.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/krssg_ssl_msgs/cmake" TYPE FILE FILES "/home/bru/grsim-pria-ws/build/krssg_ssl_msgs/catkin_generated/installspace/krssg_ssl_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/bru/grsim-pria-ws/devel/include/krssg_ssl_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/bru/grsim-pria-ws/devel/share/roseus/ros/krssg_ssl_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/bru/grsim-pria-ws/devel/share/common-lisp/ros/krssg_ssl_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/bru/grsim-pria-ws/devel/share/gennodejs/ros/krssg_ssl_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/bru/grsim-pria-ws/devel/lib/python3/dist-packages/krssg_ssl_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/bru/grsim-pria-ws/devel/lib/python3/dist-packages/krssg_ssl_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/bru/grsim-pria-ws/build/krssg_ssl_msgs/catkin_generated/installspace/krssg_ssl_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/krssg_ssl_msgs/cmake" TYPE FILE FILES "/home/bru/grsim-pria-ws/build/krssg_ssl_msgs/catkin_generated/installspace/krssg_ssl_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/krssg_ssl_msgs/cmake" TYPE FILE FILES
    "/home/bru/grsim-pria-ws/build/krssg_ssl_msgs/catkin_generated/installspace/krssg_ssl_msgsConfig.cmake"
    "/home/bru/grsim-pria-ws/build/krssg_ssl_msgs/catkin_generated/installspace/krssg_ssl_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/krssg_ssl_msgs" TYPE FILE FILES "/home/bru/grsim-pria-ws/src/krssg_ssl_msgs/package.xml")
endif()

