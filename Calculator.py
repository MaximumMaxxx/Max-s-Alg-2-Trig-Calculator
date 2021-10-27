import math


def acos(num):
    return(round(math.acos(num),2))

def asin(num):
    return(round(math.asin(num),2))

def atan(num):
    return(round(math.atan(num),2))

def cos(num):
    return(round(math.cos(math.radians(30)),2))

def sin(num):
    return(round(math.sin(math.radians(30)),2))

def tan(num):
    return(round(math.tan(math.radians(30)),2))

# Function brutally stolen from https://www.w3resource.com/python-exercises/math/python-math-exercise-68.php

def pythag():
    formula = input('Which side (a, b, c) do you wish to calculate? side> ')

    if formula == 'c':
        side_a = float(input('Input the length of side a: '))
        side_b = float(input('Input the length of side b: '))

        side_c = math.sqrt(side_a * side_a + side_b * side_b)
        
        print('The length of side c is: ' )
        print(side_c)

    elif formula == 'a':
        side_b = float(input('Input the length of side b: '))
        side_c = float(input('Input the length of side c: '))
        
        side_a = math.sqrt((side_c * side_c) - (side_b * side_b))
        
        print('The length of side a is' )
        print(side_a)

    elif formula == 'b':
        side_a = float(input('Input the length of side a: '))
        side_c = float(input('Input the length of side c: '))
            
        side_b = math.sqrt(side_c * side_c - side_a * side_a)
        
        print('The length of side b is')
        print(side_b)

    else:
        print('Please select a side between a, b, c')

# Sine
# Opposite
# Hypotonuse
#
# Cosine
# Adjacent
# Hyponuse
#
# Tangent
# Opposite
# Adjacent


def main():
    USR = str(input("What would you like to do? Pythag, Trig: "))
    USR = USR.lower()
    print(USR)
    if USR == "pythag":
        pythag()
    elif USR == "trig":
        ratio = input("What trig ratio do you want to use? Note: Use the 3 letter names for the ratio: ")
        ratio = ratio.lower()
        if ratio == "sin":
            line = input("What angle are you solving for? Opp or Hyp? ")
            ang = float(input("what angle are you solving with? (In Deg)" ))
            line=line.lower()
            if line == "opp":
                hype = float(input("What is the length of the hypotonuse? "))
                RSLT = hype*sin(ang)
            elif line == "hyp":
                opp = float(input("What is the length of the opposite line? "))
                RSLT = opp/sin(ang)
        elif ratio == "tan":
            line = input("What angle are you solving for? Opp or Adj? ")
            ang = float(input("what angle are you solving with? (In Deg) "))
            line=line.lower()
            if line == "opp":
                opp = float(input("What is the length of the opposite line? "))
                RSLT = opp*sin(ang)
            elif line == "adj":
                adj = float(input("What is the length of the adjactent line? "))
                RSLT = adj/sin(ang)
        elif ratio == "cos":
            line = input("What angle are you solving for? Opp or Hyp? ")
            ang = float(input("what angle are you solving with? (In Deg) "))
            line=line.lower()
            if line == "adj":
                hype = float(input("What is the length of the adjacent line? "))
                RSLT = hype*sin(ang)
            elif line == "hyp":
                opp = float(input("What is the length of the hypotonuse? "))
                RSLT = opp/sin(ang)
        elif ratio == "asin":
            opp = float(input("what is the length of the Opposite line? "))
            hype = float(input("what is the length of the Hypotonuse? "))
            RSLT = asin(opp/hype)
        elif ratio == "atan":
            opp = float(input("what is the length of the Opposite line? "))
            adj = float(input("what is the length of the Adjacent Line? "))
            RSLT = atan(opp/adj)
        elif ratio == "acos":
            adj = float(input("what is the length of the Adjacent line? "))
            hype = float(input("what is the length of the Hypotonuse? "))
            RSLT = acos(adj/hype)
    else:
        print("Somehow something didn't work")
    print(RSLT)
if __name__ == "__main__":
    main()

