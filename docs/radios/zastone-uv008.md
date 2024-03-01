# Zastone uv008

The Zastone (also sold as Vitai) uv008 is a handheld radio capable of comunicating with Satcom in DMR.

<img height="450" src="/../_img/radios/zastone_uv008.png" />

There are 3 versions of this radio. The only version that works with satcom without messing with software is v3 and as 
long as you don't buy a used model you should recieve the v3 version

<img height="450" src="/../_img/radios/uv008_models.jpg" />

It has a power of around 10W in the satcom frequencies.
The only limitations are the firmware and cps that have some limtations.

To transmit in DMR you need to have the TX on the VFO A and the RX on VFO B (or the inverse) as the firmware doesn't accept offsets when  using DMR

<img height="350" src="/../_img/radios/uv008_dmr.png" />

Also the CPS is not very user friendly and it cannot import channels or zones.
As a solution, [here](https://satcomradio.github.io/_files/zastone_cps.cps) you have an example of a CPS with most of the Satcom channels.

You can also get the latest firmware [here](https://satcomradio.github.io/_files/zastone_uv008_fw.rar)

Recently (January 2024) there have been attempts to dissasemble the firmware and implement custom firwares.
To do so, you can dissasembly the firmware .bin with the *cutter dissasembler* specifying *mcore* as the architecture and *c-sky* as the CPU

### Sources:

[Zastone info website](https://telegra.ph/Instrukciya-programmirovaniya-Zastone-UV008-v3-s-AES256-04-03)  
[Zastone UV008 Telegram group (Russian)](https://t.me/ZastoneUV008)  