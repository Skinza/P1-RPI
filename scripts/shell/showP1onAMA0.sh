# set speed 9600, parity odd, 7 bit, 1 stopbit and ignore cr
stty -F /dev/ttyAMA0 9600 -parodd cs7 -cstopb igncr
cat /dev/ttyAMA0
