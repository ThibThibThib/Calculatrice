import tkinter as tk
from math import * 
LARGEUR = 600
HAUTEUR = 700

# Création de la fenêtre principale (main window)
mon_app = tk.Tk()
mon_app.title('calculatrice')

# Création d'un widget Canvas (zone graphique)
surface_dessin = tk.Canvas(mon_app, width=LARGEUR, height=HAUTEUR, bg='white')
surface_dessin.pack(padx=5, pady=5)


#Texte du nombre 1
text1 = tk.StringVar()
text1.set("1")
label = tk.Label(mon_app, textvariable=text1, fg='black', bg = 'white',
                  font=('Arial',40))
label.place(x=70, y=225)

#Texte du nombre 2
text2 = tk.StringVar()
text2.set("2")
label = tk.Label(mon_app, textvariable=text2, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=220, y=225)

#Texte du nombre 3
text3 = tk.StringVar()
text3.set("3")
label = tk.Label(mon_app, textvariable=text3, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=370, y=225)

#Texte du +
textplus = tk.StringVar()
textplus.set("+")
label = tk.Label(mon_app, textvariable=textplus, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=520, y=225)

#Texte du nombre 4
text4 = tk.StringVar()
text4.set("4")
label = tk.Label(mon_app, textvariable=text4, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=70, y=325)

#Texte du nombre 5
text5 = tk.StringVar()
text5.set("5")
label = tk.Label(mon_app, textvariable=text5, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=220, y=325)

#Texte du nombre 6
text6 = tk.StringVar()
text6.set("6")
label = tk.Label(mon_app, textvariable=text6, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=370, y=325)

#Texte du -
textmoins = tk.StringVar()
textmoins.set("-")
label = tk.Label(mon_app, textvariable=textmoins, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=520, y=325)

#Texte du nombre 7
text7 = tk.StringVar()
text7.set("7")
label = tk.Label(mon_app, textvariable=text7, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=70, y=425)

#Texte du nombre 8
text8 = tk.StringVar()
text8.set("8")
label = tk.Label(mon_app, textvariable=text8, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=220, y=425)

#Texte du nombre 9
text9 = tk.StringVar()
text9.set("9")
label = tk.Label(mon_app, textvariable=text9, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=370, y=425)

#Texte du *
textfois = tk.StringVar()
textfois.set("*")
label = tk.Label(mon_app, textvariable=textfois, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=520, y=425)

#Texte du nombre 0
text0 = tk.StringVar()
text0.set("0")
label = tk.Label(mon_app, textvariable=text0, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=70, y=525)

#Texte du ,
textvir = tk.StringVar()
textvir.set(",")
label = tk.Label(mon_app, textvariable=textvir, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=220, y=525)

#Texte du =
textegal = tk.StringVar()
textegal.set("=")
label = tk.Label(mon_app, textvariable=textegal, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=370, y=525)

#Texte du  /
textdiv = tk.StringVar()
textdiv.set("/")
label = tk.Label(mon_app, textvariable=textdiv, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=520, y=525)

#Texte du DEL
textdel = tk.StringVar()
textdel.set("DEL")
label = tk.Label(mon_app, textvariable=textdel, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=30, y=625)

#Texte du %
textpour = tk.StringVar()
textpour.set("%")
label = tk.Label(mon_app, textvariable=textpour, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=200, y=625)

#Texte du total
texttotal = tk.StringVar()
texttotal.set("Total : ")
label = tk.Label(mon_app, textvariable=texttotal, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=50, y=50)

#Texte du resultat
textresult = tk.StringVar()
textresult.set("")
label = tk.Label(mon_app, textvariable=textresult, fg='black',bg = 'white',
                  font=('Arial',40))
label.place(x=300, y=50)




