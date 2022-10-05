import math 
import random
random.random()


def variables():
    variables = ('I','S','H','T','y','ish1','ish2','signs','symbols','t1','t2','x')
    return variables

def Response_random(total):
    I = ["No, Please try again","Wrong. Try Once more.","No. Keep trying."]
    S = ["Very Good!","Nice work!","Keep up the good work!"]
    if total == False:
        return I[random.randint(0,2)]
    elif total == True:
        return S[random.randint(0,2)]
    
def mainOperation():
    S = ["Very Good!","Nice work!","Keep up the good work!"]
    I = ["No, Please try again","Wrong. Try Once more.","No. Keep trying."]
    x = int(input("Enter Difficulty level(1 or 2): "))
    H = 0
    T = 0
    
    ish1 = print("1 = addition ")
    print("2 = subtraction ")
    print("3 = multiplication ")
    print("4 = Division ")
    print("5 = mixed operations ")
                 
    ish2 = int(input("Enter the operation(1 to 5): "))

    while True:
        if x == 1:
            t1 = random.randint(0,9)
            t2 = random.randint(0,9)
            if ish2 == 4 and t2 == 0:
                t2 = 1
        elif x == 2:
            t1 = random.randint(0,99)
            t2 = random.randint(0,99)
        if ish2 == 1:
            signs = "+"
        elif ish2 == 2:
            if t1<t2:
                t1,t2 = t2,t1
            signs = "-"
        elif ish2 == 3:
            signs = "*"
        elif ish2 == 4:
            signs = "//"
        elif ish2 == 5:
            ish2 = random.randint(1,4)
            symbols = ["+","-","*","//"]
            signs = symbols[ish2 - 1]
            if ish2 == 2:
                if t1<t2:
                    t1,t2 = t2,t1
        print("How much is ", t1, signs, t2)
        
        if ish2 == 1:
            while True:
                y = int(input("Enter your answer (-1 to exit): "))
                if y == t1 + t2:
                    print(Response_random(True))
                    H += 1
                    break
                elif y == -1:
                    print("Number of Correct Answers: ", H)
                    print("Number of wrong answers: ", T)
                    print("Thanks for playing!")
                    return
                elif y != t1 + t2:
                    print(Response_random(False))
                    T += 1
                    continue
        elif ish2 == 2:
            while True:
                y = int(input("Enter your answer (-1 to exit): "))
                if y == t1 - t2:
                    print(Response_random(True))
                    H += 1
                    break
                elif y == -1:
                    print("Number of Correct Answers: ", H)
                    print("Number of wrong answers: ", T)
                    print("Thanks for playing!")
                    return
                elif y != t1 - t2:
                    print(Response_random(False))
                    T += 1
                    continue
        elif ish2 == 3:
            while True:
                y = int(input("Enter your answer (-1 to exit): "))
                if y == t1 * t2:
                    print(Response_random(True))
                    H += 1
                    break
                elif y == -1:
                    print("Number of Correct Answers: ", H)
                    print("Number of wrong answers: ", T)
                    print("Thanks for playing!")
                    return
                elif y != t1 * t2:
                    print(Response_random(False))
                    T += 1
                    continue
        elif ish2 == 4:
            while True:
                y = int(input("Enter your answer (-1 to exit): "))
                if y == t1 // t2:
                    print(Response_random(True))
                    H += 1
                    break
                elif y == -1:
                    print("Number of Correct Answers: ", H)
                    print("Number of wrong answers: ", T)
                    print("Thanks for playing!")
                    return
                elif y != t1 // t2:
                    print(Response_random(False))
                    T += 1
                    continue
mainOperation()
