# Antena monopolo "bazuca"

Otra version de la antena monopolo un poco mas complicada de fabricar pero aun asi puede llegar al satelite con unos 10W de potencia.

<img height="450" src="/../_img/antennas/monopole_bazuca.png" />

En este ejemplo se muestra el calculo para 280mhz usando cable RG213 con una VF (factor de velocidad) de 0.66

```
280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

Longitud total = 1.071/4 = 0.267m
Longitud cable = (1.071/4)*0.66 = 0.176m
```

Es importante verificar las conexiones ya que la malla debe conectarse al pin central del conector PL y el nucleo del cable al neutro del conector.
Finalmente se puede poner algun tipo de proteccion de plastico o tubo termoretractil para protejer el cable.