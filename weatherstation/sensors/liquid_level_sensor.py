import smbus as s
from weatherstation.sensors.settings_sensors import SETTING_LIQUID_LVL_SENSOR

def get_water_level(number_of_bus=SETTING_LIQUID_LVL_SENSOR['BUS']):
    """Returns the water level in cm."""
    analog = SETTING_LIQUID_LVL_SENSOR['ANALOG']
    address = 0x48
    level_water = None
    bus = s.SMBus(number_of_bus)
    while True:
        bus.write_byte(address, analog)
        value = bus.read_byte(address)
        vout = round(value * 3.3 / 255, 2)
        if vout >= 0 and vout < 1.3:
            value = 0
        elif vout >= 1.30 and vout < 1.63:
            value = 0.5
        elif vout >= 1.63 and vout < 1.69:
            value = 1
        elif vout >= 1.69 and vout < 1.99:
            value = 1.5
        elif vout >= 1.99 and vout < 2.04:
            value = 2
        elif vout >= 2.04 and vout < 2.07:
            value = 2.5
        elif vout >= 2.07 and vout < 2.11:
            value =  3
        elif vout >= 2.11 and vout < 2.14:
            value = 3.5
        elif vout >= 2.14 and vout < 2.16:
            value = 4
        elif vout >= 2.16 and vout < 2.18:
            value = 4.5
        elif vout >= 2.18:
            value = 4.8
        return ((value * 600) / 6) * 0.0002
        
if __name__ == "__main__":
    print(get_water_level())
        
        
        
