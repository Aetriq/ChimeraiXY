# Chimera iXY - CoreXY Build

![Banner 1](https://github.com/Aetriq/ChimeraiXY/blob/main/Img/chimera%20v2.1%20-%20compressed.png?raw=true)
![Banner 2](https://github.com/Aetriq/ChimeraiXY/blob/main/Img/Banner3.png?raw=true)

A DIY CoreXY conversion of the Flsun i3 2017 3D printer. This project includes firmware and relevant 3D model files for the custom build. A Mingda Magician X with a burnt out mainboard and 20-pin ribbon cable was also used in this build. I chose the name 'Chimera' since this printer is essentially two completely different 3D printers with a ~5 year gap combined together to make a hybrid printer.

This is not only to demonstrate the ability of upcycling reprap in conjunction with modern printers, but also to prove that only linear rods, bearings and extrusions are needed to make a fast printer that rivals high end consumer printers while being at a lower cost.

**What's the objective of this project?** My main objective is not to make an insanely fast 3D printer, anything above 200mm/s is the goal with speeds near 500mm/s in mind. Instead, I wanted to make this printer as reliable as possible, moreso than the two bedslingers it was made out of. The Flsun (While a good printer for its time) is obviously last gen, so it's quite finicky to get quality models by today's standards, and the MMX was simply made out of cheap parts that probably didn't even pass QoS (there's also alot of review online of mingda printers using parts with questionable quality). This printer will primarily be used to build large electronic enclosures. 

**LATEST UPDATE LOG (v2.4):** - Added a nozzle cleaning system, including a ptfe wiper and nozzle brush. Partially inspired by the system seen on bambu's a1 series, this system works very well and the klipper config has been updated accordingly.
- Added an auxillary cooling fan, a 120x25mm axial 150CFM fan. This should've been a centrifugal blower but I had this one on hand and it pushes a decent amount of H20 pressure.
- Quality of life improvements to firmware, including the implementation of above. Thermal testing of steppers made me stay at 1.2A RMS for X and Y motors.

## Overview of Specifications

- **Firmware**: Klipper & MainsailOS. Marlin 2.1.2.5 continues to be supported.  
- **Controller Board**: Supports MKS Gen L vX.X, TinyBee vX.X, and Robin Nano v3.X.*
- **Build Type**: CoreXY mechanical configuration
- **Speed**: Quality Prints @ 300mm/s. Travel speeds up to 800mm/s.
- **Accel**: Up to 20k mm/s*s accel
- **Drivers**: Minimum TMC2209 UART required (>2.0A peak)
- **Build Volume**: 230mm^3
- **Extrusion**: E3D Titan Extruder Direct Drive or Bowden.
- **Hotend**: V6 volcano or normal w/ all-metal heatbreak. Supports PLA, PETG, ABS, ASA, TPU (>72D)

**Due to unforeseen circumstances, I have changed to the Robin Nano v3.1.* ### Experimental Results
Below is a comparison of the donor hardware versus the theoretical goals and final experimental data. In conclusion, alot of my project goals were met and even exceeded in some cases!

| Specification | Flsun i3 (Donor 1) | Mingda Magician X (Donor 2) | Planned Theoretical Goal | Experimental Results |
| :--- | :--- | :--- | :--- | :--- |
| **Max Print Speed** | ~100 mm/s | ~80-120 mm/s | 200-500 mm/s | 200-450mm/s|
| **Max Travel Speed** | ~150 mm/s | ~200 mm/s | 500+ mm/s | 800mm/s |
| **Max Acceleration** | ~1000 mm/s² | ~1500 mm/s² | 20000 mm/s² | 32000 mm/s² (according to input shaping)|
| **Volumetric Flow Rate** | ~8 mm³/s | ~10-12 mm³/s | >20 mm³/s | 40 mm³/s|
| **Build Volume** | 220x220x220 mm | 230x230x260 mm | 230x230x230 mm | 230x230x230 mm|
| **Kinematics** | Cartesian | Cartesian | CoreXY | CoreXY |

## Links

- [Official Page](https://aetriq.xyz/chimera.html)
- [Wiki Page](https://github.com/Aetriq/ChimeraiXY/wiki/Wiki-Page-%E2%80%90-Chimera-iXY-v2.0)
- [Full Documentation](https://aetriq.xyz/chimeradocfull.html)
- [Bill of Materials](https://aetriq.xyz/chimeradocfull.html#bom)

## Contents

- `Firmware - Mainboard/` – Klipper & Marlin 2.1.2.5 configuration for MKS Robin Nano v3.1. 
- `Firmware - ESP8266/` – Configuration for MKS Wifi v1.0. Only used in Marlin Build. 
- `Config/` - Slicer Profiles, Bootscreen, etc.
- `Model/` – 3D printable parts for CoreXY conversion (mounts, brackets, etc.)  
- `Doc/` – Rough Concept Sketches, Torque Curves, and printer setup details
- `Img/` – Images featured here, as well as some diagrams

## Configuration
Refer to config folder for start gcode for marlin, or firmware for klipper start/end gcode. This printer works optimally on both superslicer or prusaslicer but supports any marlin flavored gcode.


## Model Credits
Credits to the following models for making this possible. Please check them out:

- [1] 20 x 20 mm extrusion Power Source Unit (PSU) mount bracket – [[source/link](https://www.printables.com/model/457450-20-x-20-mm-extrusion-power-source-unit-psu-mount-b/files)]  
- [2] Bowden / PTFE Tube Coupler - Connect 2 Tubes – [[source/link](https://makerworld.com/en/models/664607-bowden-ptfe-tube-coupler-connect-2-tubes#profileId-591977)]  
- [3] E3D v6 dual 4010 fan duct – [[source/link](https://www.printables.com/model/239901-e3d-v6-dual-4010-fan-duct/files)]  
- [4] the100: 8mm linear rod gantry - [[source/link](https://github.com/MSzturc/the100/tree/main/STL/Gantry)]
- [5] KP3S PSU 120mm fan adapter (ZL-360-24) - [[source/link](https://www.thingiverse.com/thing:6010144)]
- [6] Case for Makerbase MKS TS35 V2.0 touchscreen - [[source/link](https://www.printables.com/model/83429-case-for-makerbase-mks-ts35-v20-touchscreen/comments)]
- [7] Drag Cable Chain(s) - [[source/link](https://www.printables.com/model/34894-drag-cable-chains/files)]
- [8] Modification pack, Ender 5 plus, KAY3D CoreXY. - [[source/link](https://www.thingiverse.com/thing:4643208/files)]


## Software Credits
- [1] Autodesk Fusion [[source/link](https://www.autodesk.com/products/fusion-360/personal)]
- [2] PrusaSlicer [[source/link](https://www.prusa3d.com/page/prusaslicer_424/)]
- [3] SuperSlicer [[source/link](https://superslicer.net/)]
- [4] Klipper [[source/link](https://www.klipper3d.org/)]
- [5] Configuration for MKS TS35 V2.0 working with klipper screen [[source/link](https://github.com/NamkingWIN/3d_print/wiki/Configuration-for-MKS-TS35-V2.0-working-with-klipper-screen)]
- [6] StepperSim [[source/link](https://github.com/rcarlyle/StepperSim)]