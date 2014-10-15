import datetime
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

trigger_ready = True


def photoEvent():
 	global trigger_ready
	filename = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
	cmd = 'raspivid -hf -t 5000 -o ./videos/' + filename + '.h264 && MP4Box -add ./videos/' + filename + '.h264 ./videos/' + filename + '.mp4'

	if trigger_ready:
		trigger_ready = False
		print ("clicked " + filename)
		pid = subprocess.check_call(cmd, shell=True)
		

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


