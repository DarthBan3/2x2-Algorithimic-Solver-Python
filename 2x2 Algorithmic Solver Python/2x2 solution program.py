#Face System

Red = ["r", 'r','r','r','r']
Green = ['g','g','g','g','g']
Orange = ['o','o','o','o','o']
Blue = ['b','b','b','b','b']
Yellow = ['y','y','y','y','y']
White = ['w','w','w','w','w']

##Moveset definitions
#Direct Moves
def F():
    a = Red[3]
    del Red[3]
    Red.insert(0, a)
    Green[3],White[0],Blue[1],Yellow[2] = Yellow[2], Green[3], White[0], Blue[1]
    Green[2], White[3], Blue[0], Yellow[1] = Yellow[1], Green[2], White[3], Blue[0]
    print("F", end=" ")

def U():
    a = Yellow[3]
    del Yellow[3]
    Yellow.insert(0, a)
    Red[0], Blue[0], Orange[0], Green[0] = Green[0], Red[0], Blue[0], Orange[0]
    Red[3], Blue[3], Orange[3], Green[3] = Green[3], Red[3], Blue[3], Orange[3]
    print("U", end=" ")

def D():
    a = White[3]
    del White[3]
    White.insert(0, a)
    Red[2], Green[2], Orange[2], Blue[2] = Blue[2], Red[2], Green[2], Orange[2]
    Red[1], Green[1], Orange[1], Blue[1] = Blue[1], Red[1], Green[1], Orange[1]
    print("D", end=" ")

def R():
    a = Green[3]
    del Green[3]
    Green.insert(0, a)
    Red[0], Yellow[0], Orange[2], White[0] = White[0], Red[0], Yellow[0], Orange[2]
    Red[0+1], Yellow[0+1], Orange[3], White[0+1] = White[0+1], Red[0+1], Yellow[0+1], Orange[3]
    print("R", end=" ")

def L():
    a = Blue[3]
    del Blue[3]
    Blue.insert(0, a)
    Red[3], White[3], Orange[1], Yellow[3] = Yellow[3], Red[3], White[3], Orange[1]
    Red[4-2], White[4-2], Orange[2-2], Yellow[4-2] = Yellow[4-2], Red[4-2], White[4-2], Orange[2-2]
    print("L", end=" ")

def B():
    a = Orange[3]
    del Orange[3]
    Orange.insert(0, a)
    for i in range(3):
        Green[1-1],White[1],Blue[2],Yellow[3] = Yellow[3],Green[0],White[1],Blue[2]
        Green[1], White[2], Blue[3], Yellow[0] = Yellow[0], Green[1], White[2], Blue[3]
    print("B", end=" ")

#Inverse Moveset
def Fi():
    print("Fi", end=" ")
    for i in range(3):
        a = Red[3]
        del Red[3]
        Red.insert(0, a)
        Green[3], White[0], Blue[1], Yellow[2] = Yellow[2], Green[3], White[0], Blue[1]
        Green[2], White[3], Blue[0], Yellow[1] = Yellow[1], Green[2], White[3], Blue[0]

def Ui():
    print("Ui", end = " ")
    for i in range(3):
        a = Yellow[3]
        del Yellow[3]
        Yellow.insert(0, a)
        Red[0], Blue[0], Orange[0], Green[0] = Green[0], Red[0], Blue[0], Orange[0]
        Red[3], Blue[3], Orange[3], Green[3] = Green[3], Red[3], Blue[3], Orange[3]

def Di():
    print("Di", end = " ")
    for i in range(3):
        a = White[3]
        del White[3]
        White.insert(0, a)
        Red[2], Green[2], Orange[2], Blue[2] = Blue[2], Red[2], Green[2], Orange[2]
        Red[1], Green[1], Orange[1], Blue[1] = Blue[1], Red[1], Green[1], Orange[1]

def Ri():
    print("Ri", end = " ")
    for i in range(3):
        a = Green[3]
        del Green[3]
        Green.insert(0, a)
        Red[0], Yellow[0], Orange[2], White[0] = White[0], Red[0], Yellow[0], Orange[2]
        Red[0 + 1], Yellow[0 + 1], Orange[3], White[0 + 1] = White[0 + 1], Red[0 + 1], Yellow[0 + 1], Orange[3]

def Li():
    print("Li", end = " ")
    for i in range(3):
        a = Blue[3]
        del Blue[3]
        Blue.insert(0, a)
        Red[3], White[3], Orange[1], Yellow[3] = Yellow[3], Red[3], White[3], Orange[1]
        Red[4 - 2], White[4 - 2], Orange[2 - 2], Yellow[4 - 2] = Yellow[4 - 2], Red[4 - 2], White[4 - 2], Orange[2 - 2]

