# AutoPicoDucky

Script is setting up a Raspberry Pi Pico to function as a USB Rubber Ducky.

It only works on ```Windows``` !

You first need to manually reset the Pico by pressing the white button on startup.

After that, the Pi will on default contain 2 Files. 

It will first flash the Pi, restart it and install the Circuitpython.
After Circuitpython is installed, it will reboot. After reboot, it is going to add the adafruit _hid to the /lib folder on the Pi.
When that is complete, it adds the duckyinpython.py file, and renames it to code.py.

After all that is complete, you can easily copy Ducky Script (.dd) files onto the system.
Careful!! When a .dd file is added, it will instantly run the ducky script.

Have fun!
