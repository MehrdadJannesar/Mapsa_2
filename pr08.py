from abc import ABCMeta, abstractmethod

#AbstractFactory
class CoffeeFactory(metaclass = ABCMeta):

    @abstractmethod
    def createCoffeeWithOutMilk(self):
        pass
    @abstractmethod
    def createCoffeeWithMilk(self):
        pass

#ConcreteFactory
class ItalianCoffeeFactory(CoffeeFactory):

    def createCoffeeWithOutMilk(self):
        return ItalianEspresso()

    def createCoffeeWithMilk(self):
        return ItalianCappucino()

class FrenchCoffeeFactory(CoffeeFactory):

    def createCoffeeWithOutMilk(self):
        return FrencheEspresso()

    def createCoffeeWithMilk(self):
        return FrenchCappocino()

#AbstractProduct
class CoffeeWithOutMilk(metaclass = ABCMeta):

    @abstractmethod
    def prepare(self, CoffeeWithOutMilk):
        pass

class CoffeeWithMilk(metaclass = ABCMeta):

    @abstractmethod
    def serve(self, CoffeeWithOutMilk):
        pass

#ConcreteProduct

class ItalianEspresso(CoffeeWithOutMilk):

    def prepare(self):
        print("prepare ", type(self).__name__)

class ItalianCappucino(CoffeeWithMilk):

    def serve(self, CoffeeWithOutMilk):
        print(type(self).__name__, " is served with sheep's milk on ", type(CoffeeWithOutMilk).__name__)

class FrencheEspresso(CoffeeWithOutMilk):

    def prepare(self):
        print("prepare ", type(self).__name__)

class FrenchCappocino(CoffeeWithMilk):

    def serve(self, CoffeeWithOutMilk):
        print(type(self).__name__, " is served with cow's milk on ", type(CoffeeWithOutMilk).__name__)

#Client

class CoffeeStore:

    def __init__(self):
        pass

    def makeCoffee(self):

        for factory in [ItalianCoffeeFactory(), FrenchCoffeeFactory()]:

            self.factory = factory
            self.CoffeeWithOutMilk = self.factory.createCoffeeWithOutMilk()
            self.CoffeeWithMilk = self.factory.createCoffeeWithMilk()
            self.CoffeeWithOutMilk.prepare()
            self.CoffeeWithMilk.serve(self.CoffeeWithOutMilk)

coffee = CoffeeStore()
coffee.makeCoffee()
