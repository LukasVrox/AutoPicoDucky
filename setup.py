import shutil
import os
import time
import getpass
from os import path


input = input('Please enter your Drive letter of the pico: ')
print('You selected ' + input)
checkpath = path.exists('F:/lib')
username = getpass.getuser()
src = 'C:/Users/' + username + '/Desktop/Python/DuckyPySetup/CircuitPython.uf2'
src1 = 'C:/Users/' + username + '/Desktop/Python/DuckyPySetup/Bundle/lib/adafruit_hid'
src2 = 'C:/Users/' + username + '/Desktop/Python/DuckyPySetup/pico-ducky-main/duckyinpython.py'
src3 = 'C:/Users/' + username + '/Desktop/Python/DuckyPySetup/flash_nuke.uf2'
#print(src)
dst =  input + ':/'
dst1 = input + ':/lib/adafruit_hid'

def inst():
    shutil.copy(src, dst)
    print('Making Circuitpy')
    time.sleep(7)
    print('Copy adafruit_hid to /lib on the Pi')
    shutil.copytree(src1, dst1)
    time.sleep(3)
    print('Copy duckyinpython to' + input)
    shutil.copy(src2, dst)
    time.sleep(3)
    print('remove code.py')
    os.remove(input + ':/code.py')
    time.sleep(3)
    print('Rename duckyinpython to code.py')
    os.rename(input + ':/duckyinpython.py', input + ':/code.py' )

def start():
    if checkpath == False:
        print('NUKING THE PI!!!')
        shutil.copy(src3, dst)
        print('Wait 10 for pi reboot')
        time.sleep(10)
        inst()
    elif checkpath == True:
        print('Pi is installed, please reset')

start()


