# Transverters

Transverters work by changing the range of the frequencies that the transciever can communicate

# UR3LMZ Transverter

Alexander [ur3lmz](mailto:ur3lmz@gmail.com) sells a very good transverter and depending on the model, it has an input frequency in VHF or in UHF.

<img height="300" src="/../_img/transverter/transv.jpg" />
<img height="300" src="/../_img/transverter/transv_inside.jpg" />

The only difference between the UHF version and the VHF are the frequencies programmed in the ADF4351 and the L1 coil.

<img height="400" src="/../_img/transverter/uhf_diagram.png" />
<img height="400" src="/../_img/transverter/vhf_diagram.png" />

The input power is around 2W and the output is between 12-13W while being powered with 12v DC
Depending on the version the frequency is 200Mhz lower (455Mhz -> 255mhz) or 100 Mhz higher (155mhz -> 255mhz)  

Finally with the selector in the front you choose the Tx Offset (you can cuztomize them when ordering the transverter)

1. 33.6Mhz
2. 41Mhz
3. 47.225Mhz

There are 3 BNC connectors in the back. One for connecting the transmitter, the middle one to to connect a standard 
UHV/VHF antenna that will be used when the transverter is off and the last one to connect a satcom antenna.

```
For example if you have the UHF version and you are on frequency RX and Tx = 455.50mhz with the selector on position 2

Rx Frequency = 255.50mhz
Tx Frequency = 296.55mhz (255.50 + 41)
```

The frequency is controlled by the ADF4351 chip and a attiny13

<img height="400" src="/../_img/transverter/adf.jpg" />
<img height="400" src="/../_img/transverter/adf_pinout.jpg" />

If you want to have the following offsets:
1. 33.6Mhz
2. 41Mhz
3. 0 (TX=RX)

You can use the following [firmware](https://satcomradio.github.io/_files/sint13.hex) and upload it with an 
[arduino](https://ecetechprojects.wordpress.com/2011/08/06/arduino-upload-hex-files-to-attiny85-using-your-arduino-and-avrdude/) 
to the attiny13 of the frecuency controller (only for the UHF version).

# R1ZH Transverter

You can find more info about this transverter (in russian) [here](http://r1zh.ru/satcom3/satcom3.htm)

<img height="400" src="/../_img/transverter/r1zh_diagram.png" />