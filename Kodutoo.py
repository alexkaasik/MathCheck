import random

while (True):
    MaxNum = 0
    MathRepeat = random.randint(0,40)   
    modes = ['+','-']

    while (0 == MaxNum):
        print("1 - easy")
        print("2 - medium")
        print("3 - hard")
        print("q - quit")
        level = str(input("Pick a level: "))

        if level == '1':
            MaxNum = 25
        elif level == '2':
            MaxNum = 50
            modes.append('/')
            modes.append('*')
        elif level == '3':
            MaxNum = 75
            modes.append('/')
            modes.append('*')
            modes.append('**')
        elif level == 'q':
            exit()
        else:
            print("Enter a valid level\n")

    count = 0
    for x in range(MathRepeat):
        
        c=b=a = int(0)

        while True:
            a = random.randint(0, MaxNum)
            b = random.randint(0, MaxNum)
            c = random.randint(0, len(modes)-1)
            if not (( a == 0 or b == 0 ) and ( modes[c] == "/" )):
                break
        

        if modes[c] == '+':
            guess = float(a + b)
        elif modes[c] == '-':
            guess = float(a - b)
        elif modes[c] == '/':
            guess = float(a / b)
        elif modes[c] == '*':
            guess = float(a * b)
        elif modes[c] == '**':
            guess = float(a ** b)        

        print(f"\n{x+1}/{MathRepeat}")
        answer = float(input(f"{a} {modes[c]} {b} = "))

        if ( round(guess,2) == round(answer,2) ):
            count+=1

    MarkPer = (count/MathRepeat)*100

    if MarkPer < 60:
        GradeAnswer = "U got 2 buddy better next"
    elif 60 <= MarkPer <= 75:
        GradeAnswer = "U got 3 good enough"
    elif 76 <= MarkPer <= 90:
        GradeAnswer = "U got 4 u did good"
    elif 91 <= MarkPer:
        GradeAnswer = "5 SUPER STUDENT"

    print(f"\n{GradeAnswer}\n")
    level = str(input("Do u wand do it again? yes/No?: "))
    if level[0].lower() == "n":
        exit()
