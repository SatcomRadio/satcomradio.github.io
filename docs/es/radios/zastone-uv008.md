# Zastone uv008

El Zastone (también se vende como Vitai) uv008 es un transmisor portatil capaz de comunicarse con Satcom en DMR.

<img height="450" src="/../_img/radios/zastone_uv008.png" />

Existen 3 versiones de esta radio. La única versión que funciona con satcom sin meterse con el software es v3 y como 
siempre y siempre que no compres un modelo usado, deberias recibir la versión v3

<img height="450" src="/../_img/radios/uv008_models.jpg" />

Tiene una potencia de unos 10W en las frecuencias de satcom.
Las únicas limitaciones son el firmware y el software para su programacion (CPS)

Para transmitir en DMR hay que tener el TX en el VFO A y el RX en el VFO B (o a la inversa) ya que el firmware no acepta offsets cuando se usa DMR

<img height="350" src="/../_img/radios/uv008_dmr.png" />

Además el CPS no es muy amigable y no puede importar canales o zonas.
Como solución, [aquí](https://satcomradio.github.io/_files/zastone_cps.cps) hay un ejemplo de un CPS con la mayoría de los canales Satcom.

También se puede conseguir el último firmware [aquí](https://satcomradio.github.io/_files/zastone_uv008_fw.rar)

Recientemente (Enero 2024) han habido intentos de desensamblar el firmware e implementar firwares personalizados.
Para hacerlo, se debe desensamblar el firmware .bin con el *cutter dissasembler* especificando *mcore* como arquitectura y *c-sky* como CPU.

Verifica el [foro VRTP](https://vrtp.ru/index.php?showtopic=33914&st=60) para las saber las ultimas novedades.

### Fuentes:

[Zastone info website](https://telegra.ph/Instrukciya-programmirovaniya-Zastone-UV008-v3-s-AES256-04-03)  
