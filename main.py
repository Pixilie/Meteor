from tkinter import *

#Creation fenetre
window = Tk()

#Paramètre de la fenêtre
window.title("Meteor")
window.geometry("740x510")
window.minsize(740, 510)
window.iconbitmap("meteor.ico")
window.config(background='#00C5FE')

#image
width = 170
height = 165
image = PhotoImage(file="meteor.png")
canvas = Canvas(window, width=width, height=height, bg='#00C5FE', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(pady=20)

#Boites
frame = Frame(window, bg='#00C5FE') 

#Textes
#texte1
label_title = Label(frame, text="Bienvenue sur Meteor", font=("Arial", 40), bg='#00C5FE', fg='white')
label_title.pack()

#texte2
label_subtitle = Label(frame, text="Votre temps par tous les temps", font=("Arial", 20), bg='#00C5FE', fg='white')
label_subtitle.pack()

#champs d'écriture
entry = Entry(frame, text="Insérer la ville ", font=("Arial", 20), bg='white', fg='black')
entry.pack(pady=50)

#bouton1
button = Button(frame, text="Chercher", font=("Arial", 20), bg='white', fg='black', bd=1, relief=SUNKEN)
button.pack()

#enpacktage
frame.pack(expand=YES)

#afficher
window.mainloop()
