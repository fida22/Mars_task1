#!/bin/bash

#generating random battery percentage
battery=$((RANDOM%101))

#checking for battery availabiltiy
if [[ $battery -lt 20 ]] 
then
	echo "battery low! Return to base!">>log.txt
	exit 1
fi

#checking for connectivity
if ! ping -c 4 google.com &> /dev/null
then
	echo "Communication Failure!">>log.txt
	exit 1
fi

#All conditions met
  echo "All systems operational!">>log.txt


