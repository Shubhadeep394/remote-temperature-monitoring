# **Remote Temperature Monitoring** 

Sending an alert on Telegram when Temperature Crosses Threshold

In this project the code fetchs the temperature data collected by Bolt IoT wifi module and send alert messege over telegram if the temperature
value crosses a certain threshold.


#### Hardware Required
```
1. The Bolt Wifi module
2. Three female to male wire
3. Temperature Sensor: LM35 sensor
```
#### Hardware Connection
```
Connecting the LM35 sensor to the Bolt
Hold the sensor in a manner such that you can read LM35 written on it.
In this position, identify the pins of the sensor as VCC, Output and Gnd from your left to right.
Now connect accordingly,
1. VCC pin of the LM35 connects to 5v of the Bolt Wifi module.
2. Output pin of the LM35 connects to A0 (Analog input pin) of the Bolt Wifi module.
3. Gnd pin of the LM35 connects to the Gnd.
```
>The final circuit should look like the image below:
<img src="https://github.com/Shubhadeep394/remote-temperature-monitoring/blob/master/images/circuit.JPG" width="300" height="200">

#### Creating a Virtual Private Server (VPS)
You can create a virtual private server in Two ways,
>1. By creating a [**Digital Ocean Droplet**](https://www.youtube.com/watch?v=vqZ7eKM0WS8).
>2. By creating a [**Ubuntu Server**](https://www.youtube.com/watch?v=7QIf4sf6DM0) using a Virtual Machine on your local Desktop/Laptop.

You can also use your **Raspberry Pi** as your VPS and access it using puTTY (for Windows Users).

#### Setup your Telegram
To setup your Telegram [click here]()

#### Receiving Alerts
Before running the code make sure you have installed python and the nescessary libraries for running the code in your VPS
Update the packages on Ubuntu using the following command,
```python
sudo apt-get -y update
```
Install python3 pip3 using the following command,
```python
sudo apt install python3-pip
```
Install boltiot python library using the following command,
```python
sudo pip3 install boltiot
```
Now, type in the code and run the code in your server (don't forget to modify [conf.py](https://github.com/Shubhadeep394/remote-temperature-monitoring/blob/master/conf.py) according to your own Hardware and Software Configurations).
>Run the code using the following command,
```python
python telegram_alert.py
```

