# Turnstile antenna

Esta antena es mejor que la dipolo ya que tiene polarización circular y también tiene un reflector para evitar irradiar en dirección al suelo.
Es basicamente una cross-yagi sin los elementos directores por lo que irradia en todas las direcciones.

<img height="450" src="/../_img/antennas/turnstile.png" />

Para la VF (factor de velocidad) de cada material se puede utilizar la siguiente tabla:

| Material								| VF          |
| ------------------------------------- | ----------- |
| Aluminio								| 0.94        |
| Bronce								| 0.95        |
| Cobre									| 0.95        |
| Auslantes (PVC,PE,Teflon)				| 0.94-0.98   |
| Hierro								| 0.90        |
| Acero									| 0.90        |
| Cobre aislado (Cobre*Aislante)		| 0.95*0.96   |

Haremos un ejemplo para 280mhz con barras de acero

```
280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

X = 1.071/2 * 0.9 = 0.481m
Y = 1.071/2 = 0.535m
Z = 3/8 * 1.071 = 0.401m
```

Ya que tiene polarizacion circular, se debe tener en cuenta el [cableado](/es/polarizacion.md)  

<img height="300" src="/../_img/antennas/turnstile_ex.jpg" />

### Fuentes:

[Alicia Space](https://alicja.space/blog/how-to-build-turnstile-antenna/)  
[ARRL Antenna Book for Radio Communications](https://www.arrl.org/arrl-antenna-book)