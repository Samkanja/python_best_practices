class Slug:
    def __init__(self,name) -> None:
        self.name = name
    
    def crawl(self):
        print(f'slime trail {self.name}')


class Snail(Slug):
    def __init__(self, name,shell_size) -> None:
        super().__init__(name)
        self.shell_size = shell_size


def race(first, second):
    first.crawl()
    second.crawl()

race(Slug('kanja'),Snail('samuel','new'))
