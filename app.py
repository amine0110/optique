from tkinter import *
from PIL import Image
from PIL import ImageTk

bg='#00CC99'
app = Tk()
app.geometry('700x500')
app.title('Optique')
app.configure(bg=bg)

def taille_objet():
    taille_image = taille_box.get()
    focale_cal = focale_box.get()
    bague_allonge = bague_box.get()

    if taille_image and focale_cal and bague_allonge:
        taille_obj = float(focale_cal) * float(taille_image) / float(bague_allonge)
        return taille_obj

def distance_obj_CCD():
    taille_image = taille_box.get()
    focale_cal = focale_box.get()
    bague_allonge = bague_box.get()
    taille_obj = taille_objet()
    distance_o_ccd = 0
    if taille_image and focale_cal and bague_allonge:
        agrr = float(taille_image)/taille_obj

        p_prime = (agrr + 1) * float(focale_cal)
        p = p_prime/agrr

        distance_o_ccd = p + p_prime
    return distance_o_ccd

def affiche():
    taille_obj = taille_objet()
    dist_obj_ccd = distance_obj_CCD()

    affiche1 = "La taille de l'objet est: " + str(taille_obj) + "mm"
    affiche2 = "la distance entre l'objet et le capteur CCD: " + str(dist_obj_ccd) + "mm"

    lab1 = Label(fra3, text=affiche1, bg=bg)
    lab2 = Label(fra3, text=affiche2, bg=bg)

    lab1.grid()
    lab2.grid()

def clear():
    for item in fra3.winfo_children():
        item.destroy()
    focale_box.delete(0, END)
    bague_box.delete(0, END)
    taille_box.delete(0, END)



image = Image.open('Distance_focale.png')
image = image.resize((650,300), Image.ANTIALIAS)
image_printed = ImageTk.PhotoImage(image=image)

lab = Label(app, image=image_printed)
lab.pack()

fra = Frame(app, bg=bg)
fra.pack(pady=(20,0))

focale = Label(fra, text='Focale', bg=bg, font='agencyFB 10 bold')
focale.grid(row=0, column=0)
focale_box = Entry(fra, w=10, font='agencyFB 10')
focale_box.grid(row=0, column=1)

bague = Label(fra, text='Bague Allonge', bg=bg, font='agencyFB 10 bold')
bague.grid(row=0, column=2, padx=(20,0))
bague_box = Entry(fra, w=10, font='agencyFB 10')
bague_box.grid(row=0, column=3)

taille = Label(fra, text='Taille_CCD', bg=bg, font='agencyFB 10 bold')
taille.grid(row=0, column=4, padx=(20,0))
taille_box = Entry(fra, w=10, font='agencyFB 10')
taille_box.grid(row=0, column=5)

fra2 = Frame(app, bg=bg)
fra2.pack(pady=(20,0))

calculer = Button(fra2, text='Calculer', width=30, command=affiche)
calculer.grid()

clear = Button(fra2, text='Clear', width=30, command=clear)
clear.grid(pady=(10,0))

fra3 = Frame(app, bg=bg)
fra3.pack()








app.mainloop()