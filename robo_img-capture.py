import dropbox
import picamera
import time
import datetime
import string
import random
import RPi.GPIO as GPIO

servopin=24
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(servopin,GPIO.OUT)
p=GPIO.PWM(servopin,50)
p.start(7.5)

p_format='jpeg'
camera=picamera.PiCamera()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.IN)
print("Starting PIR sensor")

def cam_cap(filename):
    camera.vflip=True
    camera.capture(filename+'.'+p_format,format=p_format,resize=(500,500))
    time.sleep(2)
    print("Picture shot")
    return filename+'.'+p_format

def img_upload(localfile):
    uploadPath='/'+localfile
    with open(localfile,'rb') as f:
        print('Uploading')
        access_token='g9Xoz7OBHGAAAAAAAAAAGU6xaDLQjkgNkEsfHWQzuwKV32oORKVYaYPuG2aEkJK_'
        dbx=dropbox.Dropbox(access_token)
        dbx.files_upload(f.read(),uploadPath)
    f.close()
    

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def cameras():
    filename=id_generator()
    file=cam_cap(filename)
    img_upload(file)
    print('Done Uploading')
print('hi')   
def all_sensor():
    while True:
        i=GPIO.input(22)
        if(i==0):
            print("No Humans Found")
            time.sleep(10)
        elif(i==1):
            print("Humans Found")
            print("PLZ stop the car!!!")
            time.sleep(5)
            
            p.ChangeDutyCycle(2.5)
            time.sleep(10)
            cameras()
            print('1...')
            
            p.ChangeDutyCycle(7.5)
            time.sleep(10)
            cameras()
            print('2...')
            
            p.ChangeDutyCycle(12.5)
            time.sleep(10)
            cameras()
            print('3...')
            
            print('Taken Picture of the Area....')
            time.sleep(1)
            p.ChangeDutyCycle(7.5)
            print('Start your Car...')
            time.sleep(80)
            
            
            


def main_int():
    try:
        all_sensor()
    except KeyboardInterrupt:
        print('ROBOT SHUTDOWN')
    
    
main_int()