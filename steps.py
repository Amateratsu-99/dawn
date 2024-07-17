from abc import ABC,abstractmethod

class build(ABC):
    @abstractmethod

    def process(self):
        pass

class construct(build):

    def process(self):
        for i in range(5):
            print("ive done it")

a1=construct()
a1.process()