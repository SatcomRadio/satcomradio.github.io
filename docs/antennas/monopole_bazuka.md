# Monopole antenna "bazuca"

Another version of the monopole antenna a bit more difficult to make but it still can reach the satellite with around 10W of power

<img height="450" src="/../_img/antennas/monopole_bazuca.png" />

As an example let's make it for 280mhz using RG213 wire with a VF of 0.66

```
280mhz = 28000000hz
λ = c/f = 299792458/28000000 ≃ 300/280 = 1.071m

Total length = 1.071/4 = 0.267m
Wire length = (1.071/4)*0.66 = 0.176m
```

It's important that you check the connections since the mesh goes to the central pin of the PL connector and the core goes to the ground.
You can put some plastic cap and heat shrink tube at the top to protect it.