import datetime
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

trigger_ready = True


def photoEvent():
 	global trigger_ready
	i = datetime.datetime.now()
	filename = i.isoformat()
	cmd = 'raspistill -o ./photos/' + filename + '.jpg -t 2000'
	
	if trigger_ready:
		trigger_ready = False
		print ("clicked" + filename)
		pid = subprocess.call(cmd, shell=True)

while 1:
	if GPIO.input(11):
		GPIO.output(13, False)
		if trigger_ready:
			photoEvent()
			trigger_ready = False
	else:
		GPIO.output(13, True)
		#print "not clicked"
		trigger_ready = True	
