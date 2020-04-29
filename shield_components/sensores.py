#!/user/bin/python
import spidev
import time
import os

#Abrimos el bus SPI
spi = spidev.SpiDev()#declaramos el objeto 
spi.open(0,0)#SPIO
spi.max_speed_hz= 1000000#declaramos la velocidad de trasnmision 1Mhz

#Funcion para leer los datos por el protocolo SPI del chip MCP3008
#El integrado tiene 8 canales para el ingreso de la señal. Pero para fines del programa
# el valor del canal de ser un entero 0-7

def leerCanal(canal):#recuerda que hablamos del canal del integrado
    adc = spi.xfer2([1, (8+canal)<<4,0]) 
    data = ((adc[1]&3) << 8) + adc[2]
    return data

#Definimos el valor del canal de los sensores
flex1 = 0


#Definimos el tiempo de retardo entre lectura de los datos
delay = 0.25



def obtenerSenial():
    #leemos el valor del ejex
    sensor_uno = leerCanal(flex1)
    return sensor_uno 