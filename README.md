# Mini Gas-Pump
Mini Gas-Pump model that displays the currenty cheapest gas prices from stations nearby

![image](https://user-images.githubusercontent.com/35639879/156648782-312177d0-bfed-444b-b084-1dd066d40fa7.png)


This Project uses the https://creativecommons.tankerkoenig.de/ api so it only works in germany or the code needs to be adjusted

How to build it yourself:

| Hardware needed:                                  |
|---------------------------------------------------|
| Esp8266 d1 mini                                   |
| 0,91 OLED Display I2C SSD1306 Chip 128 x 32 Pixel |
| Some wires and a 3d printer for the case          |

| How to set it up:                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.You need an api key, you can get it here: https://creativecommons.tankerkoenig.de/                                                                                                                                             |
| 2.Then you need Thonny to easily upload the code. Download here https://thonny.org/                                                                                                                                              |
| 3.You need the Micropython Firmware for your esp8266. For the d1 mini you need these: https://micropython.org/download/esp8266-1m/                                                                                               |
| 4.Connect the esp with your computer and open thonny                                                                                                                                                                             |
| 5.On the bottom right you can select the interpreter, select esp8266>install or update firmware>slect port and downloaded firmware and click install (go back to editor)                                                         |
| 6.Click on view and enable files, you should see files from your computer on the left and below that the files from the esp (if the esp does not show up, click the stop button/restart esp/change port at interpreter settings) |
| 7.Select all files downloaded from this git on the left side, right click and select upload                                                                                                                                      |
| 8.Open main.py on the esp filesystem adjust the important fuel if needed and insert your api key, lat and long (https://www.latlong.net/)                                                                                        |
| 9.hit strg+s and you should be good to go                                                                                                                                                                                        |

Wiring:
| ESP | Oled    |
|-----|---------|
| G   | GND     |
| 3v3 | VCC     |
| D2  | SDA     |
| D1  | SCK/SCL |
