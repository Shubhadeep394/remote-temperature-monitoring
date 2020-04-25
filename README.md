# Remote Temperature Monitoring 
Sending an alert on Telegram when Temperature Crosses Threshold

This code fetchs the temperature data collected by Bolt IoT wifi module and send alert messege over telegram if the temperature
value crosses a certain threshold.

Hardware Connections For Temperature Monitor using BOLT
Hardware required
1. The Bolt Wifi module
2. Three female to male wire
3. Temperature Sensor: LM35 sensor

Connecting the LM35 sensor to the Bolt
Firstly, Hold the sensor in a manner such that you can read LM35 written on it.In this position, identify the pins of the sensor as VCC, Output and Gnd from your left to right.Now connect accordingly,
1. VCC pin of the LM35 connects to 5v of the Bolt Wifi module.
2. Output pin of the LM35 connects to A0 (Analog input pin) of the Bolt Wifi module.
3. Gnd pin of the LM35 connects to the Gnd.
The final circuit should look like the image below:
<img src="https://github.com/Shubhadeep394/remote-temperature-monitoring/blob/master/images/circuit.JPG" width="300" height="200">
That's it.