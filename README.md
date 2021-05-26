# "Железная" часть робота 

## Установка ROS Noetic
Для установки фреймворка **ROS** нужно выполнить следующие шаги:

1. Добавить репозиторий и ключь шифрования
    ```
    1. sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

    2. sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

    3. sudo apt update
    ```
2.  Установить пакет **ROS** и указать пути в системе

    ```
    1. sudo apt install ros-noetic-ros-base
    
    2. source /opt/ros/noetic/setup.bash
    
    3. echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    
    4. source ~/.bashrc
    ```
3. Установка зависимостей и **rosdep** 
    ```
    1. sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator 
    python3-wstool build-essential
    
    2. sudo apt install python3-rosdep
    
    3. sudo rosdep init
    
    4. rosdep update
    ```
4. Установка системы сборки **Сatkin** и создание рабочей директории catkin
    ```
    1. sudo apt-get install ros-noetic-catkin

    2. source /opt/ros/noetic/setup.bash
    
    3. mkdir -p ~/catkin_ws/src
    
    4. cd ~/catkin_ws/
    
    5. catkin_make
    
    6. source devel/setup.bash
    
    7. echo $ROS_PACKAGE_PATH
    ```
5. Создание пакета ROS
    ```
    1. cd ~/catkin_ws/src
    
    2. catkin_create_pkg beginner_tutorials std_msgs rospy roscpp
    
    3. cd ~/catkin_ws
    
    4. catkin_make
    
    5. . ~/catkin_ws/devel/setup.bash
    ```

6. Зависимости пакетов
    ```
    1. rospack depends1 beginner_tutorials          #Не обзаятельно, смотрим зависимости пакета
    
    2. roscd beginner_tutorials && cat package.xml  #Тот же список зависимостей
    
    3. rospack depends beginner_tutorials
    ```
7. Написание нодов в пакете (Publisher/Subscriber)
    ```
    1. roscd beginner_tutorials

    2. mkdir scripts &&  cd scripts
    
    3.  wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/talker.py
    
    4. chmod +x talker.py

    5. wget https://raw.github.com/ros/ros_tutorials/kinetic-devel/rospy_tutorials/001_talker_listener/listener.py

    6. chmod +x listener.py
    ```
8. Редактирование **CMakeLists.txt**
    ```
    ...
    catkin_install_python(PROGRAMS scripts/talker.py scripts/listener.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
    )
    ...
    ```
9. Сборка созданного пакета 
    ```
    1. cd ~/catkin_ws
    2. catkin_make
    ```
10. Запуск всей системы
    ```
    1. roscore  #Запуск 
    2. cd ~/catkin_ws
    3. source ./devel/setup.bash # если раньше не прописали
    4. rosrun beginner_tutorials talker.py   
    5. rosrun beginner_tutorials listener.py 
    ```