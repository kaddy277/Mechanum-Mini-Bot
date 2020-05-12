#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import motorSpeed
import raspi_i2c
def callback(data):
	# print data.frontLeft,data.frontRight
	# print data.rearLeft,data.rearRight
	info=[data.frontLeft,data.frontRight,data.rearLeft,data.rearRight]
	print info
	raspi_i2c.SendDataToArduino(info)
	print("\n")

def listener():
	rospy.init_node('speedSubscriber',anonymous=False)
	rospy.Subscriber('values',motorSpeed,callback,queue_size=4)
	rospy.spin()

listener()