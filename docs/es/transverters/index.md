# Transversores

Los transversores funcionan cambiando la gama de frecuencias que el transmisor puede recibir y transmitir.

# Transversor UR3LMZ

Alexander [ur3lmz](mailto:ur3lmz@gmail.com) vende un transversor muy bueno y dependiendo del modelo, tiene una frecuencia de entrada en VHF o en UHF.

<img height="300" src="/../_img/transverter/transv.jpg" />
<img height="300" src="/../_img/transverter/transv_inside.jpg" />

La única diferencia entre la versión UHF y la VHF son las frecuencias programadas en el ADF4351 y la bobina L1.

<img height="400" src="/../_img/transverter/uhf_diagram.png" />
<img height="400" src="/../_img/transverter/vhf_diagram.png" />

La potencia de entrada es de alrededor de 2W y la salida está entre 12-13W mientras se alimenta con 12v DC
Dependiendo de la versión la frecuencia es 200Mhz más baja (455Mhz -> 255mhz) o 100 Mhz más alta (155mhz -> 255mhz)  

Finalmente con el selector en la parte frontal se elige el Tx Offset (se puede cambiar cuando encargas el transverter)

1. 33.6Mhz
2. 41Mhz
3. 47.225Mhz

En la parte trasera hay 3 conectores BNC. Uno para conectar el transmisor, el del medio para conectar una antena UHV/VHF estándar que se utilizará 
cuando el transversor esté apagado y el último para conectar una antena Satcom.

```
Por ejemplo si tienes la versión UHF y estás en frecuencia RX y Tx = 455.50mhz con el selector en la posición 2

Frecuencia Rx = 255.50mhz
Frecuencia Tx = 296.55mhz (255.50 + 41)
```

La frecuencia es controlada por el chip ADF4351 mediante un attiny13

<img height="400" src="/../_img/transverter/adf.jpg" />
<img height="400" src="/../_img/transverter/adf_pinout.jpg" />

En caso de que quieras tener los siguientes offsets:
1. 33.6Mhz
2. 41Mhz
3. 0 (TX=RX)

Puedes usar el siguiente [firmware](https://satcomradio.github.io/_files/sint13.hex) y subirlo mediante una 
[arduino](https://ecetechprojects.wordpress.com/2011/08/06/arduino-upload-hex-files-to-attiny85-using-your-arduino-and-avrdude/) 
al attiny13 del controlador de frecuencia (solo para la version UHF)

# Transversor R1ZH

Puede encontrar más información sobre este transversor (en ruso) [aquí](http://r1zh.ru/satcom3/satcom3.htm)

<img height="400" src="/../_img/transverter/r1zh_diagram.png" />