def Bi():
    print("Bi", end = " ")
    for i in range(3):
        a = Orange[3]
        del Orange[3]
        Orange.insert(0, a)
        for i in range(3):
            Green[1 - 1], White[1], Blue[2], Yellow[3] = Yellow[3], Green[0], White[1], Blue[2]
            Green[1], White[2], Blue[3], Yellow[0] = Yellow[0], Green[1], White[2], Blue[3]

def bottomwhite():
    count = 0
    for i in White:
        if i==White[4]:
            count = count+1
    if count==5:
        return True
    else:
        return False
def topyellow():
    count = 0
    for i in Yellow:
        if i==Yellow[4]:
            count -= -1
    if count==5:
        return True
    else:
        return False

def toplayer():
    if Red[0]==Red[3] and Blue[0]==Blue[3]:
        return True
    else:
        return False
def bottomlayer():
    if Red[1]==Red[2] and Blue[1]==Blue[2]:
        return True
    else:
        return False



'''
Method used is Ortega. 
Involves 3 steps. 
1. Orientation of Bottom Layer. White in this case, for sake of programming simplicity
2. Orientation of Top Layer. Yellow in this case. Can just use algorithims from 3x3's OLL
3. Permutation of Both Layers. (PBL). Simple algorithim set to shuffle the remaining pieces to their positions
Algotirthims: http://www.cubewhiz.com/ortegapbl.php
Video Explanation: https://www.youtube.com/watch?v=Ar5-X7K9v1A
'''

#Cube state input
Red = eval(input("Front")) + ["r"]
Green = eval(input("Right")) + ["g"]
Orange = eval(input("Back")) + ['o']
Blue = eval(input("Left")) + ['b']
Yellow = eval(input("Top")) + ['y']
White = eval(input("Bottom")) + ['w']


#White Face Orientation
while not bottomwhite():
    if White[0]==White[4]:
        D()
    else:
        if White[4]==Yellow[1] or White[4]==Red[0] or White[4]==Green[3]:
            if Yellow[1]==White[4]:
                R()
                U()
                U()
                Ri()
                Ui()
                R()
                U()
                Ri()
            elif Red[0]==White[4]:
                Fi()
                Ui()
                F()
            else:
                R()
                U()
                Ri()
        elif Red[2]==White[4] or Blue[1]==White[1]:
            Li()
            U()
            L()
        elif Red[1]==White[4] or Green[2]==White[4]:
            R()
            U()
            Ri()
        elif Green[1]==White[4] or Orange[2]==White[4]:
            B()
            U()
            Bi()
        elif Blue[2]==White[4] or Orange[1]==White[4]:
            Bi()
            U()
            B()
        else:
            U()
print("")


#Yellow face orientation
while not topyellow():
    while Yellow[1]!=Yellow[4]:
        Ri()
        Di()
        R()
        D()
    else:
        U()

print ("")


#Final Step. All the remaining pieces are put into their place with simple algorithims
while (not toplayer()) or (not bottomlayer()):
    if Red[0]==Red[3] and Blue[0]==Blue[3]:
        if Red[2]==Red[1] and Blue[1]==Blue[2]:
            pass
        elif Red[2]==Red[1] or Blue[1]==Blue[2] or Orange[1]==Orange[2] or Green[1]==Green[2]:
            while Green[1]!=Green[2]:
                D()
            F()
            F()
            B()
            B()
            R()
            U()
            Ri()
            Ui()
            Ri()
            F()
            R()
            R()
            Ui()
            Ri()
            Ui()
            R()
            U()
            Ri()
            Fi()
            print("")
        else:
            R()
            R()
            L()
            L()
            F()
            R()
            Ui()
            Ri()
            Ui()
            R()
            U()
            Ri()
            Fi()
            R()
            U()
            Ri()
            Ui()
            Ri()
            F()
            R()
            Fi()
            print("")
    elif Red[0]==Red[3] or Blue[0]==Blue[3] or Orange[0]==Orange[3] or Green[0]==Green[3]:
        while Blue[0]!=Blue[3]:
            U()
        R()
        U()
        Ri()
        Ui()
        Ri()
        F()
        R()
        R()
        Ui()
        Ri()
        Ui()
        R()
        U()
        Ri()
        Fi()
        print("")
    else:
        F()
        R()
        Ui()
        Ri()
        Ui()
        R()
        U()
        Ri()
        Fi()
        R()
        U()
        Ri()
        Ui()
        Ri()
        F()
        R()
        Fi()
        print("")

print("")

#Turns top layer till the cube is solved
for i in range(4):
    if Red[0]==Red[1]:
        break
    else:
        U()


print("")
print ("Solved!")

