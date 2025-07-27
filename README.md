<img style="width: 100%; height: 100%" width="100%" class="lazy" src="[https://raw.githubusercontent.com/MSzturc/the100/main/Build_Photos/Top%20Banner%20Claim%20v2.png](https://github.com/v-tw0/ChimeraiXY/blob/main/Img/Banner1.png?raw=true)">


[![Banner 2](\Img\Banner2.png "Banner 2")](https://github.com/v-tw0/ChimeraiXY/blob/main/Img/Banner2.png?raw=true)
# Chimera iXY - CoreXY Build

A DIY CoreXY conversion of the Flsun i3 2017 3D printer. This project includes firmware and relevant 3D model files for the custom build. A Mingda Magician X with a burnt out mainboard and 20-pin ribbon cable was also used in this build. I chose the name 'Chimera' since this printer is essentially two completely different 3D printers with a ~5 year gap combined together to make a hybrid printer.

This is not only to demonstrate the ability of upcycling reprap in conjunction with modern printers, but also to prove that only linear rods, bearings and extrusions are needed to make a fast printer that rivals high end consumer printers, without the need of several hundred dollars worth of linear rails. You can use them if you have spare ones on hand.

**What's the objective of this project?** My main objective is not to make an insanely fast 3D printer, anything above 200mm/s is the goal with speeds near 500mm/s in mind. The primary objective is to make this printer as reliable as possible, moreso than the two bedslingers it was made out of. The Flsun (While a good printer for its time) is quite finicky to get quality models by today's standards, and the MMX was simply made out of cheap parts that probably didn't even pass QoS. This printer will primarily be used to build large electronic enclosures. 

## Overview of Specifications

- **Firmware**: Based on Marlin 2.1.2.5, Klipper Supported  
- **Controller Board**: Supports MKS Gen L vX.X, TinyBee vX.X, and Robin Nano v3.X.*
- **Build Type**: CoreXY mechanical configuration
- **PrintHead Speed**: Minimum 200mm/s. Up to 500mm/s (TBD)
- **Speed**: Up to 20k mm/s*s accel
- **Drivers**: Minimum TMC2209 UART required (>2.0A peak)
- **Build Volume**: 230mm^3
- **Hotend**: V6, all metal to be used in final. Supports PLA, PETG, ABS, ASA, TPU (>72D)

**Due to unforeseen circumstances, I have changed to the Robin Nano v3.1.* 

## Links
[Offical Summarized Documentation Page (Not finished, Work in Progress)](https://v-tw0.github.io/chimeradoc.html)
[Offical Full Documentation Page (To be published soon)](https://v-tw0.github.io/chimeradocfull.html)
[Bill of Materials](https://docs.google.com/spreadsheets/d/141LB089onZRFYBLwHDZm7xMRdjYpGHt4JvQGmjNZiB8/edit?gid=0#gid=0)

## Contents

- `Firmware/` – Marlin 2.1.2.5 configuration for MKS Gen L v1.0  
- `Model/` – 3D printable parts for CoreXY conversion (mounts, brackets, etc.)  
- `Doc/` – Rough Concept Sketches, Torque Curves, and printer setup details
- `Img/` – Images featured here, as well as some diagrams


## Update Log
**Current Status**: (7.26.25) [v0.8] Initial Physical Inspection and Testing underway. Lots of design files have been changed, optimized and improved.

(6.18.25) [v0.7] CoreXY Kinematics Design almost complete! Testing will begin once parts are recieved.  

(5.13.25) [v0.6] Adding initial repo files. Firmware is forked from original cartesian build (To be changed). Adding initial design for hotend carriage.

## Model Credits
Credits to the following models for making this possible. Please check them out:

- [1] 20 x 20 mm extrusion Power Source Unit (PSU) mount bracket – [[source/link](https://www.printables.com/model/457450-20-x-20-mm-extrusion-power-source-unit-psu-mount-b/files)]  
- [2] Bowden / PTFE Tube Coupler - Connect 2 Tubes – [[source/link](https://makerworld.com/en/models/664607-bowden-ptfe-tube-coupler-connect-2-tubes#profileId-591977)]  
- [3] E3D v6 dual 4010 fan duct – [[source/link](https://www.printables.com/model/239901-e3d-v6-dual-4010-fan-duct/files)]  
- [4] the100: 8mm linear rod gantry - [[source/link](https://github.com/MSzturc/the100/tree/main/STL/Gantry)]
- [5] MKS Gen L v1.0 Board Case (Compatible with Tinybee, Robin Nano, etc.) - [[source/link](https://www.thingiverse.com/thing:2239770)]
- [6] Case for Makerbase MKS TS35 V2.0 touchscreen - [[source/link](https://www.printables.com/model/83429-case-for-makerbase-mks-ts35-v20-touchscreen/comments)]

> This project is a work in progress.
