from wifi_manager import WifiManager
from machine import Pin, SoftI2C, WDT
import urequests, utime, ssd1306

#VARIABLES
sort = {'Diesel':False,'E10':True,'E5':False}#choose important fuel
lat = #set your latitute
lng = #set your longitude
radius = 3#needs to be adjusted if memory error or no stations close enough
key = ''#insert api key

#display
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
display = ssd1306.SSD1306_I2C(128, 32, i2c)

display.text('connecting wifi',0,0,1)
display.text('or setup wifi on',0,8,1)
display.text('192.168.4.1',0,16,1)
display.show()

#wifi
wm = WifiManager('Petrol-Station','12345678')
wm.connect()

#show station data on display
def visualize(station:dict, white=False):
    if station == {} or not station['isOpen']:
        display.poweroff()
        display.show()
        return
    display.poweron()
    color = 1
    display.fill(0)
    if white:
        color = 0
        display.fill(1)

    brand = station['brand']
    display.text(brand,int((8-(len(brand)/2))*8) ,0,color)
    display.text('Diesel:',0,8,color)
    display.text(station['Diesel'],85,8,color)
    display.text('E10:',0,16,color)
    display.text(station['E10'],85,16,color)
    display.text('Super:',0,24,color)
    display.text(station['E5'],85,24,color)
    display.show()

#key for sorting results
def sortKey():
    for fuel in sort:
        if sort[fuel]:
            return fuel

#data collecting
rawStations = {}
meanPrice = 1
def getData():
    global meanPrice, rawStations
    print('collecting Data')
    
    stationsresponse = urequests.get('https://creativecommons.tankerkoenig.de/json/list.php?lat='+str(lat)+'&lng='+str(lng)+'&rad='+str(radius)+'&sort=dist&type=all&apikey='+key).json()
    rawStations = stationsresponse['stations']
    
    #gather meanPrice
    meanresponse = urequests.get('https://creativecommons.tankerkoenig.de/api/v4/stats?apikey='+key).json()
    meanPrice = meanresponse[sortKey()]['mean']

cheapest = {}
def prepData():
    global cheapest
    if rawStations == {}:
        return
    stations = {}
    for station in rawStations[:5]:#reducing to 5 stations and cleaining data
        if station['brand'] not in stations:
            stations[station['brand']] = {'brand':station['brand'],'isOpen':station['isOpen'],'E5':station['e5'],'E10':station['e10'],'Diesel':station['diesel']}
    #finding cheapest station
    if stations != {}:
        cheapest = list(stations.values())[0]
    for station in stations:
        stationData = stations[station]
        if stationData[sortKey()] < cheapest[sortKey()] and stationData['isOpen']:
            cheapest = stations[station]

display.text('wifi connected',0,24,1)
display.show()

getData()
prepData()
animToggle = True
counter = 1
while True:
    utime.sleep(2)
    if(cheapest != {} and cheapest[sortKey()]<meanPrice*0.8):
        visualize(cheapest, animToggle)
        animToggle = not animToggle
    else:
        visualize(cheapest)
    if counter == 300:
        getData()
        prepData()
        counter = 0
    counter = counter+1

