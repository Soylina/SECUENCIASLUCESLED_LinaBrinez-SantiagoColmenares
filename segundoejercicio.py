#PRÁCTICA DE LABORATORIO N°2       
       #EJERCICIO N° 2
from machine import Pin as pin
from utime import sleep as stop, sleep_ms as para,sleep_us as pausa
led1=pin(13,pin.OUT)
led2=pin(12,pin.OUT)
led3=pin(14,pin.OUT)
led4=pin(27,pin.OUT)
led5=pin(26,pin.OUT)
led6=pin(25,pin.OUT)
led7=pin(33,pin.OUT)
led8=pin(32,pin.OUT)
led9=pin(18,pin.OUT)
led10=pin(4,pin.OUT)

def print_led(a,b,c,d,e,f,g,h,i,j):
        led1.value(a) 
        led2.value(b)
        led3.value(c)
        led4.value(d)
        led5.value(e)
        led6.value(f)
        led7.value(g)
        led8.value(h)
        led9.value(i)
        led10.value(j)
        para(500)
while True:
                #al derecho
        print_led(0,0,0,0,0,0,0,0,0,0)
        print_led(1,0,0,0,0,0,0,0,0,0)
        print_led(0,1,0,0,0,0,0,0,0,0)
        print_led(0,0,1,0,0,0,0,0,0,0)
        print_led(0,0,0,1,0,0,0,0,0,0)
        print_led(0,0,0,0,1,0,0,0,0,0)
        print_led(0,0,0,0,0,1,0,0,0,0)
        print_led(0,0,0,0,0,0,1,0,0,0)
        print_led(0,0,0,0,0,0,0,1,0,0)
        print_led(0,0,0,0,0,0,0,0,1,0)
        print_led(0,0,0,0,0,0,0,0,0,1)
        print_led(0,0,0,0,0,0,0,0,0,0)
                #al reves
        print_led(0,0,0,0,0,0,0,0,0,0)
        print_led(0,0,0,0,0,0,0,0,0,1)
        print_led(0,0,0,0,0,0,0,0,1,0)
        print_led(0,0,0,0,0,0,0,1,0,0)
        print_led(0,0,0,0,0,0,1,0,0,0)
        print_led(0,0,0,0,0,1,0,0,0,0)
        print_led(0,0,0,0,1,0,0,0,0,0)
        print_led(0,0,0,1,0,0,0,0,0,0)
        print_led(0,0,1,0,0,0,0,0,0,0)
        print_led(0,1,0,0,0,0,0,0,0,0)
        print_led(1,0,0,0,0,0,0,0,0,0)

    