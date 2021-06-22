# just Math fun for python

class Math:
    def __init__(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def sum(self):
        Sum = int(self.numOne) + int(self.numTwo)
        print(f'Sum is: {Sum}')

    def miu(self):
        Miu = int(self.numOne) - int(self.numTwo)
        print(f'Minus is: {Miu}')

    def multipy(self):
        Mul = int(self.numOne) * int(self.numTwo)
        print(f'Multipy is: {Mul}')

    def divided(self):
        Div = int(self.numOne) / int(self.numTwo)
        print(f'Divid is: {Div}')

mathTest = Math(20,30)

mathTest.sum()
mathTest.multipy()
mathTest.divided()
mathTest.miu()