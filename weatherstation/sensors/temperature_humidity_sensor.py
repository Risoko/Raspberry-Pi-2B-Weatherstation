from Adafruit_DHT import DHT22, read_retry 
from collections import namedtuple
from weatherstation.sensors.settings_sensors import SETTING_TEMPERATURE_HUMIDITY_SENSOR

measurement = namedtuple("measurement", "humidity, temperature")

def get_temperature_humidity(PIN=SETTING_TEMPERATURE_HUMIDITY_SENSOR['PIN']):
    """Function, return tuple with data:
       (humidity (%), temperature (C)).
    """
    humidity, temperature = None, None
    while True:
        humidity, temperature = read_retry(DHT22, PIN)
        if humidity is not None and temperature is not None:
            return measurement(round(humidity, 2), round(temperature, 2))
        
if __name__ == "__main__":
    print(get_temperature_humidity())