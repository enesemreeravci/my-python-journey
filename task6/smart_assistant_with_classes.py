#!/usr/bin/env python3

class Device:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.status = 0

    def get_status(self):
        if self.status == 0:
            print("OFF")
        elif self.status == 1:
            print("ON")

    def turn_on(self):
        self.status = 1
        print(f"{self.name} is now ON")

    def turn_off(self):
        self.status = 0
        print(f"{self.name} is now OFF")


class Light(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.brightness = 100
        self.color = "white"

    def set_brightness(self, value_of_brightness):
        if 0 <= value_of_brightness <= 100:
            self.brightness = value_of_brightness
            print(f"{self.name} brightness set to {value_of_brightness}")
        else:
            print("Value range must be between 0 and 100")

    def set_color(self, new_color):
        self.color = new_color
        print(f"{self.name} color's set to ", new_color)


class Thermostat(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.temperature = 25

    def set_temperature(self, temp):
        if 15 <= temp <= 30:
            self.temperature = temp
            print(f"{self.name} temperature set to {temp}°C")


class SecurityCamera(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.recording = False
        self.resolution = "1080p"

    def start_recording(self):
        self.recording = True
        print(f"{self.name} started recording")

    def stop_recording(self):
        self.recording = False
        print(f"{self.name} stopped recording")

    def set_resolution(self, new_resolution):
        self.resolution = new_resolution
        print(f"{self.name} resolution set to {new_resolution}")

    def turn_on(self):
        super().turn_on()
        self.start_recording()

    def turn_off(self):
        super().turn_off()
        self.stop_recording()


class SmartDoor(Device):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.locked = True
        self.__security_code = 1234

    def lock(self):
        self.locked = True
        print(f"{self.name} is locked")

    def unlock(self, code):
        if code == self.__security_code:
            self.locked = False
            print(f"{self.name} is unlocked")
        else:
            print("Incorrect security code")

    def change_code(self, old_code, new_code):
        if old_code == self.__security_code:
            self.__security_code = new_code
            print("Success")
        else:
            print("Old code is incorrect, code not changed")


class HomeAutomationSystem:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"{device.name} is added")

    def find_device_by_name(self, device_name):
        for device in self.devices:
            if device.name == device_name:
                return device
        return None

    def turn_on_device(self, name):
        device = self.find_device_by_name(name)
        if device is not None:
            device.turn_on()
        else:
            print("Device not found")

    def turn_off_device(self, name):
        device = self.find_device_by_name(name)
        if device is not None:
            device.turn_off()
        else:
            print("Device not found")

    def remove_device(self, name):
        device = self.find_device_by_name(name)
        if device is not None:
            self.devices.remove(device)
            print(f"{device.name} is removed")
        else:
            print("device not found")

    def list_devices(self):
        if len(self.devices) == 0:
            print("No devices found")
            return
        for device in self.devices:
            device_type = type(device).__name__
            print(f"{device.name} ({device_type}) in {device.location}")

    def turn_on_all(self):
        if len(self.devices) == 0:
            print("No devices found")
        else:
            for device in self.devices:
                device.turn_on()

    def turn_off_all(self):
        if len(self.devices) == 0:
            print("No devices found")
        else:
            for device in self.devices:
                device.turn_off()

    def night_mode(self):
        if len(self.devices) == 0:
            print("No devices found")
        else:
            for device in self.devices:
                if isinstance(device, Light):
                    device.turn_off()
                elif isinstance(device, SmartDoor):
                    device.lock()
                elif isinstance(device, SecurityCamera):
                    device.turn_on()
        print("Night mode activated.")

    def vacation_mode(self):
        if len(self.devices) == 0:
            print("No devices  found")
        else:
            for device in self.devices:
                if isinstance(device, Light):
                    device.turn_off()
                elif isinstance(device, SmartDoor):
                    device.lock()
                elif isinstance(device, SecurityCamera):
                    device.turn_on()
        print("Vacation mode activated")


if __name__ == "__main__":
    system = HomeAutomationSystem()

# for testing
#     # Create devices
#     light1 = Light("Living Room Light", "Living Room")
#     thermo1 = Thermostat("Bedroom Thermostat", "Bedroom")
#     cam1 = SecurityCamera("Entrance Camera", "Entrance")
#     door1 = SmartDoor("Front Door", "Entrance")

#     # Add devices to the system
#     system.add_device(light1)
#     system.add_device(thermo1)
#     system.add_device(cam1)
#     system.add_device(door1)

#     # List all devices
#     system.list_devices()

#     # Control individual devices
#     system.turn_on_device("Living Room Light")
#     system.turn_off_device("Bedroom Thermostat")

#     # Turn all devices ON / OFF
#     system.turn_on_all()
#     system.turn_off_all()

#     # Modes
#     system.night_mode()
#     system.vacation_mode()

while True:
    print("\nWelcome to the Smart Home Automation System!")
    print("1. List all devices")
    print("2. Add a new device")
    print("3. Remove a device")
    print("4. Turn on a device")
    print("5. Turn off a device")
    print("6. Set mode (Night Mode / Vacation Mode)")
    print("7. Exit\n")

    user_choice = int(input("Choose an option: "))

    if user_choice == 1:
        system.list_devices()

    elif user_choice == 2:
        print("\nWhich device do you want to add?")
        print("1. Light")
        print("2. Thermostat")
        print("3. Security Camera")
        print("4. Smart Door")

        device_type = int(input("Choose device type: "))

        name = input("Enter device name: ")
        location = input("Enter device location: ")

        if device_type == 1:
            system.add_device(Light(name, location))
        elif device_type == 2:
            system.add_device(Thermostat(name, location))
        elif device_type == 3:
            system.add_device(SecurityCamera(name, location))
        elif device_type == 4:
            system.add_device(SmartDoor(name, location))
        else:
            print("Invalid device type.")

    elif user_choice == 3:
        name = input("Enter the name of the device to remove: ")
        system.remove_device(name)

    elif user_choice == 4:
        name = input("Enter device name to turn on: ")
        system.turn_on_device(name)

    elif user_choice == 5:
        name = input("Enter device name to turn off: ")
        system.turn_off_device(name)

    elif user_choice == 6:
        mode = input("Enter mode (Night Mode / Vacation Mode): ")
        if mode.lower() == "night mode":
            system.night_mode()
        elif mode.lower() == "vacation mode":
            system.vacation_mode()
        else:
            print("Invalid mode.")

    elif user_choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid option, please enter digit between 1-7 !!!.")
