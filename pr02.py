from abc import ABCMeta, abstractmethod

class AbstractOperation(metaclass = ABCMeta):

    def __init__(self, operand_A, operand_B):

        self.operand_A = operand_A
        self.operand_B = operand_B
        super().__init__()

    @abstractmethod
    def execute(self):
        pass

class AddOperation(AbstractOperation):

    def execute(self):
        print(self.operand_A + self.operand_B)

class MultiplyOperation(AbstractOperation):

    def execute(self):
        print(self.operand_A * self.operand_B)


ope1 = AddOperation(1, 2)
ope1.execute()
ope2 = MultiplyOperation(2, 2)
ope2.execute()
