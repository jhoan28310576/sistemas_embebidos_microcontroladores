''' 
descripcion:
objetivo:  Simular un sistema que enciende un ventilador cuando la temperatura supera los 25 grados Celsius.
Componentes Simulados: Sensor de temperatura y ventilador.

'''

import time
import random

TEMP_THRESHOLD = 25

def read_temperature():
    '''Simula la lectura de un sensor de temperatura.
    Retorna un valor aleatorio entre 20 y 30 grados Celsius.'''
    return random.uniform(20, 30)

def control_fan(temperature):
    '''Controla el ventilador segun la temperatura.
    Envia un mensaje indicando si el ventilador esta encendido o apagado.'''
    if temperature > TEMP_THRESHOLD:
        print("El ventilador se ha encendido.")
    else:
        print("El ventilador se ha apagado.")

while True:
    #leer la temperatura
    current_temperature = read_temperature()

    #controlar el ventilador
    control_fan(current_temperature)

    #esperar 2 segundos antes de la siguiente medicion
    time.sleep(2)
'''Aplicación en la Vida Real
En un entorno real, reemplazarías la función read_temperature() con una lectura de un 
sensor de temperatura real, como un DHT11 o DHT22, y controlarías un ventilador físico
usando un pin GPIO del microcontrolador.'''

#-------------------------------------------------------------------------------

'''Para aplicar el código en la práctica con un microcontrolador y un sensor de temperatura real, como un DHT11 o DHT22, necesitarás hacer algunos ajustes al código y configurar el hardware. Aquí te guiaré paso a paso.'''

#requisitos previos:
#Microcontrolador: ESP32 o ESP8266
#Sensor de temperatura: DHT11 o DHT22
#Ventilador: cualquier ventilador controlado por un pin GPIO
#Cables de Conexión Para conectar los componentes al microcontrolador.

'''
Conexiones de Hardware 
Conecta el Sensor DHT:
Conecta el pin de datos del sensor DHT a un pin GPIO del microcontrolador (por ejemplo, GPIO 4).
Conecta el pin VCC del sensor a 3.3V o 5V en el microcontrolador.
Conecta el pin GND del sensor a GND en el microcontrolador.
2. Conecta el LED (Ventilador Simulado):
Conecta el ánodo del LED a otro pin GPIO (por ejemplo, GPIO 2).
Conecta el cátodo del LED a GND en el microcontrolador.'''


from machine import Pin
import dht
import time

# Configuración de sensor DHT 
dht_sensor = dht.DHT11(Pin(4)) #  # Cambia a DHT11 si es necesario

# Configuración del LED
led = Pin(2, Pin.OUT)

# Umbral de temperatura para encender el ventilador
TEMP_THRESHOLD = 25

while True:
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()

        # Controlar el LED basado en la temperatura
        if temperature > TEMP_THRESHOLD:
            led.on()
        else:
            led.off()

    except OSError as e:
        print("Error en la lectura del sensor DHT:", e)

        # Esperar 2 segundos antes de la siguiente lectura
        time.sleep(2)
