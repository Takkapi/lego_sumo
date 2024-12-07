from spike import MotorPair, ColorSensor, DistanceSensor
from spike.control import wait_for_seconds
from hub import port

import color_sensor
import runloop

motor_pair = MotorPair('A', 'B')
color_sensor_e = color_sensor.reflection(port.E) #ColorSensor('E')
color_sensor_f = color_sensor.reflection(port.F) #ColorSensor('F')
distance_sensor = DistanceSensor('D')

async def Move(Power, Steering):
    motor_pair(Power - Steering, Power + Steering)

async def main():
    while True:
        distance = distance_sensor.get_distance_cm()

        if color_sensor_e > 90 and color_sensor_f > 90:
            await Move(-75, 0)
            wait_for_seconds(.5)
        elif distance == None:
            await Move(100, 0)
        elif distance <= 50:
            await Move(100, 0)
        else: await Move(0, 20)

runloop.run(main())
