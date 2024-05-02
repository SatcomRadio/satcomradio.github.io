# Amplifiers

Pirates reach the satellite with only 2W of power and a directional or dipole antenna. 
Having more power just make their voice stand out more and easier to be heard by deaf antennas.  

It doesn't make much sense to have more than 50W-60W of output power since the satellite repeater has a maximum power of 50W

## Aliexpress amplifier

To increase the transmit power they get one of the VHF/UHF amplifiers on aliexpress that run with the MITSUBISHI RA or M power modules

<img height="350" src="/../_img/amplifier/board.png" />
<img height="350" src="/../_img/amplifier/amplifier_chip.jpg" />

To make the amplifier work, ideally it needs a RA30H3340 power module altough some people use a RA55H3340, RA60H3340, RA30H2127M and others but with less output power.  

Those amplifiers usually work at 12 volts but some people increase their voltage up to a limit of 18 volts 
to get more power when they are running outside of their designated frequencies.  

Bear in mind that those amplifiers generate a lot of **heat**!  
You need to have a proper (and large) heatsink and an aluminium case for them  

Here you can see an example of the enclosure of an amplifier and a lowpass filter

<img height="400" src="/../_img/amplifier/ampli_case.png" />
<img height="400" src="/../_img/amplifier/ampli_case2.png" />

Here you can see a [Video](https://satcomradio.github.io/_img/amplifier/video.mp4) of this amplifier.  
The output power depends on the power module, the voltage and the input power.

### Power modules modification

There have been attempts to make modifications of the power modules and get over 100W of output power.  
Unfortunately they seem to be quite complex and it's just easier to combine multiple amplifiers.

<img height="300" src="/../_img/amplifier/pa_modification_simple.png" />
<img height="300" src="/../_img/amplifier/pa_modification_complex.png" />

Search `RA60H3340M1A` messages made by "Konstantin Z" on the russian Satcom [telegram](https://t.me/kosmo_konservatoria/221936) channel to see the details

## Custom amplifier

There's an amplifier made by P0150N in the russian Satcom [telegram](https://t.me/kosmo_konservatoria/173846) for RA3ZTQ but it's performance is not known

<img height="600" src="/../_img/amplifier/custom_amplifier.jpg" />

### Sources:

[Amplifier case](https://www.c4fmdmr.com/post/c%C3%B3mo-construir-un-amplificador-de-vhf-uhf-de-bajo-costo-para-un-ht-o-handy-por-rubens-ka6vha)  
[Amplifier manual](https://satcomradio.github.io/_pdf/amplifier/amplifier_manual.pdf)
