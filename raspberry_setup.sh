#!/bin/bash
apt-get install emacs -y
apt-get install arduino-core arduino-mk -y
apt-get install python3-pip -y
apt-get install python3-serial -y
apt-get install python3-rpi.gpio -y
apt-get install sqlite3 -y
apt-get install libdevice-serialport-perl -y
apt-get install libyaml-perl -y
apt-get install uild-essential -y
source install_phyton_packages.sh

cd /home/pi/rfid-arduino-raspberry/sketch && git clone https://github.com/miguelbalboa/rfid.git
rsync -va sketch/rfid sketch/sketch_catracas/
mv sketch/sketch_catracas/rfid/ sketch/sketch_catracas/MFRC522
cp -r sketch/sketch_catracas/MFRC522 /usr/share/arduino/libraries/

