#!/usr/bin/env python
import rospy
import time
from scipy.interpolate import interp1d
from sensor_msgs.msg import Imu
##from beginner_tutorials.msg import motorSpeed

#declarations
fl=0
fr=0
rl=0
rr=0
sfl=0
sfr=0
srl=0
srr=0
speed=0
z=0
los=2 
heading=0
pub=rospy.Publisher('values',motorSpeed,queue_size=1)
rospy.init_node('turtleRover', anonymous=True)
msg=motorSpeed()

def current_angle(): #(-1,1)
	global z
	if(z<=0):
		m=interp1d([0,-1],[0,180])
	else:
		m=interp1d([1,0],[180,360])
	x=m(z)
	return(x)


def set_speed(spd):
	global speed
	speed=spd

def stop():
	global fl,fr,rl,rr,sfl,sfr,srl,srr
	fl=0
	fr=0
	rl=0
	rr=0
	sfl=0
	sfr=0
	srl=0
	srr=0


def turn(heading): #(0,360) 
	while not current_angle()<=(heading+los)%360 && current_angle()>=(heading-los)%360:
		if((current_angle()+180)%360>=heading):
			fl=2
			rl=2
			fr=1
			rr=1
			sfl=sfr=srl=srr=speed
			
		else:
			fl=1
			rl=1
			fr=2
			rr=2
			sfl=sfr=srl=srr=speed
	stop()

def RT(angle):
	global fl,fr,rl,rr,los
	destination=(current_angle()+angle)%360
	while not current_angle()<=(destination+los)%360 && current_angle()>=(destination-los)%360:
		fl=2
		rl=2
		fr=1
		rr=1
		sfl=sfr=srl=srr=speed
	stop()


def LT(angle):
	global fl,fr,rl,rr,los
	destination=(current_angle()-angle)%360
	while not current_angle()<=(destination+los)%360 && current_angle()>=(destination-los)%360:
		fl=1
		rl=1
		fr=2
		rr=2
		sfl=sfr=srl=srr=speed
	stop()

def FD(units): # unit is sec
	global fl,fr,rl,rr
	t=time.time()
	while not (time.time()-t)>=units:
		fl=2
		rl=2
		fr=2
		rr=2
		sfl=sfr=srl=srr=speed
	stop()

def BD(units):
	global fl,fr,rl,rr
	t=time.time()
	while not (time.time()-t)>=units or units==-1:
		fl=1
		rl=1
		fr=1
		rr=1
		sfl=sfr=srl=srr=speed
	stop()


def callback(data):
	global z
	global fl,fr,rl,rr
	z=data.orientation.z
	
	print "frontL: ",fl,"	","frontR: ",fr,"\n\n"
	print "rearL: ",rl,"	","rearR: ",rr,"\n\n\n"
		
def listener():
	rospy.Subscriber('android/imu',Imu,callback,queue_size=4)
	while True:
		instruction=input("INSTRUCTION: ")
		if(x[0:2]=="RT"):
			RT(int(x[2:]))
		elif(x[0:2]=="LT"):
			LT(int(x[2:]))
		elif(x[0:2]=="FD"):
			FD(int(x[2:]))
		elif(x[0:2]=="BD"):
			BD(int(x[2:]))
		elif(x.strip()=="S"):
			stop()
			
		if(x[0:3]=="SET"):
			set_speed(int(x[3:]))
	
	rospy.spin()