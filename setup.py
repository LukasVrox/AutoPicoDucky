import shutil
import os
import time
import getpass
from os import path

print ("""
  ____        _     _               
 |  _ \ _   _| |__ | |__   ___ _ __ 
 | |_) | | | | '_ \| '_ \ / _ \ '__|
 |  _ <| |_| | |_) | |_) |  __/ |   
 |_|_\_\\__,_|_.__/|_.__/ \___|_|   
 |  _ \ _   _  ___| | ___   _       
 | | | | | | |/ __| |/ / | | |      
 | |_| | |_| | (__|   <| |_| |      
 |____/ \__,_|\___|_|\_\\__, |      
 |  _ \(_) ___ ___      |___/       
 | |_) | |/ __/ _ \                 
 |  __/| | (_| (_) |                
 |_|   |_|\___\___/ 


 Reset Pico before use!! 
 Press big white Button on startup!
""")

input = input('Please enter the Drive letter of the Raspberry Pico: ')
length = len(input)
typee = type(length)
check1 = ':'


if ':' in input:
    print('Please type the letter without ":"')
    exit()
elif length > 2 :
    print('Thats not possible')
    exit()

print('You selected ' + input)

checkpath = path.exists(input + ':/lib')

src = 'CircuitPython.uf2'
src1 = 'Bundle/lib/adafruit_hid'
src2 = 'pico-ducky-main/duckyinpython.py'
src3 = 'flash_nuke.uf2'

dst =  input + ':/'
dst1 = input + ':/lib/adafruit_hid'

def inst():
    shutil.copy(src, dst)
    print('Making Circuitpy')
    time.sleep(7)
    print('Copy adafruit_hid to /lib on the Pi')
    shutil.copytree(src1, dst1)
    time.sleep(3)
    print('Copy duckyinpython to ' + input)
    shutil.copy(src2, dst)
    time.sleep(3)
    print('remove code.py')
    os.remove(input + ':/code.py')
    time.sleep(3)
    print('Rename duckyinpython to code.py')
    os.rename(input + ':/duckyinpython.py', input + ':/code.py' )
    check_lib = path.exists(input + ':/lib/adafruit_hid')
    if check_lib == True:
        print('Setup is complete')
        exit()
    else:
        print('Something went wrong with the setup. Please try it again')

def start():
    if checkpath == False:
        time.sleep(1)
        print('Flashing Py to factory defaults...')
        shutil.copy(src3, dst)
        print('Wait 10sec for the pi to reboot..')
        time.sleep(10)
        inst()
    elif checkpath == True:
        time.sleep(1)
        print('Pi is installed, please reset..')

start()


