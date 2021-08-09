from turtle import *
from genieCivilOuvrage2D import *

## MAQUETTE D'UN BATIMENT

color("black")
pensize(2)
speed(6000)


## Le ciel
penup()
goto(-700, 200)
pendown()
color("skyblue")
begin_fill()
rectangle(1500, 500)
end_fill()

## Le grang rectangle
penup()
goto(-460, -170)
pendown()
color("black", "#ebf2ff") #cdcecc? #e6e6e5
begin_fill()
rectangle(960, 330)


# # Toiture trapèze
penup()
goto(-450, 160)
pendown()
trapeze(1010, 950, 50)
end_fill()

# #Fondement
petitRec(-460, -180, 960, 10)

# #Balcon
petitRec(-85, 150, 180, 50)

# # ########### Grand Rectangle terminé


# # ## La Porte # Le milieu du rectangle est l'origine du repère

petitRec(-60, -100, 120, 250)
petitRec(-50, -170, 100, 320)

penup()
goto(-40, -100)
pendown()
color("gray", "lightgray")
begin_fill()
rectangle(80, 250)
end_fill()

# # # #Petite Porte


petitRec(-25, -100, 25, 60)
petitRec(0, -100, 25, 60) # 25= -25 le x du précédent + 25 long du précédent et -25+25=0
petitRec(-25, -40, 25, 60) # -40=-100+60 larg
petitRec(0, -40, 25, 60)
penup()
goto(25, 20)
pendown()
left(90)
circle(25, 180) # La mm chose que j'avais utilisé pour l'ellipse

penup()
goto(-10, 70)
pendown()
color("black")
cercle(10)

petitRec(-25, 90, 25, 40)
petitRec(0, 90, 25, 40)

# # # ## Escaliers
# # # # Premier pas
petitRec(-60, -110, 120, 10) # En dessous du y de la porte
petitRec(-25, -110, 50, 10) # à l'intérieur

# # # #Les cotés
# # # #gauche
petitRec(-60, -170, 10, 60) # -170= -110-60
# # #droite
petitRec(50, -170, 10, 60) # -60+120-10

# # # #Les escaliers proprement
petitRec(-30, -120, 60, 10)
petitRec(-33, -130, 65, 10)
petitRec(-35, -140, 70, 10)
petitRec(-38, -150, 75, 10)
petitRec(-40, -160, 80, 10)
petitRec(-44, -170, 90, 10)

# # ######### Porte terminée


# # ## LES VITRES DE GAUCHE ET DROITE GrandRec

# # #VITRES GAUCHES
# # # -190=-60 de la porte -120(30 espace et 100 longueur) et y=-160 de l'avant dernier escalier
vitre(-190, -160, -180, -150, 30) # -150+70+70+40=30
vitre(-315, -160, -305, -150, 30)
vitre(-440, -160, -430, -150, 30)

# # #VITRES DROITES
vitre(100, -160, 110, -150, 30) # -60 x de la porte +100 larg +40 espace
vitre(230, -160, 240, -150, 30)
vitre(360, -160, 370, -150, 30)

# ############## vitres terminées


# #### ETAGE
petitRec(-315, 205,650, 50)

penup()
goto(-140, 205)
pendown()
barre(50)

penup()
goto(160, 205)
pendown()
barre(50)

# # TRIANGLES
chapeau(-140, 255) # GAUCHE
chapeau(335, 255) # DROITE

# # Relier les triangles
setheading(0) # Prck la fonction barre avait mis setheading(90)
penup()
goto(-230, 305)
pendown()
color("black","lightgreen")
begin_fill()
forward(475)
right(150)
forward(100)
right(30)
forward(295)
right(30)
forward(100)
end_fill()

# ## Les petits fenêtres
# #GAUCHE
petitRec(-295, 205,15, 40)
petitRec(-280, 205,15, 40)

petitRec(-245, 205,15, 40)
petitRec(-230, 205,15, 40)

petitRec(-195, 205,15, 40)
petitRec(-180, 205,15, 40)

# #DROITE
petitRec(180, 205,15, 40)
petitRec(195, 205,15, 40)

petitRec(230, 205,15, 40)
petitRec(245, 205,15, 40)

petitRec(280, 205,15, 40)
petitRec(295, 205,15, 40)

# #MILIEU
petitRec(-120, 205,15, 40)
petitRec(-105, 205,15, 40)

petitRec(-60, 205,15, 40)
petitRec(-45, 205,15, 40)

petitRec(-10, 205,15, 40)
petitRec(5, 205,15, 40)

petitRec(40, 205,15, 40)
petitRec(55, 205,15, 40)

petitRec(100, 205,15, 40)
petitRec(115, 205,15, 40)


######### étage terminé


##### JARDIN ##############

## TAPIS ROUGE
penup()
goto(-320, -330)
pendown()
color("brown")
begin_fill()
setheading(90)
right(60)
forward(300)
right(30)
forward(120)
right(30)
forward(300)
end_fill()


## PELOUSE

#GAUCHE
penup()
goto(-700, -330)
pendown()
color("green")
begin_fill()
setheading(90)
forward(150)
right(90)
forward(640)
right(145)
forward(260)
right(35)
forward(420)
end_fill()

# DROITE
penup()
goto(60, -180)
pendown()
color("green")
begin_fill()
setheading(0)
forward(620)
right(90)
forward(150)
right(90)
forward(360)
end_fill()


# ###### SOLEIL
penup()
goto(-500, 380)
pendown()
color("yellow")
cercle(40)

done()