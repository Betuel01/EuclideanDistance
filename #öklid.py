#öklid
from math import *
points = []
distance= []
def euclideanDistance():
    x1 = abs(int(input("X1 sayısını giriniz:")))
    x2 = abs(int(input("X2 sayısını giriniz:")))
    y1 = abs(int(input("Y1 sayısını giriniz:")))
    y2 = abs(int(input("Y2 sayısını giriniz:")))
    global points
    points.append((x1,y1)) 
    points.append((x2,y2))
    d = int(sqrt((x1 - x2)**2 + (y1 - y2)**2))
    global distance
    distance.append(d)
    print("Verilen noktalar arasındaki uzaklık: " ,d)
while True:
    print("---Öklid Hesaplama---")
    euclideanDistance()    