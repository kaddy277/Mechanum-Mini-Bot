#!/usr/bin/env python
import os
import smbus
import time

bus=smbus.SMBus(1)
arduinoI2C_address=0x07
arduinoI2C_command=0x01

def SendDataToArduino(info):

	bus.write_i2c_block_data(arduinoI2C_address,arduinoI2C_command,info)



