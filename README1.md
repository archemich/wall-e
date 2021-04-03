# Интеграция консоли в сайт

## Установка GO
``` 
sudo apt-get update
sudo apt-get -y upgrade
cd /tmp
wget https://dl.google.com/go/go1.11.linux-amd64.tar.gz
sudo tar -xvf go1.11.linux-amd64.tar.gz
sudo mv go /usr/local
``` 
## Задание путей
```
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
source ~/.profile
go version (чтобы проверить корректность установки)
go env (информация об окржуении, путях и тд)
```
##  Установка GOTTY
```
go get github.com/yudai/gotty
gotty top (тест работаспособности, дожен появится утилита htop)
```
Далее вместе top можно забивать другие команды, мы будем использовать tmux(должен быть установлен sudo apt install tmux).

## HTML-код вставки 
```
<!doctype html>
<html>
   <body>
      <iframe width="560" height="315" src="http://127.0.0.1:8080/"></iframe>
   </body>
</html>
```
Естественно размеры окна можно как угодно менять. С полным списоком фич и опций можно ознакомится по ссылкам ниже. 

## Ссылки на материалы по теме
1. https://habr.com/ru/company/ruvds/blog/529836/
2. https://www.tecmint.com/gotty-share-linux-terminal-in-web-browser/
3. https://github.com/yudai/gotty