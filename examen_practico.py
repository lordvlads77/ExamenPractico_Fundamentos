import RPi.GPIO as GPIO
import numpy as np

pin1 = 3
pin2 = 5
pin3 = 7
pin4 = 11
pin5 = 13
pin6 = 15
pin7 = 19
pin8 = 21

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin1, GPIO.OUT)
GPIO.output(pin1, GPIO.LOW)
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, GPIO.LOW)
GPIO.setup(pin3, GPIO.OUT)
GPIO.output(pin3, GPIO.LOW)
GPIO.setup(pin4, GPIO.OUT)
GPIO.output(pin4, GPIO.LOW)
GPIO.setup(pin5, GPIO.OUT)
GPIO.output(pin5, GPIO.LOW)
GPIO.setup(pin6, GPIO.OUT)
GPIO.output(pin3, GPIO.LOW)
GPIO.setup(pin7, GPIO.OUT)
GPIO.output(pin7, GPIO.LOW)
GPIO.setup(pin8, GPIO.OUT)
GPIO.output(pin8, GPIO.LOW)

num = int(input("Escriba el numero en base 10: \n"))
lista = []

while num >= 1:
    lista.insert(0, num % 2)
    num = num // 2

resultado = "".join(str(i) for i in lista)


print(resultado)

print("Escribe el resultado \n")

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
num7 = int(input())
num8 = int(input())

if num1 == 1:
    GPIO.output(pin1, GPIO.HIGH)
else:
    GPIO.output(pin1, GPIO.LOW)

if num2 == 1:
    GPIO.output(pin2, GPIO.HIGH)
else:
    GPIO.output(pin2, GPIO.LOW)

if num3 == 1:
    GPIO.output(pin3, GPIO.HIGH)
else:
    GPIO.output(pin3, GPIO.LOW)

if num4 == 1:
    GPIO.output(pin4, GPIO.HIGH)
else:
    GPIO.output(pin4, GPIO.LOW)

if num5 == 1:
    GPIO.output(pin5, GPIO.HIGH)
else:
    GPIO.output(pin5, GPIO.LOW)

if num6 == 1:
    GPIO.output(pin6, GPIO.HIGH)
else:
    GPIO.output(pin6, GPIO.LOW)

if num7 == 1:
    GPIO.output(pin7, GPIO.HIGH)
else:
    GPIO.output(pin7, GPIO.LOW)

if num8 == 1:
    GPIO.output(pin8, GPIO.HIGH)
else:
    GPIO.output(pin8, GPIO.LOW)
