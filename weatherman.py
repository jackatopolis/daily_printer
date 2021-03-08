#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:43:26 2021

@author: jackcohen
"""


# WEATHERMAN BY JACK COHEN

# INITIALIZATION
from datetime import datetime
now = datetime.now()
print ("Run timestamp: "+"%02d/%02d/%04d %02d:%02d:%02d" % (now.month,now.day,now.year,now.hour,now.minute,now.second))
print("")
print("Hi there, welcome to Weatherman!")
print("")
import requests
import urllib.request
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd 
import matplotlib.image as mpimg
import matplotlib.patches as mpatches
import numpy as np
from PIL import Image


# LOADING DATA
URL = "https://geocode.search.hereapi.com/v1/geocode"
location = input("Enter the location here: ")
api_key = '79rH_WxbI6HbFPGcvqbDp8P1XBauxba73x5AoZg3XUc'
PARAMS = {'apikey':api_key,'q':location} 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()

lat = data['items'][0]['position']['lat']
lon = data['items'][0]['position']['lng']
print("Coordinates: "+str(lat)+", "+str(lon))

weatherdata=requests.get("http://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(lon)+"&exclude={part}&units=metric&appid=14c1a478a1f329548614959a7d09bd4b")

dict=weatherdata.json()


#FUNCTIONS
def current(f):
    return dict['current'][f]
def daily(f):
    return dict['daily'][f]
def hourlytemp(c):
    return dict['hourly'][c]['temp']
def hourtime(i):
    return dict['hourly'][i]['dt']+dict['timezone_offset']
def dailytime(w):
    return dict['daily'][w]['dt']+dict['timezone_offset']
def unixtime(j):
    return datetime.utcfromtimestamp(j).strftime("%m/%d/%Y %H:%M:%S")
def unixtimer(j):
    return datetime.utcfromtimestamp(j).strftime("%m/%d %H:%M:%S")
def unixtimernosec(j):
    return datetime.utcfromtimestamp(j).strftime("%m/%d %H:%M")
def unixtimernomin(j):
    return datetime.utcfromtimestamp(j).strftime("%m/%d %H")
def unixtimerdate(j):
    return datetime.utcfromtimestamp(j).strftime("%m/%d")
def unixtimetime(j):
    return datetime.utcfromtimestamp(j).strftime("%H:%M")


# OUTPUTS
currenttime=dict['current']['dt']+dict['timezone_offset']

print("")
print("Weather data was last updated "+unixtime(currenttime))
print("")

desire=input("Would you like to know current weather, hourly forecast, or daily forecast? ")
desire=desire.lower()
print("")
sunrisetime=dict['current']['sunrise']+dict['timezone_offset']
sunsettime=dict['current']['sunset']+dict['timezone_offset']
print("Sunrise : "+unixtimer(sunrisetime))
print("Sunset : "+unixtimer(sunsettime))
print("")

if "curr" in desire:
    descriptionnow=str(current('weather')[0]['description'])
    print("---CURRENT CONDITIONS---")
    print("")
    print("Main Weather : "+str(current('weather')[0]['main']))
    print("Description : "+descriptionnow.capitalize())
    print("")
    print("Temperature = "+str(current('temp'))+" C")
    print("Feels Like = "+str(current('feels_like'))+" C")
    print("Cloud Cover = "+str(current('clouds'))+"%")
    print("Pressure = "+str(current('pressure'))+" hPa")
    print("Humidity = "+str(current('humidity'))+"%")
    print("Dew Point = "+str(current('dew_point'))+" C")
    print("UV Index = "+str(current('uvi')))
    #print("Visibility = "+str(current('visibility'))+" m")  
    print("Wind Speed = "+str(current('wind_speed'))+" m/s")
    print("Wind Direction = "+str(current('wind_deg'))+" deg")
    print("")

    icon=current('weather')[0]['icon']
    urllib.request.urlretrieve("http://openweathermap.org/img/wn/"+str(icon)+"@2x.png", "weathericon.png")
    icons=requests.get("http://openweathermap.org/img/wn/"+str(icon)+"@2x.png")
    
    ID = str(current('weather')[0]['id'])
    if ID[0]=='2':
        print("Thunderstorms inbound!")
    elif ID[0]=='3':
        print("It's drizzle fo shizzle can't you see out the windizzle?")
    elif ID[0]=='5':
        print("Here comes the rain again...")
    elif ID[0]=='6':
        print("Let it snow! Let it snow! Let it snow!")
    elif ID[0]=='7':
        print("Something spooky is going on out there...")
    elif ID=='800':
        print("The skies are clear, boss!")
    elif ID=='801':
        print("It's just a lil bit cloudy.")
    elif ID=='802':
        print("It's just a lil bit cloudy.")
    elif ID=='803':
        print("It's pretty cloudy out there!")
    elif ID=='804':
        print("It's pretty cloudy out there!")
    print("")
    
    try:
        for x in range(len(dict['minutely'])):
            if dict['minutely'][0]['precipitation']!=0:
                print("")
                break
            elif dict['minutely'][x]['precipitation']!=0:
                print("")
                print("Rain will start at "+str(unixtimernosec(dict['minutely'][x]['dt']+dict['timezone_offset'])))
                break
    except:
        print("")
 
    img = mpimg.imread('weathericon.png') 
    plt.imshow(img)
    plt.axis('off')

elif "hour" in desire:
    print("---48 HOUR FORECAST---")
    Times=[]
    Timess=[]
    Feels_like=[]
    Temps=[]
    Pressure=[]
    Humidity=[]
    Clouds=[]
    Desc=[]
    DPT=[]
    Windspeed=[]
    Winddeg=[]
    for x in range(len(dict['hourly'])):
        L1=unixtimernosec(hourtime(x))
        L11=unixtimetime(hourtime(x))
        L2=dict['hourly'][x]['temp']
        L3=dict['hourly'][x]['pressure']
        L4=dict['hourly'][x]['humidity']
        L5=dict['hourly'][x]['feels_like']
        L6=dict['hourly'][x]['clouds']
        L7=dict['hourly'][x]['weather'][0]['main']+"-"+dict['hourly'][x]['weather'][0]['description'].capitalize()
        L8=dict['hourly'][x]['dew_point']
        L9=dict['hourly'][x]['wind_speed']
        L10=dict['hourly'][x]['wind_deg']
    
        Times.append(L1)
        Timess.append(L11)
        Desc.append(L7)
        Temps.append(L2)
        Feels_like.append(L5)
        Pressure.append(L3)
        Humidity.append(L4)
        Clouds.append(L6)
        DPT.append(L8)
        Windspeed.append(L9)
        Winddeg.append(L10)

    df = pd.DataFrame({'DESCRIPTION':Desc,'TEMP (C)':Temps,'FEELS (C)':Feels_like,'PRES. (hPa)':Pressure,
                   'HUM. (%)':Humidity,'CLOUDS (%)':Clouds,'DEW POINT (C)':DPT,
                   'WIND SPEED (m/s)':Windspeed,'WIND DIR. (deg)':Winddeg}) 
    df.index=Times
    print(df)

    print("")
    
    plt.plot(Times,Temps,c='red',label='Temp')
    plt.plot(Times,Feels_like,c='orange',label='Feels')
    plt.plot(Times,DPT,c='blue',label='Dew Point')
    x_ticks = np.arange(0, 48, 6)
    plt.xticks(x_ticks,rotation=-45)
    plt.legend()
    plt.ylabel('Temperature (C)')
    plt.suptitle('48 Hour Temperature Forecast')
    plt.grid(True)
    plt.show()
        
elif "daily" in desire:
    print("---8 DAY FORECAST---")

    Daysunrise=[]
    Daysunset=[]
    Times=[]
    Daytemps=[]
    Mintemps=[]
    Maxtemps=[]
    Nighttemps=[]
    Evetemps=[]
    Morntemps=[]
    Dayfeels=[]
    Nightfeels=[]
    Evefeels=[]
    Mornfeels=[]
    Pressure=[]
    Humidity=[]
    Clouds=[]
    Desc=[]

    for x in range(len(dict['daily'])):
        L0=unixtimetime(dict['daily'][x]['sunrise']+dict['timezone_offset'])
        L00=unixtimetime(dict['daily'][x]['sunset']+dict['timezone_offset'])
        L1=unixtimerdate(dailytime(x))
        L2=dict['daily'][x]['temp']['day']
        L21=dict['daily'][x]['temp']['min']
        L22=dict['daily'][x]['temp']['max']
        L23=dict['daily'][x]['temp']['night']
        L24=dict['daily'][x]['temp']['eve']
        L25=dict['daily'][x]['temp']['morn']
        L3=dict['daily'][x]['pressure']
        L4=dict['daily'][x]['humidity']
        L5=dict['daily'][x]['feels_like']['day']
        L51=dict['daily'][x]['feels_like']['night']
        L52=dict['daily'][x]['feels_like']['eve']
        L53=dict['daily'][x]['feels_like']['morn']
        L6=dict['daily'][x]['clouds']
        L7=dict['daily'][x]['weather'][0]['main']+"-"+dict['daily'][x]['weather'][0]['description'].capitalize()
    
        Daysunrise.append(L0)
        Daysunset.append(L00)
        Times.append(L1)
        Daytemps.append(L2)
        Mintemps.append(L21)
        Maxtemps.append(L22)
        Nighttemps.append(L23)
        Evetemps.append(L24)
        Morntemps.append(L25)
        Pressure.append(L3)
        Humidity.append(L4)
        Dayfeels.append(L5)
        Nightfeels.append(L51)
        Evefeels.append(L52)
        Mornfeels.append(L53)
        Clouds.append(L6)
        Desc.append(L7)

    df = pd.DataFrame({'SUNRISE':Daysunrise,'SUNSET':Daysunset,'DESCRIPTION':Desc,'MIN TEMP (C)':Mintemps,'MAX TEMP (C)':Maxtemps,
                   'MORN TEMP (C)':Morntemps,'DAY TEMP (C)':Daytemps,'EVE TEMP (C)':Evetemps,'NIGHT TEMP (C)':Nighttemps,
                   'MORN FEELS (C)':Mornfeels,'DAY FEELS (C)':Dayfeels,'EVE FEELS (C)':Evefeels,'NIGHT FEELS (C)':Nightfeels,
                   'PRES. (hPa)':Pressure,'HUM. (%)':Humidity,'CLOUDS (%)':Clouds})
    df.index=Times
    print(df)
    
    plt.plot(Times,Mintemps,c='red',label='Min')
    plt.plot(Times,Maxtemps,c='orange',label='Max')
    plt.plot(Times,Daytemps,c='blue',label='Day')
    plt.legend()
    plt.xticks(rotation=-45)
    plt.ylabel('Temperature (C)')
    plt.suptitle('Daily Temperatures')
    plt.grid(True)
    plt.show()
    
else:
    print("Input not understood. Try again!")

