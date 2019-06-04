from weatherstation.data_base.operation_on_table import *
from weatherstation.data_base.create_table import Measurements

def get_all_data():
    """Get all data in main table database."""
    date = (instances.date for instances in session.query(Measurements))
    max_temperature = (float(instances.max_temperature[:-2]) for instances in session.query(Measurements))
    min_temperature = (float(instances.min_temperature[:-2]) for instances in session.query(Measurements))
    min_humidity = (float(instances.min_humidity[:-1]) for instances in session.query(Measurements))
    max_humidity = (float(instances.max_humidity[:-1]) for instances in session.query(Measurements))
    min_pressure = (float(instances.min_pressure[:-3]) for instances in session.query(Measurements))
    max_pressure = (float(instances.max_pressure[:-3]) for instances in session.query(Measurements))
    min_light_instesity = (int(instances.min_light_instesity[:-1]) for instances in session.query(Measurements))
    max_light_instesity = (int(instances.max_light_instesity[:-1]) for instances in session.query(Measurements))
    average_height = (float(instances.average_height[:-1]) for instances in session.query(Measurements))
    average_amount_of_rainfall  = (float(instances.average_amount_of_rainfall[:-8]) for instances in session.query(Measurements))
    return [
        date,
        max_temperature, min_temperature, min_humidity, max_humidity,
        min_pressure, max_pressure, min_light_instesity, max_light_instesity,
        average_height, average_amount_of_rainfall
    ]

if __name__ == "__main__":
    print(get_all_data())



