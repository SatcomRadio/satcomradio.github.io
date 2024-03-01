# Polarización circular

Dado que los satélites están girando en su eje, no podemos utilizar polarización vertical u horizontal ya que llegaríamos a 
llegaríamos a 90 grados entre la polarización del satélite y la de nuestra antena y no recibiríamos la señal.

Por lo tanto, debemos utilizar la polarización circular

<img height="200" src="/../_img/antennas/horizontal_pol.gif" />
<img height="200" src="/../_img/antennas/vertical_pol.gif" />
<img height="200" src="/../_img/antennas/rh_pol.gif" />
<img height="200" src="/../_img/antennas/lh_pol.gif" />

Para conseguir polarización circular puedes usar una antena helicoidal o una cross-yagi/turnstile.

Para usar una antenna de tipo cross-yagi o torniquete, debido a que contienen 2 antenas a 90º, se debe igualar la impedancia y retrasar una de las señales. 
Para retrasar la señal, se puede hacer alejando elementos verticales de los horizontales o retrasando la señal usando 
cables si los elementos verticales y horizontales están en el mismo plano

## Cableado

<img height="400" src="/../_img/antennas/wires.png" />

En lugar de RG58/RG59 se pueden usar cables más finos, pero es necesario comprobar su **factor de velocidad** (VF o velocity factor) en el datasheet de cables.
En este ejemplo se realiza un latiguilloe para 280mhz usando cables RG179 y RG178.

```
RG179 (75ohm) VF=0,69 (69%)
RG178 (50ohm) VF=0,7 (70%)

280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1,071m

Latiguillo de fase. Uno de los cables tiene que ser más largo que el otro para retrasar la señal pero ambos tienen que ser de 50ohm
Corto: (1,071/4)*0,7 = 0,187m
Largo: (1,071/2)*0,7 = 0,374m

Latiguillo de adaptación. Ambos cables deben ser de 75 ohmios. La idea es igualar la impedancia de las 2 antenas
Longitud: 1.071/4*0.69 = 0.1847m
```

Es importante cómo se conecta el núcleo de los cables. Si no se conectan correctamente no se obtendrá una **polarización circular hacia la derecha**.

<img height="450" src="/../_img/antennas/rhcp.png" />

## Acopladores híbridos

Si se quiere evitar lidiar con cables, se puedes utilizar un acoplador híbrido *Anaren 10260-3* o *Anaren 1B0260-3*.

<img height="400" src="/../_img/antennas/anaren.jpg" />

Es muy utilizado en las antenas profesionales

<img height="500" src="/../_img/antennas/Prof.jpg" />

Para las conexiones, se debe usar una resistencia de 50ohm entre la masa y el pin ISO

<img height="450" src="/../_img/antennas/anaren_conn.jpg" />
<img height="450" src="/../_img/antennas/anaren_conn2.jpg" />

De esta forma se pueden obtener antenas pequeñas y estar seguro de que la polarización es correcta

<img height="400" src="/../_img/antennas/anaren_micro.jpg" />
<img height="400" src="/../_img/antennas/anaren_micro2.jpg" />

Se suelen conseguir en ebay de equipos de radio militares antiguos desmontados.

### Fuentes:

[Alicia Space](https://alicja.space/blog/how-to-build-turnstile-antenna/)  
[Qsl](https://www.qsl.net/sv1bsx/antenna-pol/polarization.html)  
[Anaren](https://twitter.com/tvoje___mama/status/1504770518033051684)