#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher("robotics_itu_first_topic",String,queue_size=10)
    rospy.init_node("publisher_node",anonymous=True)
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        msg = "our very first publisher code!"
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
if __name__ == "__main__":
     publisher()
     
