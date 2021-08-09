from turtle import *

def triangle(cote):
    setheading(0)
    for i in range(3):
        left(120)
        forward(cote)


def barre(l):
    setheading(90)
    forward(l)


def rectangle(long, larg):
    setheading(0)
    for i in range(2):
        forward(long)
        left(90)
        forward(larg)
        left(90)


def carre(c):
    setheading(0)
    for i in range(4):
        forward(c)
        left(90)


def ellipse():
    setheading(90)
    circle(35, 45) # circle(rayon, étendu) avec étendu = la partie à dessiner(180=moitié)
    circle(220, 90) # Pas forcé d'avoir (40*2) ici
    circle(35, 45)

def cercle(rayon):
    begin_fill()
    circle(rayon)
    end_fill()

def trapeze(gbase, pbase, cote):
    setheading(0)
    forward(pbase)
    setheading(60)
    forward(cote)
    left(120)
    forward(gbase)
    left(120)
    forward(cote)


## FONCTIONS DU PONT

# Fonction fragment
def fragment(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    #Triangle milieu
    triangle(100)

    #Barre1
    barre(80)

    #Barre2
    penup()
    goto(x1, 0)
    pendown()
    barre(85)

    #Barre3
    penup()
    goto(x2, 0)
    pendown()
    barre(80)


    #Triangle droite
    penup()
    goto(x3, 0)
    pendown()
    triangle(80)

    # Barre1
    barre(45)
    #Fermeture
    backward(45)
    right(30)
    forward(35)
    backward(35)
    setheading(0)
    forward(35)
    #backward(35) # Cherche encore prkw çà n'a pas d'importance? En fait prck après c'est un penup et on repart à l'origine

    #Barre2
    penup()
    goto(x4, 0)
    pendown()
    barre(65)

    #Barre3
    penup()
    goto(x5, 0)
    pendown()
    barre(55)

    # Triangle gauche
    penup()
    goto(x6, 0)
    pendown()
    triangle(80)

    # Barre1
    barre(50)

    #Barre2
    penup()
    goto(x7, 0)
    pendown()
    barre(65)

    #Barre3
    penup()
    goto(x8, 0)
    pendown()
    barre(45)
    # Fermeture
    backward(45)
    left(30)
    forward(35)
    backward(35)
    setheading(180)
    forward(35)

    # Tracer la démi ellipse
    penup()
    goto(x9, 0)
    pendown()
    ellipse()


# Fonction Pied
def pied(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    color("blue")
    begin_fill()

    rectangle(70, 20)
    penup()
    goto(x2, y2)
    pendown()
    rectangle(110, 20) # 70+20+20

    end_fill()


# Fonctions MAISONS

#Fonction petitRec
def petitRec(x, y, long, larg):
    penup()
    goto(x, y)
    pendown()
    color("gray", "white")
    begin_fill()
    rectangle(long, larg)
    end_fill()


def petitCarre(x, y, c):
    penup()
    goto(x, y)
    pendown()
    color("gray", "white")
    begin_fill()
    carre(c)
    end_fill()


def vitre(X, Y, x1, y1, y2):
    penup()
    goto(X, Y)
    pendown()
    color("black", "gray")
    begin_fill()
    rectangle(100, 300)
    end_fill()
    # à l'intérieur
    petitRec(x1, y1, 40, 70)
    petitRec(x1+40, y1, 40, 70)
    petitRec(x1, y1+70, 40, 70)
    petitRec(x1+40, y1+70, 40, 70)

    petitCarre(x1, y2, 40)
    petitCarre(x1+40, y2, 40)
    petitCarre(x1, y2+40, 40)
    petitCarre(x1+40, y2+40, 40)


def chapeau(x, y):
    setheading(90)
    penup()
    goto(x, y)
    pendown()
    color("black", "lightgreen")
    begin_fill()
    left(60)
    forward(100)
    left(60)
    forward(100)
    end_fill()