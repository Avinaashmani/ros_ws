#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Temperature 

class RosTemperature:

    def __init__(self):
        
        rospy.init_node('rospy_temperature')
        rospy.loginfo("Welcome, ROS Temperature publisher has begun !")

        self.Q_size = 10.0
        self.rate = 10.0
        self.stamp = rospy.Time.now()

        self.publisher = rospy.Publisher('my_job_grow/temperature1', Temperature, queue_size=self.Q_size)

    def ros_spin(self):
        r = rospy.Rate(self.rate)
        while not rospy.is_shutdown():
            self.compute()
            r.sleep()

    def compute(self):

        temp = 10
        seq = 1
            
        self.temp_ = Temperature()
        self.temp_.header.stamp = self.stamp
        self.temp_.header.seq = seq+1
        self.temp_.temperature = temp

        self.publisher.publish(self.temp_)
        
if __name__ == "__main__":

    try:
        temp = RosTemperature()
        temp.ros_spin()

    except rospy.ROSInternalException as e:
        print(e)
        pass

    

