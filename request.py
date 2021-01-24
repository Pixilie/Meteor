def search():
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + str(entry) + "&appid=" + API + "&units=" + units + "&lang=" + lang
    response = requests.get(url)
    weather = (response.json())
    
    meteo = Tk()
    meteo.title("Météo de" + entry)
    meteo.geometry("740x510")
    meteo.minsize(740, 510)
    meteo.iconbitmap("meteor.ico")
    meteo.config(background='#00C5FE')
    label_title = Label(frame, text=print(weather), font=("Arial", 40), bg='#00C5FE', fg='white')
    label_title.pack()
