import operator
import math
import random
print("---------menu----------")
print("press 1 for solve math question:\npress 2 for solve later:")
choice=int(input("enter choice:"))
ch=0
if choice==1:
    n=int(input("how many solve the question"))
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    for i in range(n):
        number1 = random.randint(1, 20)
        number2 = random.randint(10, 20)
        operator, func = random.choice(operators)
        result = func(number1, number2)
        print(f"{number1} {operator} {number2}")
        results=int(input("enter answer="))
        if(results==result):
            print("corect answer continue...")
            ch=ch+1
        else:
            print("try next time that question") 
            ch=ch-1
    print(ch)
if choice==2:
    print("exit")