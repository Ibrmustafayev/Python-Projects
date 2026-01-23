import random                               #randint()  &   choice()
import operator
from time import sleep
from math import floor

class qmechanics:
    @staticmethod
    def percentage(opr_p,num_q):
        if num_q<=17:
            if opr_p<=60:
                return random.choice(["+","-"])
            else:
                return random.choice(["*","/"])
        else:
            if opr_p<=80:
                return random.choice(["+","-"])
            else:
                return random.choice(["*","/"])
            
    @staticmethod
    def eg_percentage(opr_p_,numbers):
        if numbers[0]<20 and numbers[1]<20:
            if opr_p_<=5:
                return random.choice(["+","-"])
            else:
                return "*" if opr_p_<=15 else "/"
        elif numbers[0]>40 and numbers[1]>40:
            if opr_p_<=80:
                return random.choice(["+","-"])
            else:
                return "*" if opr_p_<=95 else "/"
        elif 20<=numbers[0]<=40 and 20<=numbers[1]<=40:
            return random.choice(["+","-"]) if opr_p_<=40 else random.choice(["*","/"])
        elif numbers[0]<20 or numbers[1]<20:
            return random.choice(["+","-"]) if opr_p_<=10 else random.choice(["*","/"])
        else:
            return random.choice(["+","-","*","/"])

    @staticmethod                 
    def qmaking(num_q):
        operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        if num_q<=10:
            n1,n2=random.randint(1,10),random.randint(1,10)
            operation=random.choice(["+","-","*","/"])
        elif num_q<=17:
            n1,n2=random.randint(11,20),random.randint(11,20)
            opr_p=random.randint(1,100)
            operation=qmechanics.percentage(opr_p,num_q)
        else:
            n1,n2=random.randint(21,50),random.randint(21,50)
            opr_p=random.randint(1,100)
            operation=qmechanics.percentage(opr_p,num_q)
        return [str(n1)+operation[0]+str(n2),floor(operators.get(operation)(n1,n2)*10)/10]
    @staticmethod
    def eg_qmaking():
        operators={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        n1,n2=random.randint(1,50),random.randint(1,50)
        opr_p_=random.randint(1,100)
        operation=qmechanics.eg_percentage(opr_p_,[n1,n2])
        return [str(n1)+operation[0]+str(n2),floor(operators.get(operation)(n1,n2)*10)/10]

class game:   
    @staticmethod                                                                                      
    def endgame(score):
        print("Now, you are in the End Game.\nIt is about only one question that is the hardest one ever you faced.\nGOOD LUCK!\n")
        q_a=qmechanics.eg_qmaking()
        print(q_a[0])
        ans_g=float(input())
        sleep(1)
        if ans_g==q_a[1]:            
            if score+60==99:
                sleep(1)
                print(f"Correct!!!\nCongratulations!!!\nYou have answered all the questions correctly. So, you got \"+1\" point.\nYour total score is {score+61}.")
                return score+61
            else:
                print(f"Correct!!! Congratulations!!!\nYour total score is {score+60}.")
                return score+60
        else:
            print(f"Incorrect :(\nThe answer was {q_a[1]}.\nYou lost.\nYour total score is {score}.")
            return score

    @staticmethod
    def part3(score):
        num_q,heal,wbc=18,3,1
        print(f"Let's start to Part 3 of the game.\nHeal in Part 3: {heal}\n")
        while num_q<=22:
            q_a=qmechanics.qmaking(num_q)
            print(q_a[0])
            try:
                ans_g = float(input())
            except ValueError:
                wbc-=1
                print(f"Please enter a valid number! Next question will change.\nYou have {wbc} chances to enter invalid value!!!\n")
                if wbc==0:
                    print("You eliminated!!!\nPlay in the correct way next time, please.")
                    break
                continue
            sleep(1)
            num_q+=1
            if ans_g==q_a[1]:
                score+=3
                print(f"Correct!!!\nYour current score is {score}.\n")
            else:
                heal-=1
                print(f"Incorrect :(\nThe answer was {q_a[1]}.\nYour current score is {score}\nThe number of chances you have is {heal} in Part 3.\n")
                if heal==0:
                    print(f"\nYou lost.\nYour total score is {score}.")
                    return [heal,score]
        return [heal,score]

    @staticmethod
    def part2():
        num_q,score,heal,wbc=11,10,2,2
        print(f"Let's start to Part 2 of the game.\nHeal: {heal}\n")
        while num_q<=17:
            q_a=qmechanics.qmaking(num_q)
            print(q_a[0])
            try:
                ans_g = float(input())
            except ValueError:
                wbc-=1
                print(f"Please enter a valid number! Next question will change.\nYou have {wbc} chances to enter invalid value!!!\n")
                if wbc==0:
                    print("You eliminated!!!\nPlay in the correct way next time, please.")
                    break
                continue
            sleep(1)
            num_q+=1
            if ans_g==q_a[1]:
                score+=2
                print(f"Correct!!!\nYour current score is {score}.\n")
            else:
                heal-=1
                print(f"Incorrect :(\nThe answer was {q_a[1]}.\nYour current score is {score}\nThe number of chances you have is {heal} in Part 2 .\n")
                if heal==0:
                    print(f"\nYou lost.\nYour total score is {score}.")
                    return [heal,score]
        return [heal,score]

    @staticmethod
    def part1():
        num_q,score,heal,wbc=1,0,1,3
        print(f"Let's start to Part 1 of the game.\nHeal: {heal}\n")
        while num_q<=10:
            q_a=qmechanics.qmaking(num_q)
            print(f"The question {num_q}:",q_a[0])
            try:
                ans_g = float(input())
            except ValueError:
                wbc-=1
                print(f"Please enter a valid number! Next question will change.\nYou have {wbc} chances to enter invalid value!!!\n")
                if wbc==0:
                    print("You eliminated!!!\nPlay in the correct way next time, please.")
                    break
                continue
            sleep(1)
            num_q+=1
            if ans_g==q_a[1]:
                score+=1
                print(f"Correct!!!\nYour current score is {score}.\n")
            else:
                print(f"Incorrect :(\nThe answer was {q_a[1]}.\nYou lost.\nYour total score is {score}.")
                return score
        return score

print("Welcome to the math quiz game!!!\nIn this game, there are 4 stages: 3 parts and \"End Game\".\nPart 1:\n  10 questions (each correct = +1 point)\n  If you answer wrong, the game will over.")
print("  After entering 3 invalid value, you will be eliminated.\nPart 2:\n  7 questiions (each correct = +2 point)\n  You have 2 chance to answer wrong.\n  After entering 2 invalid value, you will be eliminated.")
print("Part 3:\n  5 questions (each correct = +3 point)\n  You have 3 chance to answer wrong.\n  After entering 1 invalid value, you will be eliminated.\nEnd Game:")
print("  The last question (correct = +60 point).\n  If you answer wrong, the game will over.\nExtra notes:\n  If all the answers you wrote are correct, you will get +1 point and reach 100.")
print("  Expressions are random.\nSpecial note:\n  If the question is \"7/4\", you must enter 1.7, not 1.75.\nGOOD LUCK!!!\n")
sleep(5)

pl_num=int(input("Enter the number of the players: "))
pl_scores=[]+[0]*pl_num
for pl in range(len(pl_scores)):
    sleep(3)
    print(f"\nNow, it is the turn of the Player {pl+1}.\n")
    pl_scores[pl]=game.part1()
    if pl_scores[pl]==10:
        sleep(1)
        ss1=game.part2()
        success,pl_scores[pl]=ss1[0],ss1[1]
        if success!=0:
            sleep(1)
            ss2=game.part3(pl_scores[pl])
            success,pl_scores[pl]=ss2[0],ss2[1]
            if success!=0:
                sleep(1)
                pl_scores[pl]=game.endgame(pl_scores[pl])
print("\nThe game is over. Now, the table:\n")

print(f"{'PLAYERs':<10} | {'SCORE':<5}")
print("-" * 18)
for i, s in enumerate(pl_scores):
    print(f"Player {i+1:<7} | {s:<5}")
sleep(3)
print(f"\nThe winner is Player {pl_scores.index(max(pl_scores))+1}!!!")



    

#https://github.com/ndleah/python-mini-project/blob/main/Math_Game/math_game.py