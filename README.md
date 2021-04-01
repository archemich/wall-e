# Веб интерфейс доя контроля состояния робота

Последовательность действий для запуска

1. Установка PostrgeSQL:
    ``` 
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```
2. Настройка PostgreSQL и создания базы данных:
    ```
    sudo -i -u postgres
    psql
    ALTER USER postgres WITH PASSWORD 'root';
    create database sfedu_project;
    ```
3. Установка Java11 и сборщика Maven
    ```
    sudo apt-get install openjdk-11-jdk
    java -version
    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
    echo $JAVA_HOME

    sudo apt install maven
    mvn -version  
    ```
4. Сборка и запуск:
    ```
    mvn clean
    mvn build
    mvn spring0boot:run
    ```