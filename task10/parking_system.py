#!/usr/bin/env python3

park_lot1 = [0, 1, 0, 0, 1]
park_lot2 = [1, 1, 1, 1, 0]

park_city1 = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 0, 1]
]

# to store stats of parking
daily_list = []

# check if lot is free or if so print messages
def check_availability(parking_lot, index):
    if parking_lot[index] == 0:
        print("Slot is vacant")
    if parking_lot[index] == 1:
        print("Slot is occupied")

# check if slot is not taken(0) then replace with 1(taken) - change the state
# if slot is full print message
def park_a_vehicle(parking_lot):
    for index in range(len(parking_lot)):
        if parking_lot[index] == 0:
            parking_lot[index] = 1
            return
    print("Parking lot is full")


def calculate_occupancy_rate(parking_lot):
    total_slot = len(parking_lot) # stores length of list
    count = 0 # stores occupied slots

    for i in parking_lot:
        if i == 1:
            count += 1
    rate = (count / total_slot) * 100 # it will calculate the rate of occupancy by using simple math :)
    return rate

def find_least_occupied_lot(parking_city):
    lowest_rate = 100
    least_occupied_index = 0

    for i in range(len(parking_city)):
        rate = calculate_occupancy_rate(parking_city[i])
        if rate < lowest_rate:
            lowest_rate = rate
            least_occupied_index = i
    return least_occupied_index

def get_one_day_record(parking_city):
    today_temp_list = []

    for row in range(len(parking_city)): # loop over parking lots
        count = 0
        for col in range(len(parking_city[row])): # loop over slots in this slot
            if parking_city[row][col] == 1:
                count += 1
        today_temp_list.append(count)

    daily_list.append(today_temp_list)
    return daily_list

def main():
    print("Initial Parking City:")
    for i in range(len(park_city1)):
        print(f"Parking Lot {i + 1}: {park_city1[i]}")
    print()
    # check availability of a specific slot
    check_availability(park_city1[0], 1)
    print()
    # Park a vehicle in the least occupied lot
    least = find_least_occupied_lot(park_city1)
    park_a_vehicle(park_city1[least])
    print("After Parking One Vehicle:")
    for i in range(len(park_city1)):
        print(f"Parking Lot {i + 1}: {park_city1[i]}")
    print()
    # Show occupancy rates
    print("Occupancy Rates:")
    for i in range(len(park_city1)):
        rate = calculate_occupancy_rate(park_city1[i])
        print(f"Lot {i + 1}: {rate:.0f}% occupied")
    print()
    # End-of-day record
    get_one_day_record(park_city1)
    print("Daily Parking Statistics:")
    print(daily_list)


if __name__ == "__main__":
    main()
