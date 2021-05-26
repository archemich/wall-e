import numpy as np
import cv2
import video

#сигнал от клиента
USLOVNAYA_PEREMENNAYA = 1;
#Устанавливаем диапозон по hsv 
if(USLOVNAYA_PEREMENNAYA == 0):
    hsv_min = np.array((40,100,100), np.uint8)
    hsv_max = np.array((80,255,255), np.uint8)
else:
    hsv_min = np.array((110,120,120), np.uint8)
    hsv_max = np.array((130,255,255), np.uint8)
#окна для вывода инфы(отключить на малинке)
# cv2.namedWindow( "result" ) 
# cv2.namedWindow( "contours" ) 
# cv2.namedWindow( "thresh" ) 


# цвет прямоугольника (B, G, R)
RECTCOLOR = (0, 255, 0)

# толщина линии прямоугольника
RTHICK = 2

# определяем функцию проверки размера пятна
BLOBSIZE = 1300
def checkSize(w, h):
    if w * h > BLOBSIZE:
        return True
    else:
        return False

my_color = (0,0,255)

#номер вебки
cap = video.create_capture(0)
#разрешение потока
height = 720
width = 1280
cap.set(3, width)
cap.set(4, height)
crange = [0,0,0, 0,0,0]
width_center=width/2;

while (cap.isOpened()):
    flag, img = cap.read(0)
    # меняем цветовую модель с BGR на HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
    # применяем цветовой фильтр
    thresh = cv2.inRange(hsv, hsv_min, hsv_max )
    # ищем контуры и складируем их в переменную contours
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    kernel = np.ones((5, 5), np.uint8)
    cv2.dilate(thresh, kernel, iterations = 1)
    cv2.erode(thresh, kernel, iterations = 1)
    # hierarchy хранит информацию об иерархии
    # отображаем контуры поверх изображения
    cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 0)
    cv2.imshow('contours', img)
    cv2.drawContours(img, contours, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 2)
    image=img
    center_rectangle=2
    # если контуры найдены...
    if len(contours) != 0:
        # выводим найденные контуры
        # находим контуры бОльшего размера
        c = max(contours, key = cv2.contourArea)
        # получаем координаты прямоугольника, в который они вписаны
        x,y,w,h = cv2.boundingRect(c)
        # если прямоугольник достаточного размера...
        if checkSize(w, h):
            # выводим его
            cv2.rectangle(image, (x, y), (x+w, y+h), RECTCOLOR, RTHICK)
            cv2.putText(img, str("UP left")+str(x)+" "+str(y), (x,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
            cv2.putText(img, str("UP right")+str(x+h)+" "+str(y), (x+h,y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
            cv2.putText(img, str("down left")+str(x)+" "+str(y+w), (x,y+w), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
            cv2.putText(img, str("down right")+ str(x+h)+" "+str(y+w), (x+h,y+w), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, my_color, 2, cv2.LINE_AA)
            center_rectangle = x + h/2;
    if(width_center < center_rectangle and abs(width_center-center_rectangle)>300):
        print("GO RIGHT!!!!")
    if(width_center > center_rectangle and abs(width_center-center_rectangle)>300):
        print("GO LEFT!!!!")
    # выводим итоговое изображение в окно
    cv2.imshow('test', image)
    cv2.imshow('result', img)
    cv2.imshow('thresh', thresh)

    ch = cv2.waitKey(5)
    if ch == 27:
        break


cap.release()
# cv2.destroyAllWindows()

