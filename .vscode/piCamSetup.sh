#!/bin/bash
#Downloads WiringPi and Builds the Code
cd /PATH/WHERE/IT/WILL/BE/SAVED (WIRINGPI)
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
#DO GPIO SETUP FOLDERS

gpio 7 out
gpio 11 out
gpio 12 out


echo 'Setup Complete'