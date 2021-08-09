from turtle import *
from genieCivilOuvrage2D import *

##MAQUETTE D'UN PONT

color("blue")
pensize(3)
speed(5000)


# Pour rappel le repère c'est la barre1(à droite) du triangle du milieu

# Fragment du milieu
fragment(-50, -100, 80, 40, 0, -100, -140, -180, 115)

# Fragment de droite
penup()
goto(330, 0)
pendown()
fragment(280, 230, 410, 370, 330, 230, 190, 150, 445) # On prend 330 et on additionne ou soustrait aux valeurs du premier appel

# Fragment de gauche
penup()
goto(-330, 0)
pendown()
fragment(-330-50, -330-100, -330+80, -330+40, -330+0, -330-100, -330-140, -330-180, -330+115)


#Pied gauche
pied(-250, -20, -270, -40)

#Pied droite
pied(80, -20, 60, -40)


done()