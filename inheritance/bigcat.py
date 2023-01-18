from typing import List

class BigCat:
    def eats(self) -> List[str]:
        return ['rodents']


class Lion(BigCat):
    def eats(self) -> List[str]:
        return ['wildbest']

class Tiger(BigCat):
    def eats(self) -> List[str]:
        return super().eats() +  ['water buffalo']

class Liger(Lion, Tiger):
    def eats(self) -> List[str]:
        return super().eats() + ['rabbit','cow','pig','chicken']


def main():
    lion = Lion()
    print(f"The Lion eats {lion.eats()}")

    tiger = Tiger()
    print(f'The Tiger eats {tiger.eats()}')

    liger = Liger()
    print(f'The Liger eats {liger.eats()}')
    print(Liger.mro)

if __name__ == '__main__':
    main()