#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
import rospy #  ROS pythonで必要なモジュール
from kbhit import *   # kbhit.pyをインポート
from std_msgs.msg import Int8


def teleop():
    atexit.register(set_normal_term)
    set_curses_term()
    # ノードの初期化。第1引数はノード名。第2引数はノード名がユニークになるように乱数をつける。
    rospy.init_node('my_teleop', anonymous=True)  

    #　パブリッシャーの生成。第1引数はトピック名、第2引数は型、第3引数はメッセージバッファのサイズ。
    pub = rospy.Publisher('/teleop', Int8, queue_size=1)

    # ループの周期。この場合は50Hz、1秒間に50回。
    rate = rospy.Rate(50) 

    print("w: forward, s: backward, d: right, a:left")

    while not rospy.is_shutdown():
        if kbhit():     # 何かキーが押されるのを待つ
            key = getch()   # 1文字取得
            print(key)
            if key == 'a':
                pub.publish(1)
            elif key == 'd':
                pub.publish(-1)
                # linear.xは前後方向の並進速度(m/s)。前方向が正。
                # angular.zは回転速度(rad/s)。反時計回りが正。
            else:
                print("Input f, b, l, r")
                
        else:
            pub.publish(0)
                # 速度指令メッセージをパブリッシュ
        rate.sleep()        # 指定した周期でループするよう寝て待つ

if __name__ == '__main__':
    try:
        teleop()
    except rospy.ROSInterruptException:
        pass

