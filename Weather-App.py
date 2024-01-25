# https://www.airnowapi.org/aq/observation/zipCode/current/?
# format=application/json&zipCode=89129&distance=5&API_KEY=0C592B9C-AFA8-4DD2-9A85-252CEF4E57AB
#60610
from tkinter import *
import requests
import json

root = Tk()
root.title('Weather App')
root.geometry('600x100')

#create Zipcode Lookup Functions

def ziplookup():
    global label
    #word.winfo_exists() this function returns 1 if the word exists and 0 if not
    if 'label' in globals():
        label.destroy()
        print('hello')

    try:
        api_request = requests.get('https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zip.get() +'&distance=5&API_KEY=0C592B9C-AFA8-4DD2-9A85-252CEF4E57AB')
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = '#0c0'
        elif category == 'Moderate':
            weather_color = '#FFFF00'
        elif category == 'Unhealthy for sensitive Groups':
            weather_color = '#FF9900'
        elif category == 'Unhealthy':
            weather_color = '#FF0000'
        elif category == 'Very Unhealthy':
            weather_color = '#990066'
        elif category == 'Hazardous':
            weather_color = '#660000'

        root.configure(background=weather_color)
        label = Label(root, text=city + ' Air Quality ' + str(quality) + ' ' + category, font=('Helvetica', 20), background=weather_color)
        label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = 'Error...'
# [{"DateObserved":"2023-01-28 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"Las Vegas",
# "StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"O3","AQI":21,"Category":{"Number":1,"Name":"Good"}},
# {"DateObserved":"2023-01-28 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"Las Vegas",
# "StateCode":"NV","Latitude":36.206,"Longitude":-115.223,"ParameterName":"PM2.5","AQI":67,"Category":{"Number":2,"Name":"Moderate"}},
# {"DateObserved":"2023-01-28 ","HourObserved":7,"LocalTimeZone":"PST","ReportingArea":"Las Vegas","StateCode":"NV","Latitude":36.206,
# "Longitude":-115.223,"ParameterName":"PM10","AQI":39,"Category":{"Number":1,"Name":"Good"}}]


zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+N+S+E)

zipButton = Button(root, text='Loolup Zipcode', command=ziplookup)
zipButton.grid(row=0, column=1, sticky=W+N+S+E)

root.mainloop()
