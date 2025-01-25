from my_operations import add, diff, mul
from greeting_a import greeting_a
from greeting_b import greeting_b
from greeting_c import greeting_c
def main():

    num1 = int(input("Enter your number 1:"))
    num2 = int(input("Enter your number 2:"))
    
<<<<<<< HEAD
    add(num1, num2)
    diff(num1, num2)
=======
    mul(num1, num2)
    add(num1, num2) # hahahaha
>>>>>>> 106de71ef4dcf8deb7288bc813f2567ca068f8d5

    # Member A call method add() at line: 8
    # Member B call method diff() at line: 8
    # Member C call method mul() at line: 8
    
    pass

if __name__ == "__main__":
    main()