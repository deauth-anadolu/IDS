#!/bin/bash

# Function to be called on exit
on_exit() {
	sudo airmon-ng stop wlp3s0mon;
}

# Set the trap to call the on_exit function on EXIT signal
trap on_exit EXIT


sudo airmon-ng start wlp3s0;
sleep 3

# Check if the second argument is "saver"
if [ "$1" == "saver" ]; then
    sudo python3 save_network.py
else
    sudo python3 main.py
fi

# Loop to keep the script running until Ctrl+C is pressed
echo "Press Ctrl+C to stop the script."
while true; do
    sleep 1
done
