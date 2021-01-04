#!/usr/bin/env python2.7
# -*- coding: utf8 -*-
import Tkinter
import rospy
from std_msgs.msg import Int8
import sys
import time
import random
#
# GUI設定
#
Endtime = 20
End = False

rospy.init_node('tkinterUI', anonymous=True)
x=150
y=350
dx=50
dy=50    

score = 0

#ミサイルのサイズ
m_size_x = 5
m_size_y = 15


root = Tkinter.Tk()
root.title("雨粒集めてゲーム")
root.geometry("800x450")
misile=[]
misile_x = []
misile_y = []
misile_fire = []
misile_size_list = []

misile_v = 7
#ミサイルの個数
misile_cnt = 30
#ミサイルの間隔
m_e = 800/misile_cnt

cnt = 0
text = Tkinter.StringVar()
text.set("Unko!!")
#キャンバスエリア
label = Tkinter.Label(root, textvariable=text)
label.pack()

canvas = Tkinter.Canvas(root, width = 800, height = 450,bg="white")#Canvasの作成
canvas.pack()#Canvasの配置
square = canvas.create_rectangle(5, 5, 5+dx, 5+dy, fill = 'black')#塗りつぶし

for count in range(misile_cnt):
    misile_x.append(count*m_e)
    misile_y.append(-30)
    misile_size_list.append(m_size_y*random.randint(1,3))
    misile.append(canvas.create_rectangle(misile_x[count], misile_y[count], misile_x[count] + m_size_x, misile_y[count] +misile_size_list[count], fill = 'black')) 
    misile_fire.append(False)

def misile_maneger():
    for count in range(misile_cnt):
        if misile_fire[count]:
            fire_misile(count)
    
def fire_misile(num):
    global misile,misile_x,misile_y,misile_fire,y,dy,x,dx,score
    misile_x[num] += 0
    if y <= misile_y[num]+m_size_y and y+dy >= misile_y[num]:    
        if x <= misile_x[num]+m_size_x and x+dx >= misile_x[num]:
            score+=1
            
    if misile_y[num]<500:
        misile_y[num] += misile_v
    else:
        misile_y[num]=-30
        misile_size_list[num] = m_size_y*random.randint(1,3)
        misile_fire[num] = False
    canvas.coords(misile[num],misile_x[num],misile_y[num],misile_x[num]+m_size_x,misile_y[num]+misile_size_list[num])

def callback(num):
    global x,y,dx,dy,cnt,score,Endtime,canvas,End
    if cnt <50*Endtime:
        cnt += 1
        text.set("score:"+str(score)+"  time:"+str(Endtime-cnt/50))
        canvas.coords(square,x,y,x+dx,y+dy)
        x += 10*num.data
        misile_maneger()
        if cnt % 20 == 0:
            num = random.randint(0,misile_cnt-1)
            if not misile_fire[num]:
                misile_fire[num] = True
    else:
        if not End:
            text.set("!!END!!")
            canvas.create_rectangle(0,0,800,450,fill = 'white',)
            canvas.create_text(400, 100, text = "score:"+str(score), font = ('MSゴシック', 100), fill = 'black')
            End = True
    root.update()
print("start!")
rospy.Subscriber("/teleop", Int8, callback)
root.mainloop()       