def calcul (event):
    global case1, case2, case3, case4, case5, case6, case7, case8, case9, case0, casevir, caseplus, casemoin, casepour, casedel, casediv, caseegal, casefois
    X = event.x
    Y = event.y
    

    case1 = False
    case2 = False
    case3 = False
    case4 = False
    case5 = False
    case6 = False
    case7 = False
    case8 = False
    case9 = False
    case0 = False
    casevir = False
    caseplus = False
    casemoin = False
    casepour = False
    casedel = False
    casediv = False 
    caseegal = False
    casefois = False

    if X < 600 and Y < 200:
        print("total")

    #1
    if X < 150 and  Y > 200 and Y < 300:
        case1 = True
        print ("1")

    #2
    if X > 150 and X < 300 and Y > 200 and Y < 300:
        case2 = True
        print ("2")

    #3
    if X > 300 and X < 450 and Y > 200 and Y < 300:
        case3 = True
        print ("3")

    #+
    if X > 450 and X < 600 and Y > 200 and Y < 300:
        caseplus = True
        print("+")

    #4
    if X < 150 and Y > 300 and Y < 400:
        case4 = True
        print("4")

    #5
    if X > 150 and X < 300 and Y > 300 and Y < 400:
        case5 = True
        print("5")

    #6
    if X > 300 and X < 450 and Y > 300 and Y < 400:
        case6 = True
        print("6")

    #-
    if X > 450 and X < 600 and Y > 300 and Y < 400:
        casemoin = True
        print("-")
    
    #7
    if X < 150 and Y > 400 and Y < 500:
        case7 = True 
        print("7")
    
    #8
    if X > 150 and X < 300 and Y > 400 and Y < 500:
        case8 = True
        print("8")
    
    #9
    if X > 300 and X < 450 and Y > 400 and Y < 500:
        case9 = True
        print("9")

    #*
    if X > 450 and X < 600 and Y > 400 and Y < 500:
        casefois = True
        print("*")

    #0
    if X < 150 and Y > 500 and Y < 600:
        case0 = True
        print("0")

    #,
    if X > 150 and X < 300 and Y > 500 and Y < 600:
        casevir = True
        print(",")
    
    #=
    if X > 300 and X < 450 and Y > 500 and Y < 600:
        caseegal = True
        print("=")

    #/
    if X > 450 and X < 600 and Y > 500 and Y < 600:
        casediv = True
        print("/")    

    #DEL
    if X < 150 and Y > 600 and Y < 700:
        casedel = True
        print("DEL")

    #%
    if X > 150 and X < 300 and Y > 600 and Y < 700:
        casepour = True
        print("%")

    #Je sais pas
    if X > 300 and X < 450 and Y > 600 and Y < 700:
        print("Je sais pas")

    #Je sais pas
    if X > 450 and X < 600 and Y > 600 and Y < 700:
        print("Je sais pas")



    #Chiffre
    if case1 == True: 
        case1 = 1
    elif case2 == True:
        case2 = 2
    elif case3 == True:
        case3 = 3
    elif case4 == True:
        case4 = 4
    elif case5 == True:
        case5 = 5
    elif case6 == True:
        case6 = 6
    elif case7 == True:
        case7 = 7
    elif case8 == True:
        case8 = 8
    elif case9 == True:
        case9 = 9
    elif case0 == True:
        case0 = 0  


    
    #Signe
    elif casedel == True :
        print("efface tout")
    elif casediv == True:
        print("Division")
    elif caseegal == True:
        print ("égal")
    elif casefois == True:
        print("fois")
    elif caseplus == True:
        print("plus")
    elif casemoin == True:
        print("Moins")
    elif casepour == True:
        print("pourcentage")
    elif casevir == True:
        print("virgule")



#vertical
surface_dessin.create_line(5, 200, 5, 700, fill="black", width=5)
surface_dessin.create_line(150, 200, 150, 700, fill="black", width=5)
surface_dessin.create_line(300, 200, 300, 700, fill="black", width=5)
surface_dessin.create_line(450, 200, 450, 700, fill="black", width=5)
surface_dessin.create_line(598, 200, 598, 700, fill="black", width=5)

#HORIZONTAL
surface_dessin.create_line(0, 200, 600, 200, fill="black", width=5)
surface_dessin.create_line(0, 300, 600, 300, fill="black", width=5)
surface_dessin.create_line(0, 400, 600, 400, fill="black", width=5)
surface_dessin.create_line(0, 500, 600, 500, fill="black", width=5)
surface_dessin.create_line(0, 600, 600, 600, fill="black", width=5)
surface_dessin.create_line(0, 700, 600, 700, fill="black", width=5)


#Autour du total
surface_dessin.create_line(40, 30, 560, 30, fill="black", width=5)
surface_dessin.create_line(40, 30, 40, 130, fill="black", width=5)
surface_dessin.create_line(40, 130, 560, 130, fill="black", width=5)
surface_dessin.create_line(560, 30, 560, 130, fill="black", width=5)




# La méthode bind() permet de lier un événement avec une fonction :
# un clic gauche sur la surface provoquera l'appel de la fonction clic()
surface_dessin.bind('<Button-1>', calcul)
surface_dessin.pack(padx=5, pady=5)



# Scanne toute la page
mon_app.mainloop()