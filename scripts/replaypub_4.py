#!/usr/bin/env python
import rospy
import pygame
import time
from beginner_tutorials.msg import motorSpeed
from scipy.interpolate import interp1d

#declarations
fl=rl=fr=rr=0
speed=0
sfl=srl=sfr=srr=0
replayDir=0
replayTime=0
record=0
status=0
chronology_samjhiye=[]
autonomous=0
step=-1
step_done=1
done = False
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()
pub=rospy.Publisher('values',motorSpeed,queue_size=1)
rospy.init_node('speedPublisher', anonymous=True)
msg=motorSpeed()
#

# main code
while not rospy.is_shutdown():
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			done = True 
		#if event.type == pygame.JOYBUTTONDOWN and event.button==2 and record==0:
			#record=1
			#chronology_samjhiye=[]
			#t=time.time()
		if event.type == pygame.JOYBUTTONDOWN and event.button==4 and record==1:
			chronology_samjhiye.append([(time.time()-t),status])
			record=0
		if event.type == pygame.JOYBUTTONDOWN and event.button==3 and autonomous==0:
			autonomous=1
		if event.type == pygame.JOYBUTTONDOWN and event.button==5 and autonomous==1:
			autonomous=0

	if autonomous==1:
		if step_done:
			step=step+1
			try:
				replayTime=chronology_samjhiye[step][0]
				replayDir=chronology_samjhiye[step][1]
				step_done=0
				t=time.time()
			except:
				autonomous=0
				step=-1
		if not step_done:
			if (time.time()-t)>=replayTime:
				step_done=1

		
	joystick_count = pygame.joystick.get_count()
	for i in range(joystick_count):
		joystick = pygame.joystick.Joystick(i)
		joystick.init()

		axis0=joystick.get_axis(0)
		axis1=joystick.get_axis(1)
		axis3=joystick.get_axis(3)
		m=interp1d([1,-1],[0,255])
		speed=int(m(axis3))
		button=joystick.get_button(0)	
		 
		if((axis0<-0.77 and button==1) or replayDir==-5):	#mov=-5
			if(record==1):
				if(status!=-5):
					chronology_samjhiye.append([(time.time()-t),status])
					status=-5
					t=time.time()
			fl=1
			rl=1
			fr=2
			rr=2
		elif((axis0>0.77 and button==1) or replayDir==5):#mov=5
			if(record==1):
				if(status!=5):
					chronology_samjhiye.append([(time.time()-t),status])
					status=5
					t=time.time()
			fl=2
			rl=2 
			fr=1
			rr=1
		elif((axis0>0.77 and axis1<-0.77) or replayDir==2):#mov=2
			if(record==1):
				if(status!=2):
					chronology_samjhiye.append([(time.time()-t),status])
					status=2
					t=time.time()
			fl=2
			rl=0
			fr=0
			rr=2
		elif((axis0<-0.77 and axis1<-0.77) or replayDir==-4):#mov=-4
			if(record==1):
				if(status!=-4):
					chronology_samjhiye.append([(time.time()-t),status])
					status=-4
					t=time.time()
			fl=0
			rl=2
			fr=2
			rr=0
		elif((axis0<-0.77 and axis1>0.77) or replayDir==-2):#mov=-2
			if(record==1):
				if(status!=-2):
					chronology_samjhiye.append([(time.time()-t),status])
					status=-2
					t=time.time()
			fl=1
			rl=0
			fr=0
			rr=1
		elif((axis0>0.77 and axis1>0.77) or replayDir==4):#mov=4
			if(record==1):
				if(status!=4):
					chronology_samjhiye.append([(time.time()-t),status])
					status=4
					t=time.time()
			fl=0
			rl=1
			fr=1
			rr=0
		elif(axis0<-0.77 or replayDir==-3):#mov=-3
			if(record==1):
				if(status!=-3):
					chronology_samjhiye.append([(time.time()-t),status])
					status=-3
					t=time.time()
			fl=1
			rl=2
			fr=2
			rr=1
		elif(axis0>0.77 or replayDir==3):#mov=3
			if(record==1):
				if(status!=3):
					chronology_samjhiye.append([(time.time()-t),status])
					status=3
					t=time.time()
			fl=2
			rl=1
			fr=1
			rr=2
		elif(axis1>0.77 or replayDir==-1):#mov=-1
			if(record==1):
				if(status!=-1):
					chronology_samjhiye.append([(time.time()-t),status])
					status=-1
					t=time.time()
			fl=1
			rl=1
			fr=1
			rr=1
		elif(axis1<-0.77 or replayDir==1):#mov=1
			if(record==1):
				if(status!=1):
					chronology_samjhiye.append([(time.time()-t),status])
					status=1
					t=time.time()
			fl=2
			rl=2
			fr=2
			rr=2
		else:
			if(record==1):
				if(status!=0):
					chronology_samjhiye.append([(time.time()-t),status])
					status=0
					t=time.time()
			fl=0
			rl=0
			fr=0
			rr=0

		sfl=srl=sfr=srr=speed
		
		if fl==0:
			sfl=0
		if rl==0:
			srl=0
		if fr==0:
			sfr=0
		if rr==0:
			srr=0


		print "speed: ",speed,"\n"
		print "frontL: ",fl,"	","frontR: ",fr,"\n\n"
		print "rearL: ",rl,"	","rearR: ",rr,"\n\n\n"

		msg.frontLeft=fl
		msg.frontRight=fr
		msg.rearLeft=rl
		msg.rearRight=rr
		msg.speedFL=sfl
		msg.speedFR=int(0.8*sfr)
		msg.speedRL=srl
		msg.speedRR=int(0.8*srr)
		print (chronology_samjhiye)
		print step,replayTime,replayDir
		pub.publish(msg)
		#rospy.loginfo(msg)
	clock.tick(30)
pygame.quit()
