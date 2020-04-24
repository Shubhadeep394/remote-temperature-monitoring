# remote-temperature-monitoring

Hardware Connections For Temperature Monitor using BOLT
Hardware required
1. The Bolt Wifi module
2. Three female to male wire
3. Temperature Sensor: LM35 sensor

Connecting the LM35 sensor to the Bolt
Step 1: Hold the sensor in a manner such that you can read LM35 written on it.
Step 2: In this position, identify the pins of the sensor as VCC, Output and Gnd from your left to right.
In the above image, VCC is connected to the red wire, Output is connected to the orange wire and
Gnd is connected to the brown wire.
Step 3: Using male to female wire connect the 3 pins of the LM35 to the Bolt Wifi Module as follows:
● VCC pin of the LM35 connects to 5v of the Bolt Wifi module.
● Output pin of the LM35 connects to A0 (Analog input pin) of the Bolt Wifi module.
● Gnd pin of the LM35 connects to the Gnd.
The final circuit should look like the image below:
That's it.