from wiringpi import digitalRead, INPUT, pinMode, wiringPiSetupGpio
from weatherstation.sensors.settings_sensors import SETTING_PRECIPTION_SENSOR

wiringPiSetupGpio()

def get_occurrence_of_rain(PIN=SETTING_PRECIPTION_SENSOR['PIN'], number_of_checks=SETTING_PRECIPTION_SENSOR['number_check']):
    """Function will be true if there is a rainfall else False"""
    pinMode(PIN, INPUT)
    for _ in range(number_of_checks):
        if digitalRead(PIN) == 0:
            return True
    return False
        
if __name__ == "__main__":
    print(get_occurrence_of_rain())
    
    

