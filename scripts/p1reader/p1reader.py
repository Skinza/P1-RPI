#!/usr/bin/python
# imports
import signal
import sys
import serial
import time
import rrdtool

# defines
def saveTelegram(telegram):
	print "=================================="
	print "Tijdstip: %s" % (time.strftime("%d/%m/%Y %H:%M:%S"))
	for row in telegram:
		#print (row)
		if row[0:9] == "1-0:1.8.1":
			telegram_verbruikTotaalLaag = row[10:19]
			print "totaal verbruik laag tarief: %s kWh" % row[10:19]
		elif row[0:9] == "1-0:1.8.2":
			telegram_verbruikTotaalHoog = row[10:19]
                        print "totaal verbruik hoog tarief: %s kWh" % row[10:19]
		elif row[0:9] == "1-0:2.8.1":
			telegram_leveringTotaalLaag = row[10:19]
                        print "totaal levering laag tarief: %s kWh" % row[10:19]
                elif row[0:9] == "1-0:2.8.2":
			telegram_leveringTotaalHoog = row[10:19]
                        print "totaal levering hoog tarief: %s kWh" % row[10:19]
		elif row[0:11] == "0-0:96.14.0":
			telegram_tariefIndicator = row[12:16]
			sys.stdout.write("huidig tarief: ")
			if row[12:16] == "0000":
				print "onbekend (0000)"
			elif row[12:16] == "0001":
				print "Laag tarief"
			elif row [12:16] == "0002":
				print "Hoog tarief"
			else:
				print "geheel onbekend (%s)" % row[12:16]
		elif row[0:9] == "1-0:1.7.0":
			telegram_huidigVerbruik = row[10:17]
			print "huidig verbruik: %s kW" % row[10:17]
		elif row[0:9] == "1-0:2.7.0":
			telegram_huidigLeveren = row[10:17]
			print "huidige teruglevering: %s kW" % row[10:17]
	print "================================="
	rrdtool.update("/home/p1/p1reader/v1/p1.rrd","N:%s:%s:%s:%s:%s:%s:%s" % (telegram_verbruikTotaalHoog,telegram_verbruikTotaalLaag,telegram_leveringTotaalHoog,telegram_leveringTotaalLaag,telegram_tariefIndicator,telegram_huidigVerbruik,telegram_huidigLeveren))


# we are not running
running = 0

# catch signal
def signal_handler(signum,frame):
	running = 0
signal.signal(signal.SIGINT,signal_handler)

# config serial
serialPort = serial.Serial()
serialPort.baudrate = 9600
serialPort.bytesize = serial.SEVENBITS
serialPort.parity = serial.PARITY_EVEN
serialPort.stopbits = serial.STOPBITS_ONE
serialPort.port = "/dev/ttyAMA0"
serialPort.xonxoff = 0
serialPort.rtscts = 0
serialPort.timeout = 20

# try to open serial port
try:
	sys.stdout.write("connecting to %s... " % serialPort.port)
	serialPort.open()
except:
	print "failed"
	sys.exit("Unable to open %s" % serialPort.port)
print "connected"

# try reading
running = 1
inTelegram = 0
telegram=[]

while running:
	try: 
		rawp1Line = serialPort.readline()
	except:
		sys.exit("Error reading line from serial %s. Please investigate" % serialPort.port)
	
	p1Line = rawp1Line.strip()
	#print (p1Line)
	#print "waiting for start of telegram"
	if inTelegram != 1:
		if p1Line[0:1] == "/":
			#print "begin"
			inTelegram = 1
	else:
		if p1Line[0:1] == "!":
			#print "einde gevonden na een begin, nu parsen"
			#print "er zitten %s regels in telegram" % len(telegram)
			saveTelegram(telegram)
			telegram=[]
			inTelegram = 0
	if inTelegram == 1:
		# we hebben begin gevonden en zijn actief aan het verzamelen
		telegram.append(p1Line)
 
print "closing serial port"
serialPort.close()



	
