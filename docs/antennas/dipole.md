# Dipole antenna

This antenna works a bit better than the monopole altough is not so portable.

<img height="300" src="/../_img/antennas/dipole_ex.jpg" />

Tipically the total length of a dipole is calculated as

`L = λ/2 * VF`

So each leg of the dipole is `L/2`

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

As an example let's make it for 280mhz using Insulated copper

```
280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

Total length = 1.071/2*0.98*0.95 = 0.498m
Length of each leg = 0.498/2 = 0.249m
```

Most constructions however use a length of 0.235m for each leg as they take into consideration the separation between the active elements.
As always, it's better to use NanoVNA to do the final tunning of the antenna.

Some people add a director to this antenna. It will not work perfectly since it's very close to the active element but it makes the antenna a bit more directional

Usually the director has a length of 0.325m and is attached to the Banana using double side tape or 3d printed parts.

<img height="300" src="/../_img/antennas/dipole_instr.png" />

<img height="300" src="/../_img/antennas/dipole_dir_ex.jpg" />

### Sources:

[Youtube construction video](https://youtu.be/Q9kyX0oMdtQ?si=bD8NNUBlY7qiXXqT)