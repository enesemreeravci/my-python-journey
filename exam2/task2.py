from functools import reduce

def analyze_energy(sensor_data):
    threshold = 1000

    energy_values = list(map(lambda x: x["energy_usage_kWh"], sensor_data))
    min_energy = min(energy_values)
    max_energy = max(energy_values)

    def normalize(value):
        if max_energy - min_energy == 0:
            return 0
        return (value - min_energy) / (max_energy - min_energy)

    high_energy_locations = list(
        map(
            lambda x: x["location"],
            filter(lambda x: x["energy_usage_kWh"] > threshold, sensor_data)
        )
    )

    total_energy = reduce(
        lambda total, x: total + x["energy_usage_kWh"],
        sensor_data,
        0
    )

    average_energy = total_energy / len(sensor_data)

    return high_energy_locations, average_energy


def main():
    sensor_data = [
        {"location": "Downtown", "energy_usage_kWh": 1200, "time_of_day": "Night"},
        {"location": "Suburb", "energy_usage_kWh": 800, "time_of_day": "Evening"},
        {"location": "Industrial Area", "energy_usage_kWh": 1500, "time_of_day": "Day"},
        {"location": "Park", "energy_usage_kWh": 300, "time_of_day": "Afternoon"}
    ]

    high_locations, avg_energy = analyze_energy(sensor_data)

    print("Locations with high energy consumption:", high_locations)
    print("Average energy usage:", int(avg_energy), "kWh")


if __name__ == "__main__":
    main()
