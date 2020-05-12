#!/usr/bin/env python
import rospy
import pygame
import time
from beginner_tutorials.msg import motorSpeed

fr=fl=rr=rl=0
done = False
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
pub=rospy.Publisher('values',motorSpeed,queue_size=1)
rospy.init_node('speedPublisher', anonymous=True)
msg=motorSpeed()
while not rospy.is_shutdown() :
	fr=fl=rr=rl=0
	for event in pygame.event.get(): # User did something.
		if event.type == pygame.QUIT: # If user clicked close.
			done = True # Flag that we are done so we exit this loop.
		elif event.type == pygame.JOYBUTTONDOWN:
			pass#print "Button ",event.button," pressed"
		elif event.type == pygame.JOYBUTTONUP:
			pass#print "Button ",event.button," released"

	joystick_count = pygame.joystick.get_count()
	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()

		axis3=joystick.get_axis(3)
		if(axis3<-0.9):
			fl=1
			rl=1
			fr=2
			rr=2
		elif(axis3>0.9):
			fl=2
			rl=2
			fr=1
			rr=1

		hats = joystick.get_numhats()
		for i in range(hats):
			hat = joystick.get_hat(0) 
			#print(str(hat))
			if(hat==(-1,0)):
				fl=1
				rl=2
				fr=2
				rr=1
			elif(hat==(1,0)):
				fl=2
				rl=1
				fr=1
				rr=2
			elif(hat==(0,-1)):
				fl=1
				rl=1
				fr=1
				rr=1
			elif(hat==(0,1)):
				fl=2
				rl=2
				fr=2
				rr=2
			elif(hat==(1,1)):
				fl=2
				rl=0
				fr=0
				rr=2
			elif(hat==(-1,1)):
				fl=0
				rl=2
				fr=2
				rr=0
			elif(hat==(-1,-1)):
				fl=1
				rl=0
				fr=0
				rr=1
			elif(hat==(1,-1)):
				fl=0
				rl=1
				fr=1
				rr=0
			# else:
			# 	fl=0
			# 	rl=0
			# 	fr=0
			# 	rr=0
			print "frontL: ",fl,"	","frontR: ",fr,"\n\n"
			print "rearL: ",rl,"	","rearR: ",rr,"\n\n\n"
			msg.frontLeft=fl
			msg.frontRight=fr
			msg.rearLeft=rl
			msg.rearRight=rr
			pub.publish(msg)
			#rospy.loginfo(msg)
	clock.tick(30)
pygame.quit()
