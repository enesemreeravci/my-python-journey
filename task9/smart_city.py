import functools
from functools import reduce

sensor_data = [
    {"location": "Area A", "energy_consumption": 120.5, "status": "active"},
    {"location": "Area B", "energy_consumption": 98.3, "status": "active"},
    {"location": "Area C", "energy_consumption": 0.0, "status": "faulty"},
    {"location": "Area D", "energy_consumption": 76.2, "status": "active"},
    {"location": "Area E", "energy_consumption": 0.0, "status": "inactive"},
]

# go through the sensor_data list and if status is active it will return a new list
def filter_sensors():
   filtered_data = filter(lambda sensor : sensor["status"] == "active" , sensor_data)
   active_sensors = list(filtered_data)
   return active_sensors
# store value of consumption(new values divided by 100) with new list and return
def normalize_energy_consumption(active_sensors):
    normalized_data = map(lambda sensor : sensor["energy_consumption"] / 100, active_sensors)
    result = list(normalized_data)
    return result

def total_energy_consumption(active_sensors):
    values = map(lambda sensor : sensor["energy_consumption"], active_sensors)
    total = functools.reduce(lambda a, b: a+b, values)
    return total

def identify_high_energy_areas(active_sensors, limit):
    filtered = filter(lambda sensor : sensor["energy_consumption"] / 100 >= limit, active_sensors)
    location = map(lambda sensor: sensor["location"], filtered)
    result = list(location)
    return result

def main():
    active = filter_sensors()
    normalized = normalize_energy_consumption(active)
    total = total_energy_consumption(active)
    high = identify_high_energy_areas(active, 0.80)
    print("Filtered data:", active)
    print("Normalized data:", normalized)
    print("Total energy consumption:", total, "kWh")
    print("High energy areas:", high)

if __name__ == "__main__":
    main()


