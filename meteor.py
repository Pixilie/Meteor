import tkinter
from tkinter import *
import requests
import json
import time
import webbrowser

API = "token"

# Dictionnaire des textes affichés (pour une langue en entrée)
def get_dictionnaire (langue):
    dictionnaires = {
        'Français': {
            'welcome': 'Bienvenue sur Meteor',
            'slogan': 'Votre temps par tous les temps',
            'weather': 'Temps',
            'weather_of': 'Météo de la ville de',
            'search' : 'Rechercher',
            'choose_langage' : 'Choisissez votre langue',
            'temp' : 'Température',
            'min_temp' : 'Température minimale',
            'max_temp' : 'Température maximum',
            'date_hour' : 'Date & heure',
            'Name' : 'Nom',
            'country' : 'Pays',
            'felt_temp' : 'Température ressenti',
            'humidity' : 'Humidité',
            'pressure' : 'Pression',
            'wind_speed' : 'Vitesse du vent',
            'percentage_clouds' : 'Pourcentage de nuage',
            'sunset' : 'Le soleil se couchera à',
            'sunrise' : "Le soleil s'est levé à",
            'parameter' : "Paramètres"
        }, 'English': {
            'welcome': 'Welcome on Meteor',
            'slogan': 'Your weather in any weather',
            'weather': 'Weather',
            'weather_of': 'Weather of',
            'search' : 'Search',
            'choose_langage' : 'Choose your langage',
            'temp' : 'Temperature',
            'min_temp' : 'Minimum temperature',
            'max_temp' : 'Maximum temperature',
            'date_hour' : 'Date & hour',
            'Name' : 'Name',
            'country' : 'Country',
            'felt_temp' : 'Felt temperature',
            'humidity' : 'Humidity',
            'pressure' : 'Pressure',
            'wind_speed' : 'VWind speed',
            'percentage_clouds' : 'Percentage of clouds',
            'sunset' : 'The sun will set at',
            'sunrise' : "The sun rose at",
            'parameter' : "Parameter"
        }
    }
    dictionnaire = dictionnaires.get (langue)
    return dictionnaire

# Récupération d'un libellé (pour un identifiant et une langue)
def get_label(label, langue):
    dictionnaire = get_dictionnaire (langue)
    new_label = dictionnaire.get (label)
    return new_label

# Création fenêtres des paramètres
def setting_window():
    #Création fenetre
    global setting
    setting = Toplevel()
    langue = var_langue.get()
    #Paramètre de la fenêtre
    parameter_txt=get_label('parameter', langue)
    setting.title(parameter_txt)
    setting.geometry("340x210")
    setting.minsize(340, 210)
    setting.maxsize(340, 210)
    setting.iconbitmap("app_icon\meteor.ico")
    setting.config(background='#00C5FE')

    #Textes
    langue_text = StringVar()
    langue_text.set (get_label('choose_langage', langue))
    text_units = Label(setting, textvariable=langue_text, font=("Arial", 15), bg='#00C5FE', fg='white')
    text_units.place(x=10, y=10)

    option_langue = OptionMenu(setting, var_langue, *langues, command=change_langue)
    option_langue.config(width=10, font=('Arial', 12))
    option_langue.place(x=10, y=50)

def change_langue(self):
    langue = var_langue.get()
    welcome_text.set (get_label('welcome', langue))
    slogan_text.set (get_label('slogan', langue))
    search_text.set (get_label('search', langue))
    setting.destroy()

# Création et affichage des informations météo (appel api et traitement réponse)
def search():
    city = entry.get()
    if city != '':
        url="http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&lang=fr&appid=" + API
        response = requests.get(url)
        response_json = (response.json())
        print (response_json)
        meteo = meteo_window()
        display_info_meteo(meteo, response_json)

