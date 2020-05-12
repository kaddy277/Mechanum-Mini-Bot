#!/usr/bin/env python

import rospy
import time
from beginner_tutorials.msg import TwoInputGate
from beginner_tutorials.msg import GateOutput
from beginner_tutorials.msg import Total

a=10
b=20
pub1 =rospy.Publisher('all',Total,queue_size=1)
def callback(data):
	global a,b,pub1
	msg1=Total()
	msg1.a=a
	msg1.b=b
	print "          ",a+b,data.output
	msg1.sum=data.output
	pub1.publish(msg1)

def publish_info():
	global a,b
	pub = rospy.Publisher('gateInputs', TwoInputGate, queue_size = 1)
	rospy.init_node('publisher', anonymous=True)
	msg=TwoInputGate()
	rospy.Subscriber('/gateOutput',GateOutput,callback,queue_size=1)
	while not rospy.is_shutdown():
		a += 1
		b += 1
		print(a,b)
		msg.input1 = a
		msg.input2 = b
		pub.publish(msg)
		time.sleep(0.5) #to synchronize with subscriber
		#rospy.Subscriber('gateOutput',GateOutput,callback,queue_size=1)

if __name__ == '__main__':
	try:
		publish_info()
	except rospy.ROSInterruptException:
		pass
