from abc import ABC , abstractmethod

class Predator(ABC):

    @abstractmethod
    def eat(self, prey) -> str:
        """Return the prey the predators eats"""


class Bear(Predator):
    def eat(self, prey) -> str:
        print(f'Mauling a {prey}')

    @abstractmethod
    def roar(self):
        print('roar')


class Owl(Predator):
    def eat(self, prey) -> str:
        print(f'Swooping in on {prey}')


class Chameleon(Predator):
    def eat(self, prey) -> str:
        print(f'Shooting it tongue at {prey}')


def main():
    bear = Bear()
    bear.eat('deer')
    bear.roar()

    owl = Owl()
    owl.eat('mouse')

    chameleon = Chameleon()
    chameleon.eat('fly')


if __name__ == '__main__':
    main()