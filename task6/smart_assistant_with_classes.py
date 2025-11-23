
class Device:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.status = 0

    def get_status(self):
        i f(self.status == 0):
            print("OFF")
        eli f(self.status == 1):
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
        i f(value_of_brightness >= 0 and value_of_brightness <= 100):
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
            print(f"{self.name} tempreture set to {temp}°C")

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
        i f(code == self.__security_code):
            self.locked = False
            print(f"{self.name} is unlocked")
        else:
            print("Incorrect security code")

    def change_code(self, old_code, new_code):
        i f(old_code == self.__security_code):
            self.__security_code = new_code
            print("Success")
        else:
            print("Old code is incorrect, code not changed")

class HomeAutomationSystem:
    pass