# Turnstile antenna

This antenna is better than the dipole as it has circular polarization and it also has a reflector to avoid radiating towards the ground.
It's basically a cross-yagi without the director elements so it radiates in all directions.

<img height="450" src="/../_img/antennas/turnstile.png" />

For the VF of each material you can use this table:

| Material								| VF          |
| ------------------------------------- | ----------- |
| Aluminium								| 0.94        |
| Brass									| 0.95        |
| Copper								| 0.95        |
| Insulators (PVC,PE,Teflon)			| 0.94-0.98   |
| Iron									| 0.90        |
| Steel									| 0.90        |
| Insulated Copper (Copper*Insulator)	| 0.95*0.96   |

As an example let's make it for 280mhz and using steel rods

```
280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

X = 1.071/2 * 0.9 = 0.481m
Y = 1.071/2 = 0.535m
Z = 3/8 * 1.071 = 0.401m
```

Since it has circular polarization be sure to check on how to do the [wiring](/polarization.md)  

<img height="300" src="/../_img/antennas/turnstile_ex.jpg" />

### Sources:

[Alicia Space](https://alicja.space/blog/how-to-build-turnstile-antenna/)  
[ARRL Antenna Book for Radio Communications](https://www.arrl.org/arrl-antenna-book)