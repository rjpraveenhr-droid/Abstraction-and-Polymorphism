
from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute_command(self):
        pass


class SmartLight(SmartDevice):
    def execute_command(self):
         print(self.name, "is turning on the light.")

class SmartFan(SmartDevice):
     def execute_command(self):
         print(self.name, "is turning on the fan.")

class SmartSpeaker(SmartDevice):
     def execute_command(self):
         print(self.name, "is playing music.")

class SmartAC(SmartDevice):
     def execute_command(self):
         print(self.name, "is cooling the room.")

devices = [
    SmartLight("Living Room Light"),
    SmartFan("Bedroom Fan"),
    SmartSpeaker("Smart Speaker"),
    SmartAC("{Air Conditioner}")
]

print("Smart Device Command Center")

for device in devices:
    device.execute_command()


         