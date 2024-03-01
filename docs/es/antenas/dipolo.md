# Antena dipolo

Esta antena funciona mejor que la monopolo pero es menos portatil.

<img height="300" src="/../_img/antennas/dipole_ex.jpg" />

Por norma general su longitud se calcula con la formula

`L = λ/2 * VF`

Por lo que cada pata de la dipolo tiene una longitud de `L/2`

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

Realizaremos un ejemplo para 280mhz usando cobre con aislante

```
280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

Longitud total = 1.071/2*0.98*0.95 = 0.498m
Longitud de cada pata = 0.498/2 = 0.249m
```

La mayoria de las construcciones utilizan 0.235m para cada pata ya que tambien calculan la distancia de separacion entre los elementos radiantes.
Como siempre, es mejor utilizar el NanoVNA para hacer los ajustes finales.

Algunas personas añaden un director a la antena. No va a funcionar a la perfeccion ya que la distancia es 
muy corta pero consige transformarla en una antena mas direccional

Por lo general el director tiene una longitud de 0.325 y se une al conector banana usando cinta de doble cara o piezas impresas en 3d.

<img height="300" src="/../_img/antennas/dipole_dir_ex.png" />
<img height="300" src="/../_img/antennas/dipole_dir_ex2.jpg" />

### Fuentes:

[Youtube construction video](https://youtu.be/Q9kyX0oMdtQ?si=bD8NNUBlY7qiXXqT)