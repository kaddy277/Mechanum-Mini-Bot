#!/usr/bin/env python
import time
import rospy
from beginner_tutorials.msg import TwoInputGate
from beginner_tutorials.msg import GateOutput
pub1 = rospy.Publisher('gateOutput',GateOutput, queue_size=1)

def callback(data):
	global pub1
	output=data.input1+data.input2
	print(data.input1,data.input2,output)
	msg1=GateOutput()
	msg1.output=output
	#time.sleep(2) #asynchronous if delay is before publishing the data
	pub1.publish(msg1)
	#time.sleep(2) #synchronous if delay is after publishing

	# but logically delay will come before publishing as calculations are done before publishing if they are tedious
	# so how to synchronize?
	# method 1: find the computational time of the subscriber that is publishing back and keep the delay in publishing slightly more than that

def subsrcibe_info():
	rospy.init_node('subscriber', anonymous=True)
	rospy.Subscriber('gateInputs', TwoInputGate, callback,queue_size=1)
	rospy.spin()

if __name__ == '__main__':
	subsrcibe_info()
	
