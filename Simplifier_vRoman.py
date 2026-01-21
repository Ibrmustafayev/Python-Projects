import time

class interpret:                        #Handles conversion between Roman numerals and Decimal integers.
    def rtd(number_given):                  #Converts Roman string to Decimal integer. Returns '!!!' on invalid input.                                                  
        number_given=number_given.upper()                                                  
        for m,n in {"I":"V","X":"L","C":"D","M":"D"}.items():           # Basic validation: Check for repeated characters that violate standard rules
            if number_given.count(m)>3 or number_given.count(n)>1:
                return "!!!"
        rnum={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}              
        number=0

        # Iterates through the string to apply additive/subtractive rules
        # e.g., IV: subtracts 1 (I) because it's less than 5 (V)
        for k in range(len(number_given)-1):
            j1,j2=number_given[k],number_given[k+1]
            if not(j1=="I" and (j2=="V" or j2=="X") or j1=="X" and (j2=="L" or j2=="C") or j1=="C" and (j2=="D" or j2=="M")):
                number+=rnum[j1]
            else:
                number-=rnum[j1]
        return number

    def dtr(n_given):                                                       #Converts Decimal integer to Roman string using the subtractive method.
        rnum=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        value=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans=""
        for j in value:
            ans+=(n_given//j)*rnum[value.index(j)]
            n_given-=(n_given//j)*j
        return ans

class operations:                               #Contains basic arithmetic methods used by the order evaluator.
    def product(nums):
        return [nums[0]*nums[1]]

    def division(nums):                         # Only returns integer results; fractions are invalid in standard Roman numerals
        if nums[0]/nums[1]==nums[0]//nums[1]:
            return [int(nums[0]/nums[1])]
        return ["!!!"]

    def addition(nums):
        return [sum(nums)]  

    def subtraction(nums):                      # Roman numerals do not support zero or negative numbers
        if nums[0]-nums[1]>0:
            return [nums[0]-nums[1]]
        return ["!!!"]
    
class order:                                    #Handles mathematical precedence (order of operations).
    def basicoperations(exp1):                  #Evaluates multiplication, division, addition, and subtraction in order.
        while "*" in exp1 or "/" in exp1 or "+" in exp1 or "-" in exp1 or "!!!" in exp1:
            if "!!!" in exp1:
                return "There are some issues about the system(Fraction, zero, minus)!!! Enter a valid expression."
            ind1,ind2,ind3,ind4=exp1.index("*") if "*" in exp1 else -1,exp1.index("/") if "/" in exp1 else -1,exp1.index("+") if "+" in exp1 else -1,exp1.index("-") if "-" in exp1 else -1
            # Priority 1: Multiplication and Division (Left to Right)
            if 0<ind1<ind2 or ind2<0<ind1:
                exp1[ind1-1:ind1+2]=operations.product(exp1[ind1-1:ind1+2:2])
            elif 0<ind2<ind1 or ind1<0<ind2:
                exp1[ind2-1:ind2+2]=operations.division(exp1[ind2-1:ind2+2:2])
            # Priority 2: Addition and Subtraction
            elif 0<ind3<ind4 or ind4<0<ind3:
                exp1[ind3-1:ind3+2]=operations.addition(exp1[ind3-1:ind3+2:2])
            elif 0<ind4<ind3 or ind3<0<ind4:
                exp1[ind4-1:ind4+2]=operations.subtraction(exp1[ind4-1:ind4+2:2])
        return exp1

    def parenthesis(exp1):                      #Recursively solves expressions inside parentheses first.
        while "(" in exp1:
            left = len(exp1) - 1 - exp1[::-1].index("(")                # find the last opening parenthesis
            right = exp1.index(")", left)                               # find the first closing parenthesis after it
            value = order.basicoperations(exp1[left + 1:right])         # evaluate inside the parentheses        
            exp1[left:right + 1] = value                                # replace "( ... )" with the computed value
        return exp1

class main:                                     #Main logic to parse the string into tokens and compute the result.
    def main(given_exp):                        #Pre-processing: handle spaces and identify tokens
        exp=[i for i in given_exp]+["$"]        
        exp1,digit=[],""
        for j in range(len(exp)):
            if exp[j] in ["*","/","+","-","$",")"]:
                if exp[j-1]!=")":
                    exp1+=[interpret.rtd(digit+" ")]+[exp[j]]
                    digit=""
                else:
                    exp1+=[exp[j]]
            elif exp[j] in ["("]:
                exp1+=[exp[j]]
            else:
                digit+=exp[j]

        # Step 1: Solve Parentheses -> Step 2: Solve remaining operations
        exp1=order.parenthesis(exp1)
        if "!!!" not in exp1:
            if str(order.basicoperations(exp1)[0]).isdigit():
                print(f"The answer is {interpret.dtr(order.basicoperations(exp1)[0])}\n")
            else:
                print(f"The answer is {order.basicoperations(exp1[0])}\n")
        else:
            print("Enter a valid number.\n")

#Entry Point
print("Welcome to the Simplifier v.Roman!!!\n")
while True:
    ent=input("Do you want to enter? (y): ")
    if ent.lower()=="y":
        given_exp=input("Enter the expression: ")
        main.main(given_exp)
        time.sleep(1)
    else:
        print("See you again!!!")
        break