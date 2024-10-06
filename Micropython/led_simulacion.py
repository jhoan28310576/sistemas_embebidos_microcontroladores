import time

#simulacion del estado de un led
led_state = False #False = apagado, True = encendido

while True:
    #cambiamos el estado del led
    led_state = not led_state

    #imprimimos el estado del led
    if led_state:
        print("Led encendido")
    else:
        print("Led apagado")

    #esperamos 1 segundo
    time.sleep(1)

#codigo aplicado en la practica 

from machine import Pin
from time import sleep
#definimos el pin del led
led = Pin(2, Pin.OUT)

while True:
    led.value(1)#encendemos el led
    sleep(1) # esperamos 1 segundo 
    led.value(0) #apagamos el led
    sleep(1) # esperamos 1 segundo 
    



