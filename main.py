from tkinter import *
import requests
import json    

city = "Paris"
API = "33f784258bbf921ad48a2b9b3d06d4c6"
units = "metric"
lang = "fr"

def meteo_window():
    #Creation fenetre
    meteo = Tk()

    #Paramètre de la fenêtre
    meteo.title("Meteor")
    meteo.geometry("740x510")
    meteo.minsize(740, 510)
    window.minsize(740, 510)
    meteo.iconbitmap("meteor.ico")
    meteo.config(background='#00C5FE')

def search():
    city=entry
    url="http://api.openweathermap.org/data/2.5/weather?q=" + entry + "&appid=33f784258bbf921ad48a2b9b3d06d4c6&units=metric&lang=fr"
    response = resquets.get(url)
    weather= (response.json())
    meteo_window()
    label_title = Label(window, text=print(weather), font=("Arial", 40), bg='#00C5FE', fg='white')
    label_title.pack()


#Creation fenetre
window = Tk()

#Paramètre de la fenêtre
window.title("Meteor")
window.geometry("740x510")
window.minsize(740, 510)
window.maxsize(740, 510)
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
label_title = Label(frame, text="Bienvenue sur Meteor", font=("Arial", 40), bg='#00C5FE', fg='white')
label_title.pack()

#texte2
label_subtitle = Label(frame, text="Votre temps par tous les temps", font=("Arial", 20), bg='#00C5FE', fg='white')
label_subtitle.pack()

#champs d'écriture
entry = Entry(frame, text="Insérer la ville ", font=("Arial", 20), bg='white', fg='black')
entry.pack(pady=50)

#bouton1
button = Button(frame, text="Chercher", font=("Arial", 20), bg='white', fg='black', bd=1, relief=SUNKEN, command=search)
button.pack()

#enpacktage
frame.pack(expand=YES)

#afficher
window.mainloop()
