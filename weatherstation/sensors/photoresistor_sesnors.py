from time import sleep
from wiringpi import digitalRead, digitalWrite, INPUT, LOW, OUTPUT, pinMode, wiringPiSetupGpio
from weatherstation.sensors.settings_sensors import SETTING_PHOTORESISTOR_SENSOR 

wiringPiSetupGpio() 

def get_level_light(PRpin=SETTING_PHOTORESISTOR_SENSOR['PIN']):
    """Returns the level of light exposure in %."""
    reading = 0
    pinMode(PRpin, OUTPUT)
    digitalWrite(PRpin, LOW)
    sleep(0.1)
    pinMode(PRpin, INPUT)
    while digitalRead(PRpin) == LOW:
            reading += 1
    return 100 - int(reading / 50)

if __name__ == "__main__":
    print(get_level_light())