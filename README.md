### linuxino

### changing linux sound volume with a potentiometer 

we can using potentiometer and arduino changing sound volume of linux os live

#### What do we need ?
- Arduino
- potentiometer
- breadboard
- a few jumper wire

#### run
### Step 1 : making the circuit

first of all you have to making circuit like the below picture :

[4.jpg link]

### Step 2 : initialize arduino for programming

after making the circuit in step 1, you have to connect your arduino to your PC and in arduino IDE and choose your Arduino type: 

[1.png link]

Make sure the Arduino is connected to the computer via the Tools -> port tab, and also remember the name of the device (in this case, the device is /dev/ttyUSB0).

[2.png link]


Finally, bring up the desired code from the File -> examples -> Firmata -> standardFirmata tab 

[3.png link]

### Step 3 : stating Arduino programming via python

first before doing anything install required python libraries from src/requiremets.txt

``` sh
pip install -r src/requirements.txt
```

also we have to change the source file and put our device name : 

``` python
...
device = "/dev/ttyUSB0" # change this
...
```

Now we can run the code : 

``` sh
python src/PotentiometricSoundChanger.py 
```

#### at the end we can see that we can changing sound volume using a potentiometer.