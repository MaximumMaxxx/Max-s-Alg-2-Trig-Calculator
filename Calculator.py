import math, distutils.util

def acos(num):
        return(math.degrees(math.acos(num)))
def asin(num):
        return(math.degrees(math.asin(num)))
def atan(num):
        return(math.degrees(math.atan(num)))
def cos(num):
        return(math.cos(math.radians(num)))
def sin(num):
        return(math.sin(math.radians(num)))
def tan(num):
        return(math.tan(math.radians(num)))

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
    completed = True
    round_places = 0
    Round = distutils.util.strtobool(input("Do you want to round? "))
    if Round == True:
        round_places = int(input("How many places do you want to round to? "))
    USR = str(input("What would you like to do? Pythag, Trig: "))
    USR = USR.lower()
    if USR == "pythag":
        pythag()
    elif USR == "trig":
        ratio = input("What trig ratio do you want to use? Note: Use the 3 letter names for the ratio: ")
        ratio = ratio.lower()
        if ratio == "sin":
            line = input("What angle are you solving for? Opp or Hyp? ")
            ang = float(input("what angle are you solving with? (In Deg) " ))
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
                opp = float(input("What is the length of the adjactent line? "))
                RSLT = opp*tan(ang)
            elif line == "adj":
                adj = float(input("What i ras the length of the opposite line? "))
                RSLT = adj/tan(ang)
        elif ratio == "cos":
            line = input("What angle are you solving for? Adj or Hyp? ")
            ang = float(input("what angle are you solving with? (In Deg) "))
            line=line.lower()
            if line == "adj":
                hype = float(input("What is the length of the hypotonuse line? "))
                RSLT = hype*cos(ang)
            elif line == "hyp":
                opp = float(input("What is the length of the adjacent? "))
                RSLT = opp/cos(ang)
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
        completed = False
    if completed:    
        if Round:
            print(round(RSLT,round_places))
        else:
            print(RSLT)
        Again = distutils.util.strtobool(input("Do you want to run again? "))
        if Again:
            main()

if __name__ == "__main__":
    main()

