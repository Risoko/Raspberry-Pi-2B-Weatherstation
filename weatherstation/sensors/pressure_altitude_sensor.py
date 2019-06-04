from collections import namedtuple
import smbus as s
from time import sleep
from weatherstation.sensors.settings_sensors import SETTING_PRESSURE_ALTITUDE_SENSOR

measurement = namedtuple("measurement", "presurre, altitude")

def get_pressure_altitude(number_of_bus=SETTING_PRESSURE_ALTITUDE_SENSOR['BUS']):
    """Function returns tuple with data:
       (pressure (kPa), altitude (m)).
    """
    pressure, altitude = 0, None
    while True:
        bus = s.SMBus(number_of_bus)
        bus.write_byte_data(0x60, 0x26, 0xB9)
        bus.write_byte_data(0x60, 0x13, 0x07)
        bus.write_byte_data(0x60, 0x26, 0xB9)
        sleep(1)
        data = bus.read_i2c_block_data(0x60, 0x00, 6)
        tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
        altitude = tHeight / 16.0
        bus.write_byte_data(0x60, 0x26, 0x39)
        data = bus.read_i2c_block_data(0x60, 0x00, 4)
        sleep(1)
        pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
        pressure = (pres / 4.0) / 1000.0
        if pressure > 0 and altitude is not None:
            return measurement(round(pressure, 2), round(altitude, 2))

if __name__ == "__main__":
    print(get_pressure_altitude())



