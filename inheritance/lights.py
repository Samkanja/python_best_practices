from abc import ABC, abstractmethod
from dataclasses import dataclass

class SwitchAble(ABC):

    @abstractmethod
    def turn_off(self) -> None:
        """Function to turn lights off"""

    @abstractmethod
    def turn_on(self):
        """Function to turn light on"""


class LightBulb(SwitchAble):
    def turn_off(self) -> str:
        print('LightBulb: turned off ...')

    def turn_on(self) -> str:
        print('LightBulb: turned on ...')


@dataclass
class ElectricPowerSwitch:
    status : SwitchAble
    on: False = None

    def press(self) -> None:
        if self.on:
            self.status.turn_off()
            self.on = False
        else:
            self.status.turn_on()
            self.on = True


switch = ElectricPowerSwitch(status=LightBulb())
switch.press()
switch.press()


