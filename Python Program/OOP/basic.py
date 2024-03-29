class Demo: 

    #Constructor
    def __init__(self,x,y):
        self.num1 = x
        self.num2 = y

    #Attributes / Variables / State
    num1=0
    num2=0

    #User-Define Function / Methods / Behaviour
    def Info(self):
        print(self.num1,self.num2)

    def add(self):
        print("The Sum is",self.num1+self.num2)
    
    
    def sub(self):
        print("The Differ is",self.num1-self.num2)
    
    
    def multi(self):
        print("The Prodt is",self.num1*self.num2)
    
    
    def Div(self):
        print("The Quot is",self.num1/self.num2)
    
    
    def rem(self):
        print("The rem is",self.num1%self.num2)

class Test:
    calc = Demo(10,5)
    calc.add()
    calc.sub()
    calc.multi()
    calc.Div()
    calc.rem()

    print("x =",calc.num1)
    print("y =",calc.num2)
