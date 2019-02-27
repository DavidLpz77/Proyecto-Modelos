from tkinter import *
from EnlistCharacter import EnlistCharacter
import pygame, sys
from pygame.locals import *
from random import randint


class charChooserGUI:
    imageweapon = None

    def __init__(self, master):

        pygame.mixer.init()
        pygame.mixer.music.load('Musica/musica1.wav')
        pygame.mixer.music.play(-1)

        # ***** Parent Window Size ****
        master.minsize(width=1000, height=500)
        master.maxsize(width=1000, height=500)

        label = Label(bg="white")
        

        # **** Title ****

        title = Label(text="Seleciona un personaje", font="times 24 bold italic", fg="black", bg="white")
        title.pack(pady=(30, 0))

        # ***** Images ****

        img1 = PhotoImage(file="imagenes/brujaini.png")
        img2 = PhotoImage(file="imagenes/Demonio.png")
        img3 = PhotoImage(file="imagenes/enano.png")
        img4 = PhotoImage(file="imagenes/orco.png")

        char1 = Button(label, image=img1, command=lambda: self.chooseConjurer(master), bg="white",activebackground="white",border=0)
        char1.image = img1
        char1.grid(row=0, padx=10, pady=5)
        char2 = Button(label, image=img2, command=lambda: self.chooseWeapon(2, master), bg="white", activebackground="white",border=0)
        char2.image = img2
        char2.grid(row=0, column=1, padx=10, pady=5)
        char3 = Button(label, image=img3, command=lambda: self.chooseWeapon(3, master), bg="white",activebackground="white",border=0)
        char3.image = img3
        char3.grid(row=0, column=2, padx=10, pady=5)
        char4 = Button(label, image=img4, command=lambda: self.chooseWeapon(4, master), bg="white",activebackground="white",border=0)
        char4.image = img4
        char4.grid(row=0, column=3, padx=10, pady=5)

        # ****** Names *****

        name1 = Label(label, text="Bruja", font="times 10 bold italic", fg="#000000", bg="white")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Demonio", font="times 10 bold italic", fg="#000000", bg="white")
        name2.grid(row=1, column=1)
        name3 = Label(label, text="Enano", font="times 10 bold italic", fg="#000000", bg="white")
        name3.grid(row=1, column=2)
        name4 = Label(label, text="Orco", font="times 10 bold italic", fg="#000000", bg="white")
        name4.grid(row=1, column=3)

        # *** Adds the whole content that's on the label ***
        label.pack()

    def chooseConjurer(self, root):

        root.destroy()
        root2 = Tk()
        root2.title("Elije una bruja")
        root2.configure(bg="white")
        root2.minsize(width=660, height=460)

        # *** Main content ***

        label = Label(bg="white")

        #*** Inner content ***

        title = Label(text="De que lado quieres estar?", font="times 22 bold italic", fg="black", bg="white")
        title.pack(pady=(40, 0))

        img1 = PhotoImage(file="imagenes/bruja.png")
        img2 = PhotoImage(file="imagenes/bruja2.png")

        char1 = Button(label, image=img1, command=lambda: self.chooseWeapon(1, root2), bg="white", activebackground="white",border=0)
        char1.image = img1
        char1.grid(row=0, padx=(40,40), pady=10)
        char2 = Button(label, image=img2, command=lambda: self.chooseWeapon(5, root2), bg="white",activebackground="white",border=0)
        char2.image = img2
        char2.grid(row=0, column=1, padx=(40,40), pady=10)

        # ****** Names *****

        name1 = Label(label, text="Bruja Buena", font="times 10 bold italic", fg="black", bg="white")
        name1.grid(row=1, column=0)
        name2 = Label(label, text="Bruja Malvada", font="times 10 bold italic", fg="black", bg="white")
        name2.grid(row=1, column=1)

        label.pack()

    def chooseWeapon(self, raze, root):

        root.destroy()
        root2 = Tk()
        root2.title("Elejir arma")
        root2.configure(bg="white")
        root2.minsize(width=1000, height=600)

        # **** Content ***

        label = Label(bg="white")
        # **** Title ****

        title = Label(text="Elije tu arma", font="times 24 bold italic", fg="black", bg="white")
        title.pack(pady=(50, 0))

        # ***** Images ****
        raze1 = raze

        if (raze1 == 1) or (raze1 == 5):
            image1 = PhotoImage(file="imagenes/EpicScepter.png")
            image2 = PhotoImage(file="imagenes/HeavenlyScepter.png")
            image3 = PhotoImage(file="imagenes/Scepter.png")
            nameweapon = {1: "Cetro Demoniaco", 2: "Cetro Celestial", 3: "Cetro Mistico"}
            numweapon = {1: 1, 2: 2, 3: 3}
        if raze1 == 2:
            image1 = PhotoImage(file="imagenes/HadesSword.png")
            image2 = PhotoImage(file="imagenes/DamnBlade.png")
            image3 = PhotoImage(file="imagenes/DragonHammer.png")
            nameweapon = {1: "Espada de Hades", 2: "Cuchilla Maldita", 3: "Mazo de Dragon"}
            numweapon = {1: 4, 2: 5, 3: 6}
        if raze1 == 3:
            image1 = PhotoImage(file="imagenes/ExcaliburSword.png")
            image2 = PhotoImage(file="imagenes/Hammer.png")
            image3 = PhotoImage(file="imagenes/OdinSpear.png")
            nameweapon = {1: "Espada Excalibur", 2: "Martillo de Odin", 3: "Lanza de Paris"}
            numweapon = {1: 7, 2: 8, 3: 9}
        if raze1 == 4:
            image1 = PhotoImage(file="imagenes/DragonTail.png")
            image2 = PhotoImage(file="imagenes/MortalDagger.png")
            image3 = PhotoImage(file="imagenes/VampireSpear.png")
            nameweapon = {1: "Cuerno de Dragon", 2: "Daga Mortal", 3: "Hacha de Lava"}
            numweapon = {1: 10, 2: 11, 3: 12}

        char1 = Button(label, image=image1, command=lambda: self.createChar(raze, numweapon[1], nCharVar.get(), root2),
                       bg="white", activebackground="white",border=0)
        char1.image = image1
        char1.grid(row=0, padx=10, pady=5)
        char2 = Button(label, image=image2, command=lambda: self.createChar(raze, numweapon[2], nCharVar.get(), root2),
                       bg="white", activebackground="white",border=0)
        char2.image = image2
        char2.grid(row=0, column=1, padx=10, pady=5)
        char3 = Button(label, image=image3, command=lambda: self.createChar(raze, numweapon[3], nCharVar.get(), root2),
                       bg="white", activebackground="white",border=0)
        char3.image = image3
        char3.grid(row=0, column=2, padx=10, pady=5)

        # ****** Names *****

        name1 = Label(label, text=nameweapon[1], font="times 10 bold italic", fg="black", bg="white")
        name1.grid(row=1, column=0)
        name2 = Label(label, text=nameweapon[2], font="times 10 bold italic", fg="black", bg="white")
        name2.grid(row=1, column=1)
        name3 = Label(label, text=nameweapon[3], font="times 10 bold italic", fg="black", bg="white")
        name3.grid(row=1, column=2)

        # *** Adds the whole content that's on the label ***
        nCharMsj = Label(label, text="Elije Cuantos Oponentes quieres:", font="times 15 bold italic",
                         fg="black", bg="white")
        nCharMsj.grid(row=2, column=0, columnspan=2, sticky=E)

        nCharVar = StringVar(label)
        nCharVar.set("1")
        nChar = ["1", "2", "3"]

        nCharMenu = OptionMenu(label, nCharVar, *nChar)
        nCharMenu.config(width=5, font="times 15 bold italic", fg="black", bg="white",
                         highlightbackground="white", activebackground="#222222")
        nCharMenu.grid(row=2, column=2, pady=30)

        label.pack()

    def createChar(self, raze, weapon, nchar, root2):

        pygame.mixer.music.stop()

        root2.destroy()

        creacion = EnlistCharacter()
        creacion.createWeapon(weapon)
        creacion.createAurora()
        creacion.createCharacter(raze)

        creacion.BuildCharacter()

        personaje1 = None
        personaje12 = None
        personaje13 = None

        if nchar == "1":
            personaje1 = creacion.cloneCharacter()

        if nchar == "2":
            personaje1 = creacion.cloneCharacter()
            personaje12 = creacion.cloneCharacter()
        if nchar == "3":
            personaje1 = creacion.cloneCharacter()
            personaje12 = creacion.cloneCharacter()
            personaje13 = creacion.cloneCharacter()
        imweapon = personaje1.getWeapon().getImageWeapon()
        print(imweapon)
        imchar = personaje1.getImage()
        print(imchar)
        imAurora = personaje1.getAurora()
        print(imAurora)


        class Cursor(pygame.Rect):

            def __init__(self):
                pygame.Rect.__init__(self,0,0,1,1)
            def update(self):
                self.left,self.top=pygame.mouse.get_pos() 

        
        
        class BotonAtacar(pygame.sprite.Sprite):
            def __init__(self,imagen1,imagen2,x=-50,y=500):
                self.imagen_normal=imagen1
                self.imagen_seleccion=imagen2
                self.imagen_actual=self.imagen_normal
                self.rect=self.imagen_actual.get_rect()
                self.rect.left,self.rect.top=(50,500)

        class Boton(pygame.sprite.Sprite):
            def __init__(self,imagen1,imagen2,x=200,y=200):
                self.imagen_normal=imagen1
                self.imagen_seleccion=imagen2
                self.imagen_actual=self.imagen_normal
                self.rect=self.imagen_actual.get_rect()
                self.rect.left,self.rect.top=(x,y)

        

            def update(self,pantalla,cursor):
                if cursor.colliderect(self.rect):
                    self.imagen_actual=self.imagen_seleccion
                else: self.imagen_actual=self.imagen_normal

                pantalla.blit(self.imagen_actual,self.rect)


        class Animation():

            pygame.init()
            ventana = pygame.display.set_mode((1024, 683))
            SonidoEspada = pygame.mixer.Sound("Musica/samurai.wav")
            pygame.display.set_caption("personajes")

            atras1=pygame.image.load("imagenes/button11.png")
            atras2=pygame.image.load("imagenes/button1.png")

            boton1=Boton(atras1,atras2,0,0)
            cursor1=Cursor()
            r1=pygame.Rect(50,440,300,500)
            r2=pygame.Rect(400,440,300,500)
            r3=pygame.Rect(600,440,300,500)
            imagen_cursor=pygame.image.load("imagenes/cursor.png")
            pX=0
            pY=0
            cont1=1000
            cont2=1000
            cont3=1000
            imagen_arma = pygame.image.load(imweapon)
            imagen_personaje = pygame.image.load(imchar)
            imagen_aurora = pygame.image.load(imAurora)
            


            if (raze == 1) or (raze == 5):
                
                X = 0
                Y = 290
                X1 = 250
                Y1 = 290
                X2 = 500
                Y2 = 290
                posX = 100
                posY = 350
                posX1 = 350
                posY1 = 350
                posX2 = 600
                posY2 = 350
                positX = -15
                positY = 260
                positX1 = 235
                positY1 = 260
                positX2 = 485
                positY2 = 260
                
            if raze == 2:
                X = 135
                Y = 365
                X1 = 385
                Y1 = 365
                X2 = 640
                Y2 = 365
                posX = 150
                posY = 350
                posX1 = 400
                posY1 = 350
                posX2 = 660
                posY2 = 350
                positX = 30
                positY = 260
                positX1 = 280
                positY1 = 260
                positX2 = 530
                positY2 = 260
            if raze == 3:
                X = 35
                Y = 405
                X1 = 285
                Y1 = 405
                X2 = 535
                Y2 = 405
                posX = 150
                posY = 470
                posX1 = 400
                posY1 = 470
                posX2 = 650
                posY2 = 470
                positX = 25
                positY = 260
                positX1 = 275
                positY1 = 260
                positX2 = 525
                positY2 = 260
            if raze == 4:
                X = 125
                Y = 303
                X1 = 375
                Y1 = 303
                X2 = 625
                Y2 = 303
                posX = 120
                posY = 350
                posX1 = 370
                posY1 = 350
                posX2 = 620
                posY2 = 350
                positX = -15
                positY = 240
                positX1 = 235
                positY1 = 240
                positX2 = 485
                positY2 = 240

            fondo = pygame.image.load("fondo.jpg")
            boton2 = Boton(fondo,fondo,0,0)
            velocidad = 5
            verde = (0, 255, 0)
            derecha = True
            
            
            pygame.mixer.music.load('Musica/musica1.wav')
            pygame.mixer.music.play(-1)
            sangre = pygame.image.load("imagenes/sangre.png")
            wood = pygame.image.load("imagenes/2.png")
            while True:
                ventana.fill(verde)
                ventana.blit(fondo, (0, 0))
                if nchar == "1":
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                if nchar == "2":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                if nchar == "3":
                    ventana.blit(imagen_aurora, (positX, positY))
                    ventana.blit(imagen_personaje, (posX, posY))
                    ventana.blit(imagen_arma, (X, Y))
                    ventana.blit(imagen_aurora, (positX1, positY1))
                    ventana.blit(imagen_personaje, (posX1, posY1))
                    ventana.blit(imagen_arma, (X1, Y1))
                    ventana.blit(imagen_aurora, (positX2, positY2))
                    ventana.blit(imagen_personaje, (posX2, posY2))
                    ventana.blit(imagen_arma, (X2, Y2))
                ventana.blit(imagen_cursor, (pX,pY))
                ventana.blit(wood, (450,30))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        pintar_rect=False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if cursor1.colliderect(boton1.rect):
                            root = Tk()
                            root.title("Elejir Personaje")
                            root.configure(bg="white")

                            charChooser = charChooserGUI(root)
                            pygame.display.quit()
                            pygame.mixer.init()
                            pygame.mixer.music.load('Musica/musica1.wav')
                            pygame.mixer.music.play(-1)
                            root.mainloop() 
                            sys.exit()      
                        if cursor1.colliderect(r1):
                            pintar_rect=True
                            SonidoEspada.play()
                            ventana.blit(sangre,(0,300))
                            cont1=cont1-10
                            print(" vida:"+ str(cont1))
                            if cont1==0:
                                print("Te han matado")
                        if cursor1.colliderect(r2):
                            pintar_rect=True
                            SonidoEspada.play()
                            ventana.blit(sangre,(300,300))
                            cont1=cont1-10
                            print("vida:"+ str(cont1))
                            if cont1==0:
                                print("Te han matado")     
                        if cursor1.colliderect(r3):
                            pintar_rect=True
                            SonidoEspada.play()
                            ventana.blit(sangre,(600,300))
                            cont1=cont1-10
                            print("vida:"+ str(cont1))
                            if cont1==0:
                                print("Te han matado")
                                
                            
                                
                    if event.type == pygame.MOUSEBUTTONUP:
                        if cursor1.colliderect(r1):
                            ventana.blit(sangre,(0,350))
                        if cursor1.colliderect(r2):
                            ventana.blit(sangre,(300,350))
                        if cursor1.colliderect(r3):
                            ventana.blit(sangre,(550,350))

                keys = pygame.key.get_pressed()
                if keys[K_LEFT]:
                    positX -= velocidad
                    X -= velocidad
                    posX -= velocidad
                elif keys[K_RIGHT]:
                    positX += velocidad
                    posX += velocidad
                    X += velocidad
                if keys [K_a]:
                    positX1 -= velocidad
                    X1 -= velocidad
                    posX1 -= velocidad
                elif keys[K_d]:
                    positX1 += velocidad
                    posX1 += velocidad
                    X1 += velocidad
                if keys [K_j]:
                    positX2 -= velocidad
                    X2 -= velocidad
                    posX2 -= velocidad
                elif keys [K_l]:
                    positX2 += velocidad
                    posX2 += velocidad
                    X2 += velocidad
                if keys[K_SPACE]:
                    SonidoEspada.play()
                    personaje1.attack()
                fuente = pygame.font.Font("fuente/Sketch3D.otf",40)
                text1="Vida:"+str(cont1)
                texto1= fuente.render(text1,1,(155,127,22))
                ventana.blit(texto1,(500,50))
                
                cursor1.update()
                boton1.update(ventana,cursor1)
                pX,pY= pygame.mouse.get_pos()
                pX= pX-10
                pY= pY-10
                pygame.mouse.set_visible(False)
                pygame.display.flip()
                
                pygame.display.update()



# *** Defines window ***

root = Tk()
root.title("Seleccion de Personaje")
root.configure(bg="white")

charChooser = charChooserGUI(root)

root.mainloop()
