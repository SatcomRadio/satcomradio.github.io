# Amplificadores

Los piratas llegan al satélite con sólo 2W de potencia y una antena direccional o dipolo. 
Tener mas potencia solo hace que su voz destaque mas y sea mas facil de ser escuchada por antenas sordas.  

No tiene mucho sentido tener mas de 50W-60W de potencia de salida ya que el repetidor del satelite tiene una potencia maxima de 50W

## Amplificador Aliexpress

Para aumentar la potencia de transmisión consiguen uno de los amplificadores VHF/UHF en aliexpress que funcionan con los módulos de potencia MITSUBISHI RA o M

<img height="350" src="/../_img/amplifier/board.png" />
<img height="350" src="/../_img/amplifier/amplifier_chip.jpg" />

Para que el amplificador funcione, lo ideal es un  módulo de potencia RA30H3340 aunque algunas personas utilizan un RA55H3340, RA60H3340, RA30H2127M u otros aunque con menor potencia de salida.  

Esos amplificadores suelen funcionar a 12 voltios, pero algunas personas aumentan su voltaje hasta un límite de 18 voltios 
para obtener más potencia cuando funcionan fuera de sus frecuencias designadas.  

Hay que tener en cuenta que estos amplificadores generan mucho **calor**  
Por ello se necesita un disipador adecuado (grande) y una carcasa de aluminio para ellos.  

Aquí se puede ver un ejemplo de la caja de un amplificador y un filtro paso bajo

<img height="400" src="/../_img/amplifier/ampli_case.png" />
<img height="400" src="/../_img/amplifier/ampli_case2.png" />

Aquí se puede ver un [Video](https://satcomradio.github.io/_img/amplifier/video.mp4) de este amplificador.  
La potencia de salida depende del módulo de potencia, del voltaje y de la potencia de entrada.

### Modificación de los módulos de potencia

Ha habido intentos de hacer modificaciones de los módulos de potencia y conseguir más de 100W de potencia de salida.  
Desafortunadamente parecen ser bastante complejos y es más fácil combinar varios amplificadores.

<img height="300" src="/../_img/amplifier/pa_modification_simple.png" />
<img height="300" src="/../_img/amplifier/pa_modification_complex.png" />

Busca los mensajes `RA60H3340M1A` realizados por "Konstantin Z" en el canal ruso Satcom [telegram](/telegram.md) para ver los detalles

## Amplificador personalizado

Hay un amplificador hecho por P0150N en el [telegram](/telegram.md) de Satcom ruso pero su rendimiento no es conocido

<img height="600" src="/../_img/amplifier/custom_amplifier.jpg" />

### Fuentes:

[Caja del amplificador](https://www.c4fmdmr.com/post/c%C3%B3mo-construir-un-amplificador-de-vhf-uhf-de-bajo-costo-para-un-ht-o-handy-por-rubens-ka6vha)  
[Manual del amplificador](https://satcomradio.github.io/_pdf/amplifier/amplifier_manual.pdf)