'''
MicroPython en un sistema embebido es crear un programa 
que controle un LED usando un microcontrolador como el ESP8266 o ESP32

Requisitos:
Un microcontrolador compatible con MicroPython (ESP8266 o ESP32).
Un LED.
Una resistencia (220 ohmios es común).
Cables de conexión.

Conexiones:
Conecta el ánodo del LED (el pin más largo) a un pin GPIO del microcontrolador.
Conecta el cátodo del LED a una resistencia.
Conecta el otro extremo de la resistencia a GND en el microcontrolador.
'''



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
    



