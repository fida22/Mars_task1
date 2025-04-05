#!/bin/bash

#Create a new directory called rover_mission and navigate into it.
mkdir rover_mission
cd rover_mission

#Create three empty files named log1.txt, log2.txt, and log3.txt inside rover_mission.
touch log1.txt
touch log2.txt
touch log3.txt

#Rename log1.txt to mission_log.txt.
mv log1.txt mission_log.txt

#Find all files in the current directory that have a .log extension
find . -name "*.log"

#Display the contents of mission_log.txt without opening it in an editor
cat mission_log.txt

#Find and display all lines containing the word "ERROR" in mission_log.txt.
grep "ERROR" mission_log.txt

#Count the number of lines in mission_log.txt.++
wc -l mission_log.txt

#Show the system's current date and time.
date

#Display the CPU usage of your system in real time.
top

#Schedule a command to shut down the system in 10 minutes.
shutdown -h +10


