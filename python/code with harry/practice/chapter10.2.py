# 2. Write a class “Calculator” 
# capable of finding square, cube and square root
#  of a number. 

class Calculator:
    a="thanku"
    @staticmethod
    def square(n):
        print("the square is ",n*n)
        print(Calculator.a)

    @staticmethod
    def cube(n):
        print("the cube is ",n*n*n)
        print(Calculator.a)

    @staticmethod
    def squareRoot(n):
        print("the squareroot is ",n**0.5)
        print(Calculator.a)
        

Calculator.square(9)
Calculator.cube(9)
Calculator.squareRoot(9)
        
