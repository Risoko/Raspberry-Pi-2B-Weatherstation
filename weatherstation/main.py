from random import randint
from time import sleep
from weatherstation.apache2.create_data_graphs import *
from weatherstation.data_base.connect_database import *
from weatherstation.data_base.create_table import * 
from weatherstation.data_base.operation_on_table import *
from weatherstation.main_settings import MAIN_SETTINGS
from weatherstation.sensors.photoresistor_sesnors import get_level_light
from weatherstation.sensors.liquid_level_sensor import get_water_level
from weatherstation.sensors.precipitation_sensor import get_occurrence_of_rain
from weatherstation.sensors.pressure_altitude_sensor import get_pressure_altitude
from weatherstation.sensors.real_time_sensor import get_time
from weatherstation.sensors.temperature_humidity_sensor import get_temperature_humidity

def main():
    """Function save data in database and create data on Apache serwer."""
    number_of_measurements = MAIN_SETTINGS["number_of_measurements"]
    main_id = 1
    break_time = MAIN_SETTINGS["break_time"]
    while True:
        id = 0
        for _ in range(number_of_measurements):
            humidity, temperature = get_temperature_humidity()
            pressure, altitude = get_pressure_altitude()
            occurence_of_rain = get_occurrence_of_rain()
            light_instesity = get_level_light()
            amount_of_rainfall = get_water_level()
            date = get_time()
            insert_value(table_name=Temperature, id=id, date=date, temperature=temperature)
            insert_value(table_name=Humidity, id=id, date=date, humidity=humidity)
            insert_value(table_name=AirPressure, id=id, date=date, air_pressure=pressure)
            insert_value(table_name=Height, id=id, date=date, height=altitude)
            insert_value(table_name=RainFall, id=id, date=date, precipitation=occurence_of_rain, amount_of_rainfall=amount_of_rainfall)
            insert_value(table_name=LightInstesity, id=id, date=date, light_instesity=light_instesity)
            id += 1
            sleep(break_time)
        date = get_time()
        min_temperature = str(get_min_column(Temperature.temperature)) + " " + '℃'
        max_temperature = str(get_max_column(Temperature.temperature)) + " " + '℃'
        min_humidity = str(get_min_column(Humidity.humidity)) + " " + '%'
        max_humidity = str(get_max_column(Humidity.humidity)) + " " + '%'
        min_pressure = str(get_min_column(AirPressure.air_pressure)) + " " + 'kPa'
        max_pressure = str(get_max_column(AirPressure.air_pressure)) + " " + 'kPa'
        min_light_instesity = str(get_min_column(LightInstesity.light_instesity)) + " " + '%'
        max_light_instesity = str(get_max_column(LightInstesity.light_instesity)) + " " + '%'
        average_height = str(get_avg_column(Height.height)) + " " + 'm'
        max_amount_of_rainfall = get_max_column(RainFall.amount_of_rainfall)
        if max_amount_of_rainfall > 0 and session.query(func.count(RainFall.id).filter(RainFall.precipitation == True)).scalar() != 0:
            precipitation = True
            max_amount_of_rainfall = str(max_amount_of_rainfall) + " " + 'l / cm^3'
            average_amount_of_rainfall = str(get_avg_column(RainFall.amount_of_rainfall)) + " " + 'l / cm^3'
        else:
            precipitation = False
            max_amount_of_rainfall = str(0) + " " + 'l / cm^3'
            average_amount_of_rainfall = str(0) + " " + 'l / cm^3'
        insert_value(table_name=Measurements, id=main_id, date=date, min_temperature=min_temperature, max_temperature=max_temperature,
                     min_humidity=min_humidity, max_humidity=max_humidity, min_pressure=min_pressure, max_pressure=max_pressure,
                     min_light_instesity=min_light_instesity, max_light_instesity=max_light_instesity, average_height=average_height,
                     max_amount_of_rainfall=max_amount_of_rainfall, precipitation=precipitation, 
                     average_amount_of_rainfall=average_amount_of_rainfall)
        clear_table(TEMPORARYTABLES)
        main_id += 1
        create_graphs()
main()



