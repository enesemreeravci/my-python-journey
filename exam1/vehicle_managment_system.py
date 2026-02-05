


class Vehicle:
    def __init__(self, name, vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type
        self.status = "off"
        self.__fuel_level = 0   # private attribute (encapsulation)
        # to make it private 2 underscore

    #getter
    def get_fuel_level(self):
        return self.__fuel_level

    # setter with validation
    def set_fuel_level(self, value):
        if 0 <= value <= 100:
            self.__fuel_level = value
        else:
            print("Fuel level must be between 0 and 100.")

    def activate(self):
        self.status = "on"

    def deactivate(self):
        self.status = "off"

    def refuel(self):
        pass

class Car(Vehicle):
    def __init__(self, name, trunk_capacity):
        super().__init__(name, "Car")
        self.trunk_capacity = trunk_capacity

    def refuel(self):
        new_level = self.get_fuel_level() + 20
        if new_level > 100:
            new_level = 100
        self.set_fuel_level(new_level)

class Motorcycle(Vehicle):
    def __init__(self, name, helmet_available):
        super().__init__(name, "Motorcycle")
        self.helmet_available = helmet_available

    def refuel(self):
        new_level = self.get_fuel_level() + 15
        if new_level > 100:
            new_level = 100
        self.set_fuel_level(new_level)

class Truck(Vehicle):
    def __init__(self, name, cargo_capacity):
        super().__init__(name, "Truck")
        self.cargo_capacity = cargo_capacity

    def refuel(self):
        new_level = self.get_fuel_level() + 30
        if new_level > 100:
            new_level = 100
        self.set_fuel_level(new_level)

class FleetManagement:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, name):
        for vehicle in self.vehicles:
            if vehicle.name == name:
                self.vehicles.remove(vehicle)
                return
        print("Vehicle not found.")

    def display_all_vehicles(self):
        if not self.vehicles:
            print("No vehicles registered.")
            return
        for v in self.vehicles:
            print(f"{v.name} | {v.vehicle_type} | Status: {v.status} | Fuel: {v.get_fuel_level()}%")

    def activate_all(self):
        for v in self.vehicles:
            v.activate()

    def deactivate_all(self):
        for v in self.vehicles:
            v.deactivate()

def main():
    fleet = FleetManagement()

    while True:
        print("\n--- Fleet Management Menu ---")
        print("1. Add Car")
        print("2. Add Motorcycle")
        print("3. Add Truck")
        print("4. Display all vehicles")
        print("5. Refuel all vehicles")
        print("6. Activate all vehicles")
        print("7. Deactivate all vehicles")
        print("8. Remove vehicle")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Car name: ")
            trunk = int(input("Trunk capacity: "))
            fleet.add_vehicle(Car(name, trunk))

        elif choice == "2":
            name = input("Motorcycle name: ")
            helmet = input("Helmet available (yes/no): ").lower() == "yes"
            fleet.add_vehicle(Motorcycle(name, helmet))

        elif choice == "3":
            name = input("Truck name: ")
            cargo = int(input("Cargo capacity: "))
            fleet.add_vehicle(Truck(name, cargo))

        elif choice == "4":
            fleet.display_all_vehicles()

        elif choice == "5":
            for v in fleet.vehicles:
                v.refuel()

        elif choice == "6":
            fleet.activate_all()

        elif choice == "7":
            fleet.deactivate_all()

        elif choice == "8":
            name = input("Enter vehicle name to remove: ")
            fleet.remove_vehicle(name)

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
