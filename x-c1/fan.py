#!/usr/bin/python
import pigpio
import time

servo = 18

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 25000 )
pwm.set_PWM_range(servo, 100)

last = 0

while(1):
     #get CPU temp
     file = open("/sys/class/thermal/thermal_zone0/temp")
     temp = float(file.read()) / 1000.00
     temp = float('%.2f' % temp)
     file.close()

     if(temp > 30 and last != 40):
          pwm.set_PWM_dutycycle(servo, 40)
          last = 40

     if(temp > 50 and last != 50):
          pwm.set_PWM_dutycycle(servo, 50)
          last = 50

     if(temp > 60 and last != 70):
          pwm.set_PWM_dutycycle(servo, 70)
          last = 70

     if(temp > 70 and last != 80):
          pwm.set_PWM_dutycycle(servo, 80)
          last = 80

     if(temp > 75 and last != 100):
          pwm.set_PWM_dutycycle(servo, 100)
          last = 100

     if(temp < 30 and last != 0):
          pwm.set_PWM_dutycycle(servo, 0)
          last = 0

     time.sleep(1)