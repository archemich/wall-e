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
    
Если когда-нибудь надо будет статью
1. http://earchive.tpu.ru/bitstream/11683/47752/1/TPU541998.pdf
2. https://medium.com/nuances-of-programming/%D0%BE%D0%B1%D0%BD%D0%B0%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-%D1%86%D0%B2%D0%B5%D1%82%D0%BE%D0%B2%D0%BE%D0%B9-%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-python-9128814bc55c
3. https://habr.com/ru/post/332464/
4. https://cyberleninka.ru/article/n/avtonomnaya-navigatsiya-mobilnogo-robota-na-osnove-ultrazvukovogo-datchika-izmereniya-rasstoyaniy/viewer
5. https://cyberleninka.ru/search?q=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0%20%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B3%D0%BE%20%D0%B0%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%20%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%B0&page=6
6. https://www.reddit.com/r/ROS/comments/lywv8s/rospy_vs_roscpp/
7. https://github.com/aikoncwd/rpi-benchmark
8. https://github.com/ros/meta-ros/wiki/OpenEmbedded-Build-Instructions#add-meta-ros-to-an-existing-openembedded-project
