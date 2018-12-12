import turtle
from random import *

#Setting up turtle
x = turtle.Turtle()
x.hideturtle()
turtle.hideturtle()
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
turtle.speed(9000)

#Making the square
def square(size):
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)

square(400)
square(100)
square(200)
square(300)
turtle.penup()
turtle.goto(200,300)
turtle.pendown()
square(-100)
square(-200)
square(-300)


# Makes a red circle
def redDraw(x,y):
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.pencolor("red")
    turtle.penup()
    turtle.goto(x,y-40)
    turtle.pendown()
    turtle.circle(40)
    turtle.end_fill()


def blueDraw(x,y):
    turtle.begin_fill()
    turtle.fillcolor("blue")
    turtle.pencolor("blue")
    turtle.penup()
    turtle.goto(x,y-40)
    turtle.pendown()
    turtle.circle(40)
    turtle.end_fill()

#Turtle code above

# Actual code below


#Variables
userWins = False
computerWins = False

totalFilas = 4
totalColumnas = 4

#Matrix all with 0 ,1 , or 2 depending on if it has a token and what color it is
matrix = [[0, 0, 0, 0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
xValues = [-150, -50, 50, 150]
yValues = [-50, 50, 150, 250]

#Asks the user for input and draws the circle
def userInput():
    x = input("Where?")
    print(matrix)
    if x == "1":
        if matrix[0][0] == 0:
            redDraw(-150,-50)
            matrix [0][0] = 1

        elif matrix[0][1]==0:
            redDraw(-150,50)
            matrix[0][1] = 1

        elif matrix[0][2]==0:
            redDraw(-150,150)
            matrix[0][2] = 1

        elif matrix[0][3]==0:
            redDraw(-150,250)
            matrix[0][3] = 1

    elif x == "2":
        if matrix[1][0] == 0:
            redDraw(-50, -50)
            matrix[1][0] = 1

        elif matrix[1][1] == 0:
            redDraw(-50, 50)
            matrix[1][1] = 1

        elif matrix[1][2] == 0:
            redDraw(-50, 150)
            matrix[1][2] = 1

        elif matrix[1][3] == 0:
            redDraw(-50, 250)
            matrix[1][3] = 1

    elif x == "3":
        if matrix[2][0] == 0:
            redDraw(50, -50)
            matrix[2][0] = 1

        elif matrix[2][1] == 0:
            redDraw(50, 50)
            matrix[2][1] = 1

        elif matrix[2][2] == 0:
            redDraw(50, 150)
            matrix[2][2] = 1

        elif matrix[2][3] == 0:
            redDraw(50, 250)
            matrix[2][3] = 1


    elif x=="4":
        if matrix[3][0] == 0:
            redDraw(150, -50)
            matrix[3][0] = 1

        elif matrix[3][1] == 0:
            redDraw(150, 50)
            matrix[3][1] = 1

        elif matrix[3][2] == 0:
            redDraw(150, 150)
            matrix[3][2] = 1

        elif matrix[3][3] == 0:
            redDraw(150, 250)
            matrix[3][3] = 1


def computerTurn():
    done=False
    columna=0
    for a in range(4):
        fila = 0
        for a in range(4):
            if done == False and matrix[columna][fila]==1:
                    done = checking1(columna,fila)
            fila= fila+1

        columna = columna +1

    if done == False:
        done = notDone()


##For when the computer doesn't detect any threats
## 1 equals user piece and 2 equals computer piece
def notDone():
    done = False;
    x=0
    y=0
    print("hello")
    if matrix[x][y] ==1 and done == False:
        ran = randint(0,1)
        print(ran)
        if ran == 0 and matrix[x + 1][y] == 0:
            blueDraw(xValues[x+1], yValues[y])
            matrix[x+1][y] = 2
            done = True

        elif matrix[x][y+1] == 0:
            blueDraw(xValues[x], yValues[y+1])
            matrix[x][y+1] =2
            done = True


    if matrix[x+1][y] ==1 and done == False:
        if matrix[x + 2][y]==0:
            blueDraw(xValues[x+2], yValues[y])
            matrix[x+2][y] = 2
            done = True
            print("2")
        if matrix[x][y]==0 and done== False:
            blueDraw(xValues[x], yValues[y])
            matrix[x][y] = 2
            done = True
            print("3")
        if matrix[x+1][y+1]==0 and done==False:
            blueDraw(xValues[x+1],yValues[y+1])
            matrix[x+1][y+1]=2
            


    if matrix[x+3][y]==1 and done ==False:
        if matrix[x + 2][y] == 0:
            blueDraw(xValues[x + 2], yValues[y])
            matrix[x + 2][y] = 2
            done = True
            print("4")

    if matrix[x+2][y]==1 and done == False:
        if matrix[x+3][y]==0:
            blueDraw(xValues[x+3], yValues[y])
            matrix[x+3][y]=2
            done = True
            print("5")
        if matrix[x+1][y]==0 and done ==False:
            blueDraw(xValues[x+1], yValues[y])
            matrix[x+1][y]=2
            done = True
            print("6")
        if matrix[x+2][y+1]==0 and done==False:
            blueDraw(xValues[x+2], yValues[y+1])
            matrix[x+2][y+1]=2
            done= True
            print("7")
    if matrix[x+1][y+1]==1 and done == False:
        if matrix[x+1][y+2]==0:
            blueDraw(xValues[x+1], yValues[y+2])
            matrix[x+1][y+2]=2
            done = True
            print("8")




def checking1(x,y,):
    done1 =False

    if x >= totalColumnas - 2:

        # Checking horizontally
        if matrix[x - 1][y] == 1  and matrix[x-2][y-1] !=0 and matrix[x-2][y] ==0 and done1==False:
            blueDraw(xValues[x - 2], yValues[y])
            matrix[x - 2][y] = 2
            done1 = True

        # Checking vertically
        if matrix[x][y + 1] == 1 and matrix[x][y + 2] == 0 and done1==False:

            blueDraw(xValues[x], yValues[y + 2])
            matrix[x][y + 2] = 2
            done1 = True

        # Checking vertically above half of the squar
        if y>= totalFilas -2 and matrix[x][y - 1] == 1 and matrix[x][y + 1] == 0 and done1==False:
            blueDraw(xValues[x], yValues[y + 1])
            matrix[x][y + 1] = 2
            done1 = True

        # Checking diagonally
        if matrix[x - 1][y - 1] == 1 and matrix[x - 2][y - 1] and done1==False:
            blueDraw(xValues[x - 2], yValues[y - 2])
            matrix[x - 2][y - 2] = 2
            done1 = True

        # Checking for space in between horizontally
        if matrix[x - 2][y] != 0 and matrix[x - 1][y] == 0 and done1==False:
            blueDraw(xValues[x - 1], yValues[y])
            matrix[x - 1][y] = 2
            done1 = True
        # Checking for space in between diagonally
        # if matrix[x-2][y-2] ==1:
        #     print("hello")


    else:
        # Checking vertically
        if matrix[x][y + 1] == 1 and matrix[x][y + 2] == 0 and done1==False:
            blueDraw(xValues[x], yValues[y + 2])
            matrix[x][y + 2] = 2
            done1 = True
        # Checking horizontally
        if matrix[x + 1][y] == 1 and matrix[x+2][y] ==0 and matrix[x+2][y-1] !=0  and done1==False:
            blueDraw(xValues[x + 2], yValues[y])
            matrix[x + 2][y] = 2
            done1 = True
        # Checking diagonally
        if matrix[x + 1][y + 1] == 1 and matrix[x + 2][y + 1] != 0 and done1==False:
            blueDraw(xValues[x + 2], yValues[y + 2])
            matrix[x + 2][y + 2] = 2
            done1 = True
        # Checking for space in between horizontally
        if matrix[x + 2][y] == 1 and matrix[x + 1][y] == 0 and done1==False:
            blueDraw(xValues[x + 1], yValues[y])
            matrix[x + 1][y] = 2
            done1 = True


        if matrix[x+2][y+2] ==1 and matrix[x+1][y+1]==0 and matrix[x+1][y]!=0:
            print("jgsjkdkafsdkljfsdkl;jdsf;lkjdsf")


    return done1



while userWins == False and computerWins == False :
    userInput()
    computerTurn()



turtle.done()