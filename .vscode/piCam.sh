#!/bin/bash

gpio 7 write 1
gpio 11 write 0
gpio 12 write 0
capture(1)

gpio 7 write 1
gpio 11 write 0
gpio 12 write 1
capture(2)

gpio 7 write 0
gpio 11 write 1
gpio 12 write 0
capture(3)

function capture(cam){
    rapistill -o capture$cam.png
}

exit