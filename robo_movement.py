import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(15,gpio.OUT)   #Left motor input A
    gpio.setup(16,gpio.OUT)   #Left motor input B
    gpio.setup(11,gpio.OUT)  #Right motor input A
    gpio.setup(13,gpio.OUT)  #Right motor input B
    gpio.setwarnings(False)
def forward(tf):
    gpio.output(15,0)
    gpio.output(16,1)
    gpio.output(11,0)
    gpio.output(13,1)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    gpio.output(15,1)
    gpio.output(16,0)
    gpio.output(11,1)
    gpio.output(13,0)
    time.sleep(tf)
    gpio.cleanup()
    
def turn_left(tf):
    gpio.output(15,True)
    gpio.output(16,True)
    gpio.output(11,True)
    gpio.output(13,False)
    time.sleep(tf)
    gpio.cleanup()

    
def turn_right(tf):
    gpio.output(15,False)
    gpio.output(16,False)
    gpio.output(11,False)
    gpio.output(13,True)
    time.sleep(tf)
    gpio.cleanup()
    
    
    
def pivot_left(tf):
    gpio.output(15,True)
    gpio.output(16,False)
    gpio.output(11,True)
    gpio.output(13,False)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_right(tf):
    gpio.output(15,False)
    gpio.output(16,True)
    gpio.output(11,False)
    gpio.output(13,True)
    time.sleep(tf)
    gpio.cleanup()
    

def key_input(event):
    init()
    print("KEY:",event.char)
    key_press=event.char
    sleep_time=0.030
    
    if(key_press.lower()=='w'):
        forward(sleep_time)
    elif(key_press.lower()=='s'):
        reverse(sleep_time)
    elif(key_press.lower()=='a'):
        turn_left(sleep_time)
    elif(key_press.lower()=='d'):
        turn_right(sleep_time)
    elif(key_press.lower()=='q'):
        pivot_left(sleep_time)
    elif(key_press.lower()=='e'):
        pivot_right(sleep_time)
    gpio.cleanup()
        
command=tk.Tk()
command.bind("<KeyPress>",key_input)
command.mainloop()
    