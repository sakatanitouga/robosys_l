#!/usr/bin/env python2.7

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Twist
import math

rospy.init_node('marker_pub')

pub = rospy.Publisher("arrow_pub", Marker, queue_size = 10)
rate = rospy.Rate(25)

r=0
dx=0
dy=0
def callback(vel):
    global dx,dy
    global r
    rospy.loginfo("dx:%f",dx)
    rospy.loginfo("dy:%f",dy)
    
    dx+=vel.linear.x*math.cos(math.radians(r*90))
    dy+=vel.linear.x*math.sin(math.radians(r*90))
    r+=vel.angular.z*10/90
    marker_data = Marker()
    marker_data.header.frame_id = "map"
    marker_data.header.stamp = rospy.Time.now()

    marker_data.ns = "basic_shapes"
    marker_data.id = 0

    marker_data.action = Marker.ADD

    marker_data.pose.position.x = 0.0-dx*10
    marker_data.pose.position.y = 0.0-dy*10
    marker_data.pose.position.z = 0.0

    marker_data.pose.orientation.x=0.0
    marker_data.pose.orientation.y=0
    marker_data.pose.orientation.z=r
    marker_data.pose.orientation.w=1


    marker_data.color.r = 1.0
    marker_data.color.g = 0.0
    marker_data.color.b = 0.0
    marker_data.color.a = 1.0

    marker_data.scale.x = 1
    marker_data.scale.y = 0.1
    marker_data.scale.z = 0.1

    marker_data.lifetime = rospy.Duration()

    marker_data.type = 0

    pub.publish(marker_data)

    rate.sleep()

def main():    
    rospy.Subscriber("/teleop", Twist, callback)
    rospy.spin()

if __name__ == "__main__":
    main()    