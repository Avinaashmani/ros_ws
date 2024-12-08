#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


class ROS_TEM:

    def __init__(self):
        rospy.init_node('ROSPY_TEMPLATE', anonymous=False)
        rospy.loginfo ("Welcome, ROSPY_TEMPLATE_NODE has begun")

        self.stamp = rospy.Time.now()
        self.rate = 10.0
        self.Q_size = 10.0

        self.publisher = rospy.Publisher('rospy_template/publisher', String, queue_size=self.Q_size)
        
    def ros_spin(self):
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.compute()
            r.sleep()

    def compute(self):
        while True:
            self.string_ = String()
            self.string_.data = "Hello"
            self.publisher.publish(self.string_)
        
if __name__ =='__main__':
    try:
        rospy_temp = ROS_TEM()
        rospy_temp.ros_spin()

    except rospy.ROSInternalException as e:
        print (e)
        pass