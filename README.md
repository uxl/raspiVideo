### prepare pi for python
```
sudo apt-get install python
sudo apt-get install python-dev
sudo apt-get install libjpeg-dev
//sudo apt-get install libfreetype6-dev
sudo apt-get install python-setuptools
sudo apt-get install python-pip
sudo apt-get install libffi-dev
```

####With this done, now its time to install the required Python libraries but first, update the Python distribution by running

```sudo easy_install -U distribute```

Finally you can install the Raspberry Pi GPIO (General Purpose Input/Ouput) and other packages:

```
sudo pip install RPi.GPIO
sudo pip install pySerial
sudo pip install nose
sudo pip install cmd2
```

### install MP4 converter
```sudo apt-get update```
```sudo apt-get install gpac```

####Usage
```MP4Box -add filename.h264 filename.mp4```

### run app
```sudo python photoboard.py```

