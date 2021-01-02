#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
import rospy #  ROS pythonで必要なモジュール
from geometry_msgs.msg import Twist
from kbhit import *   # kbhit.pyをインポート

def teleop():
    atexit.register(set_normal_term)
    set_curses_term()
    # ノードの初期化。第1引数はノード名。第2引数はノード名がユニークになるように乱数をつける。
    rospy.init_node('my_teleop', anonymous=True)  

    #　パブリッシャーの生成。第1引数はトピック名、第2引数は型、第3引数はメッセージバッファのサイズ。
    pub = rospy.Publisher('/teleop', Twist, queue_size=1)

    # ループの周期。この場合は50Hz、1秒間に50回。
    rate = rospy.Rate(50) 

    vel = Twist()

    print("w: forward, s: backward, d: right, a:left")

    while not rospy.is_shutdown():
        if kbhit():     # 何かキーが押されるのを待つ
            key = getch()   # 1文字取得
            print(key)
            if key == 'w': 
                vel.linear.x  =  0.01
            elif key == 's':
                vel.linear.x  = -0.01
            elif key == 'a':
                vel.angular.z =  0.1
            elif key == 'd':
                vel.angular.z = -0.1
                # linear.xは前後方向の並進速度(m/s)。前方向が正。
                # angular.zは回転速度(rad/s)。反時計回りが正。
            else:
                print("Input f, b, l, r")
            pub.publish(vel)    # 速度指令メッセージをパブリッシュ
        
        vel.linear.x  = 0.0 # 並進速度の初期化
        vel.angular.z = 0.0 # 回転速度の初期化
        rate.sleep()        # 指定した周期でループするよう寝て待つ

if __name__ == '__main__':
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass

