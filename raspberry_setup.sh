#!/bin/bash
apt-get install emacs
apt-get install arduino-core arduino-mk
apt-get install python3-pip
apt-get install python3-serial
apt-get install sqlite3
apt-get install libdevice-serialport-perl
apt-get install libyaml-perl
apt-get install uild-essential
source install_phyton_packages.sh


cp -r sketch/rfid/ sketch/sketch_catracas/
mv sketch/sketch_catracas/rfid/ sketch/sketch_catracas/MFRC522
cp -r sketch/sketch_catracas/MFRC522 /usr/share/arduino/libraries/