def display_info_meteo(window, response_json):
    city = entry.get()
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

    langue = var_langue.get()
    meteo_title_lbl = get_label ('weather_of', langue) + " " + city
    titre = Label(window, text=meteo_title_lbl, font=("Arial", 30), bg='#00C5FE', fg='white')
    titre.pack()

    # 1er ligne - ville
    name_text = get_label('Name', langue)
    name_lbl = Label(window, text=name_text, font=("Arial", 15), bg='#00C5FE', fg='white')
    name_lbl.place(x=130,y =90)
    city_lbl = Label(window, text=city, font=("Arial", 15), bg='#00C5FE', fg='white')
    city_lbl.place(x=380,y =90)
    # 2ème ligne - pays
    country_st_text = get_label('country', langue)
    country_st_lbl = Label(window, text=country_st_text, font=("Arial", 15), bg='#00C5FE', fg='white')
    country_st_lbl.place(x=130,y =120)
    country_lbl = Label(window, text=str(country), font=("Arial", 15), bg='#00C5FE', fg='white')
    country_lbl.place(  x=380,y =120)
    # 3ème ligne - date et heure
    date_text = get_label('date_hour', langue)
    date_st_lbl = Label(window, text=date_text, font=("Arial", 15), bg='#00C5FE', fg='white')
    date_st_lbl.place(x=130,y =150)
    date_lbl = Label(window, text=date_info, font=("Arial", 15), bg='#00C5FE', fg='white')
    date_lbl.place(  x=380,y =150)
    # 4ème ligne - temps
    weather_txt = get_label('weather', langue)
    weather_st_lbl = Label(window, text=weather_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    weather_st_lbl.place(x=130,y =180)
    weather_lbl = Label(window, text=str(description), font=("Arial", 15), bg='#00C5FE', fg='white')
    weather_lbl.place(x=380,y =180)
    # 5ème ligne - temperature
    temp_st = get_label ('temp', langue)
    temp_st_lbl = Label(window, text=temp_st, font=("Arial", 15), bg='#00C5FE', fg='white')
    temp_st_lbl.place(x=130,y =210)
    temp_lbl = Label(window, text=str(temp)+ " °C", font=("Arial", 15), bg='#00C5FE', fg='white')
    temp_lbl.place(x=380,y =210)
    # 6ème ligne - température min
    temp_min_txt = get_label('min_temp', langue)
    temp_min_st_lbl = Label(window, text=temp_min_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    temp_min_st_lbl.place(x=130,y =240)
    temp_min_lbl = Label(window, text=str(temp_min) + " °C", font=("Arial", 15), bg='#00C5FE', fg='white')
    temp_min_lbl.place(x=380,y =240)
    # 7ème ligne - température max
    temp_max_txt = get_label('max_temp', langue)
    temp_max_st_lbl = Label(window, text=temp_max_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    temp_max_st_lbl.place(x=130,y =270)
    temp_max_lbl = Label(window, text=str(temp_max) + " °C", font=("Arial", 15), bg='#00C5FE', fg='white')
    temp_max_lbl.place(x=380,y =270)
    # 8ème ligne - température ressentie
    felt_temp_txt = get_label('felt_temp', langue)
    felt_temp_st_lbl = Label(window, text=felt_temp_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    felt_temp_st_lbl.place(x=130,y =300)
    felt_temp_lbl = Label(window, text=str(ressenti) + " °C", font=("Arial", 15), bg='#00C5FE', fg='white')
    felt_temp_lbl.place(x=380,y =300)
    # 9ème ligne - humidité
    humidity_txt = get_label('humidity', langue)
    humidity_st_lbl = Label(window, text=humidity_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    humidity_st_lbl.place(x=130,y =330)
    humidity_lbl = Label(window, text=str(humidity) + " %", font=("Arial", 15), bg='#00C5FE', fg='white')
    humidity_lbl.place(x=380,y =330)
    # 10ème ligne - pression
    pressure_txt = get_label('pressure', langue)
    pressure_st_lbl = Label(window, text=pressure_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    pressure_st_lbl.place(x=130,y =360)
    pressure_lbl = Label(window, text=str(pressure) + " hpa", font=("Arial", 15), bg='#00C5FE', fg='white')
    pressure_lbl.place(x=380,y =360)
    # 11ème ligne - vitesse du vent
    wind_speed_txt = get_label('wind_speed', langue)
    wind_speed_st_lbl = Label(window, text=wind_speed_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    wind_speed_st_lbl.place(x=130,y =390)
    wind_speed_lbl = Label(window, text=str(wind_speed) + " km/h", font=("Arial", 15), bg='#00C5FE', fg='white')
    wind_speed_lbl.place(x=380,y =390)
    # 12ème ligne - nuages
    percentage_clouds_txt = get_label('percentage_clouds', langue)
    percentage_clouds_st_lbl = Label(window, text=percentage_clouds_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    percentage_clouds_st_lbl.place(x=130,y =420)
    percentage_clouds_lbl = Label(window, text=str(clouds) + " %", font=("Arial", 15), bg='#00C5FE', fg='white')
    percentage_clouds_lbl.place(x=380,y =420)
    # 13ème ligne - lever soleil
    sunset_txt = get_label('sunset', langue)
    sunset_st_lbl = Label(window, text=sunset_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    sunset_st_lbl.place(x=130,y =450)
    sunset_lbl = Label(window, text=str(sunset_info), font=("Arial", 15), bg='#00C5FE', fg='white')
    sunset_lbl.place(x=380,y =450)
    # 14ème ligne - coucher soleil
    sunrise_txt = get_label('sunrise', langue)
    sunrise_st_lbl = Label(window, text=sunrise_txt, font=("Arial", 15), bg='#00C5FE', fg='white')
    sunrise_st_lbl.place(x=130,y =480)
    sunrise_lbl = Label(window, text=str(sunrise_info), font=("Arial", 15), bg='#00C5FE', fg='white')
    sunrise_lbl.place(x=380,y =480)

# Création fenêtre des informations Météo
def meteo_window():
    #Creation fenetre
    meteo = Toplevel()
    city = entry.get()

    #Paramètre de la fenêtre
    langue = var_langue.get()
    weather_of_lbl = get_label ('weather_of', langue)
    meteo.title(weather_of_lbl + " " +city)
    meteo.geometry("780x540")
    meteo.minsize(780, 540)
    meteo.maxsize(780, 540)
    meteo.iconbitmap("app_icon\meteor.ico")
    meteo.config(background='#00C5FE')
    return meteo

def callback(event):
    webbrowser.open_new("http://www.openweathermap.org")

# Programme principal
#  création de la fenêtre principale
main_window = tkinter.Tk ()

#  paramètres de la fenêtre
main_window.title("Meteor")
main_window.geometry("780x540")
main_window.minsize(780, 540)
main_window.maxsize(780, 540)
main_window.iconbitmap("app_icon\meteor.ico")
main_window.config(background='#00C5FE')

# variables
global langues
langues = ['Français', 'English']
global var_langue
var_langue = StringVar()
var_langue.set(langues[0])

langue = var_langue.get()

# image
width = 170
height = 165
image = PhotoImage(file="app_icon\meteor.png")
canvas = Canvas(main_window, width=width, height=height, bg='#00C5FE', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.pack(pady=20)

# boites
frame = Frame(main_window, bg='#00C5FE')

# texte titre principal : label_title
welcome_text = StringVar()
welcome_text.set (get_label('welcome', langue))
label_title = Label(frame, textvariable=welcome_text, font=("Arial", 40), bg='#00C5FE', fg='white')
label_title.pack()

# texte sous-titre : label_subtitle
slogan_text = StringVar()
slogan_text.set (get_label('slogan', langue))
label_subtitle = Label(frame, textvariable=slogan_text, font=("Arial", 20), bg='#00C5FE', fg='white')
label_subtitle.pack()

# champs de saisie : entry (saisie de la ville)
entry = Entry(frame, font=("Arial", 20), bg='white', fg='black')
entry.pack(pady=50)

# bouton de recherche : search_button
search_text = StringVar()
search_text.set (get_label('search', langue))
search_button = Button(frame, textvariable=search_text, font=("Arial", 20), bg='white', fg='black', bd=1, relief=SUNKEN, command=search)
search_button.pack()

# bouton des paramètres : setting_button
image_setting = PhotoImage(file='app_icon\setting_icon.png', width=50, height=50)
setting_button = Button(main_window, image=image_setting, bd=0, bg='#00C5FE', fg='black', relief=SUNKEN, command=setting_window)
setting_button.place(x=5, y=5)

# enpacktage
frame.pack(expand=YES)

# affichage fenêtre principal et attente événements (souris, clic, clavier)
main_window.mainloop ()
