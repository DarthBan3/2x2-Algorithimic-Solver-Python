Red = ["r", 'r','r','r','r']
Green = ['g','g','g','g','g']
Orange = ['o','o','o','o','o']
Blue = ['b','b','b','b','b']
Yellow = ['y','y','y','y','y']
White = ['w','w','w','w','w']

'''
Each side of the cube is a list of 5 elements. First four are the colours of the pieces.
The fifth is merely a placeholder, and serves as a piece to compare with. 
The colours go as per the indexing mentioned in the Image.
This file serves as a library of all the Quarter turn metric moves for a 2x2 under those 
conditions. I am including this as a seperate file as it may be useful for other projects that
you may try.
'''



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
