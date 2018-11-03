from darksky import forecast
from datetime import datetime as dt

def convertLaunchDate(year, month, day):
    return dt(year, month, day).isoformat()

def getStatus():
    DSKEY = '02382e7114e768e2588b030ae3803832'
    coords = (37.8716, 122.2727)
    forecast = getWeather(coords, convertLaunchDate(2018, 10, 3), DSKEY)
    return forecast

def getWeather(coords, date, DSKEY):
    lat = coords[0]
    lng = coords[1]
    weatherRaw = (forecast(DSKEY, lat, lng, time=date, units="si"))
    try:
        type = weatherRaw.icon
    except:
        type = 0
    try:
        temp = weatherRaw.temperature
    except:
        temp = None
    return {"Weather": type, "Temp": temp}
