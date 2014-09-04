#!/bin/bash
rrdtool graph test.png \
	--start -2h \
	--end now \
	DEF:verbruikHuidig=p1.rrd:huidigVerbruik:AVERAGE \
	CDEF:verbruikHuidigWatt=verbruikHuidig,1000,* \
	LINE2:verbruikHuidigWatt#FF0000
