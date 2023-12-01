from servo import Servo
from machine import ADC, Pin
import time

# configure servo on pin G7:
servo = Servo(pin=7)

# configure ADC input on pin G1 with 11dB attenuation:
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)

# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
    v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
    if v < out_min: 
        v = out_min 
    elif v > out_max: 
        v = out_max
    return int(v)

# Fixed position for the servo when ADC value is above 1000
fixed_position = 90  # This can be adjusted to a desired 'rest' position

while True:
    # read 12-bit analog value (0 - 4095 range):
    adc_val = adc.read()
    
    if adc_val < 1000:
        # Convert adc_val to 90 - 150 range for servo movement:
        servo_val = map_value(adc_val, in_min=0, in_max=1000, out_min=90, out_max=150)
        print(f"ADC Value: {adc_val} => Servo Value: {servo_val}")
        servo.move(servo_val)
        time.sleep(0.5)  # Move servo for 2 seconds
    else:
        # ADC value greater than 1000, hold servo at a fixed position
        print(f"ADC Value: {adc_val} - Holding Servo at Position {fixed_position}")
        servo.move(fixed_position)
        time.sleep(0.1)  # Small delay to reduce CPU usage

