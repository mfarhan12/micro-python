import pyb
import time

x_pin = pyb.ADC(0)
y_pin = pyb.ADC(1)

while True:
    x_val = x_pin.read()
    y_val = y_pin.read()

    if x_val > 3500:
        pyb.LED(1).on()
        pyb.LED(2).off()
    elif x_val < 500:
        pyb.LED(2).on()
        pyb.LED(1).off()
    else:
        pyb.LED(2).off()
        pyb.LED(1).off()

    if y_val > 3500:
        pyb.LED(3).on()
        pyb.LED(4).off()
    elif y_val < 500:
        pyb.LED(4).on()
        pyb.LED(3).off()
    else:
        pyb.LED(3).off()
        pyb.LED(4).off()
