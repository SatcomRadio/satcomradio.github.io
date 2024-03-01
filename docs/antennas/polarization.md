# Circular Polarization

Since the satellites are spinning in their axis, we cannot use vertical or horizontal polarization as we would 
eventually reach 90 degrees between the satellite and our antenna polarization and we would not recieve the signal.

Therefore, we must use circular polarization

<img height="200" src="/../_img/antennas/horizontal_pol.gif" />
<img height="200" src="/../_img/antennas/vertical_pol.gif" />
<img height="200" src="/../_img/antennas/rh_pol.gif" />
<img height="200" src="/../_img/antennas/lh_pol.gif" />

To achieve circular polarization you can use a helical antenna or a cross yagi/turnstile.

If you are going to use a crossyagi or a turnstile since you're using 2 antennas you must match the impedance and you need to delay one of the signals. 
for the delay part, you can do it either by moving the vertical elements away from the horizontal elements or delaying the signal using 
wires if vertical and horizontal elements are in the same plane

## Wiring

<img height="400" src="/../_img/antennas/wires.png" />

Instead of RG58/RG59 you can use thinner wires, but you need to check their **velocity factor** in the datasheet of your cables.

In this example I will try to make a matching stub for 280mhz using RG179 and RG178.

```
RG179 (75ohm) VF=0,69 (69%)
RG178 (50ohm) VF=0.7 (70%)

280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

Phase Stub. One of the wires needs to be longer than the other one to delay the signal but both have to be of 50ohm
Short: (1.071/4)*0.7 = 0.187m
Long: (1.071/2)*0.7 = 0.374m

Matching stub. Both wires have to be of 75 ohm. The idea is to match the impedance of the 2 antenas
Length: 1.071/4*0.69 = 0.1847m
```

It's important how you connect the core of the cables! If you don't connect them properly you will not get **right hand** circular polarization.

<img height="450" src="/../_img/antennas/rhcp.png" />

## Hybrid couplers

If you don't want to deal with wires, you can also get a *Anaren 10260-3* or *Anaren 1B0260-3* hybrid coupler.

<img height="400" src="/../_img/antennas/anaren.jpg" />

This is what they use on professional antennas

<img height="500" src="/../_img/antennas/Prof.jpg" />

For the connections, you need to use a 50ohm resistor between the ground and the ISO pin

<img height="450" src="/../_img/antennas/anaren_conn.jpg" />
<img height="450" src="/../_img/antennas/anaren_conn2.jpg" />

With this you can make some really small antennas and be sure that the polarization is correct

<img height="400" src="/../_img/antennas/anaren_micro.jpg" />
<img height="400" src="/../_img/antennas/anaren_micro2.jpg" />

You can usually get them on ebay from old military radio equipments that have been dissasembled.

### Sources:

[Alicia Space](https://alicja.space/blog/how-to-build-turnstile-antenna/)  
[Qsl](https://www.qsl.net/sv1bsx/antenna-pol/polarization.html)  
[Anaren](https://twitter.com/tvoje___mama/status/1504770518033051684)
