from abc import ABC,abstractmethod
from dataclasses import dataclass

class Tire(ABC):

    @abstractmethod
    def __repr__(self) -> str:
        pass


class RubberTire(Tire):
    def __repr__(self) -> str:
        return 'A rubber tire'
    
class FancyTire(Tire):
    def __repr__(self) -> str:
        return 'A fancy tire'
        

class Frame:
    def __repr__(self) -> str:
        return 'A bicycle frame'

class AluminumFrame(Frame):
    def __repr__(self) -> str:

        return 'An aluminum frame'

@dataclass
class Bicycle:
    front_tire : Tire
    back_tire: Tire
    frame: Frame

    def display(self) -> str:
        print(f'Frame:{self.frame} front_tire: {self.front_tire} back_tire: {self.back_tire}')


bike = Bicycle(front_tire=FancyTire(),back_tire=RubberTire(),frame=Frame())
bike.display()