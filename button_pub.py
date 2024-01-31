#!/usr/bin/env python3
import sys
import rospy as rp
from std_msgs.msg import String
from time import sleep
# Initialize ros node
rp.init_node("web_pub")
rp.loginfo("hello from web_pub")
# Create publisher
pub = rp.Publisher("/cmd_button", String, queue_size=10)

#sleep(60)
args = sys.argv
msg = args[1]
pub.publish(msg)
rp.loginfo(msg)
