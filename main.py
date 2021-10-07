from tkinter import *
import requests 
import json
import time
import webbrowser

API = "33f784258bbf921ad48a2b9b3d06d4c6"


def callback(event):
    webbrowser.open_new("http://www.openweathermap.org")

def meteo_window():
    #Creation fenetre
    meteo = Tk()
    city = entry.get()
    
    #Paramètre de la fenêtre
    meteo.title("Metéo de la ville de " + city)
    meteo.geometry("740x510")
    meteo.minsize(740, 510)
    meteo.maxsize(740, 510)
    meteo.iconbitmap("app_icon\meteor.ico")
    meteo.config(background='#00C5FE')
    return meteo


def search():
    city = entry.get()
    url="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&lang=fr&appid=token"
    response = requests.get(url)
    response_json = (response.json())
    meteo = meteo_window()

    main_info = response_json.get('main')
    wind_info = response_json.get('wind')
    clouds_info = response_json.get('clouds')
    sys_info = response_json.get('sys')
    weather_info = response_json.get('weather')

    temp_max = main_info.get('temp_max')
    temp_min = main_info.get('temp_min')
    temp = main_info.get('temp')
    ressenti = main_info.get('feels_like')
    pressure = main_info.get('pressure')
    humidity = main_info.get('humidity')
    wind_speed = wind_info.get('speed')
    clouds = clouds_info.get('all')
    country = sys_info.get('country')
    sunrise = sys_info.get('sunrise')
    sunrise_info = time.ctime(sunrise)
    sunset = sys_info.get('sunset')
    sunset_info = time.ctime(sunset)
    timezone = sys_info.get('timezone')
    name = sys_info.get('name')
    date = response_json.get('dt')
    date_info = time.ctime(date)
    description = weather_info[0].get('description')
    icon = weather_info[0].get('icon')

    reponse = "Nom: " + city + "\n" + "Pays: " + str(country) + "\n" + "Date & Heure: " + date_info + "\n" + "Temps: " + str(description) + "\n" + "\n" + "\n" + "Température :" + str(temp) + " °C" + "\n" + "Température minimum: " + str(temp_min) + " °C"+ "\n" +  "Température maximum: " + str(temp_max) + " °C" + "\n" + "Température ressentie: " + str(ressenti) + " °C" + "\n" + "\n" + "Humidité: " + str(humidity) + " %" + "\n" + "Pression: " + str(pressure) + " hpa" + "\n" + "Vitesse du vent: " + str(wind_speed) + " km/h" + "\n" + "Pourcentage de nuage: " + str(clouds) + " %" + "\n" + "\n" + "Le soleil se couchera à: " + str(sunset_info) + "\n" + "Le soleil s'est levé: " + str(sunrise_info) + "\n"
        
    titre = Label(meteo, text="Météo de " + city, font=("Arial", 30), bg='#00C5FE', fg='white')
    titre.pack()
    temps = Label(meteo, text=reponse, font=("Arial", 15), bg='#00C5FE', fg='white')
    temps.pack()


#Creation fenetre
window = Tk()

#Paramètre de la fenêtre
window.title("Meteor")
window.geometry("740x510")
window.minsize(740, 510)
window.maxsize(740, 510)
window.iconbitmap("app_icon\meteor.ico")
window.config(background='#00C5FE')

#image
width = 170
height = 165
image = PhotoImage(file="app_icon\meteor.png")
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
entry = Entry(frame, text="Insérer la ville", font=("Arial", 20), bg='white', fg='black')
entry.pack(pady=50)

#bouton1
button = Button(frame, text="Chercher", font=("Arial", 20), bg='white', fg='black', bd=1, relief=SUNKEN, command=search)
button.pack()

def Setting_window():

    #Creation fenetre
    setting = Tk()

    #Boites
    frame_setting = Frame(setting, bg='#00C5FE')
    frame_setting.pack(expand=YES)
    
    #Paramètre de la fenêtre
    setting.title("Crédits")
    setting.geometry("740x510")
    setting.minsize(740, 510)
    setting.maxsize(740, 510)
    setting.iconbitmap("app_icon\meteor.ico")
    setting.config(background='#00C5FE')

    #Textes
    text_units = Label(frame_setting, text="Cette application a été créée par Kristen Couty et Thomas Bruno. \n Elle a été créée à l'aide de l'API openweathermap.org", font=("Arial", 15), bg='#00C5FE', fg='white')
    text_units.pack()

    #liens
    link = Label(frame_setting, text="OpenWeather Map", font=("Arial", 15), fg="blue", bg='#00C5FE', cursor="hand2")
    link.pack()
    link.bind("<Button-1>", callback)
    

#bouton parametre
image_setting = PhotoImage(file='app_icon\setting_icon.png', width=50, height=50)
setting = Button(window, image=image_setting, bd=0, bg='#00C5FE', fg='black', relief=SUNKEN, command=Setting_window)
setting.place(x=5, y=5)

#enpacktage
frame.pack(expand=YES)

#afficher
window.mainloop()
